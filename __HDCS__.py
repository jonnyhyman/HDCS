'''---------------------------------------------------------------------------

Copyright (C) 2017, Jonathan "Jonny" Hyman

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

-------------------------------------------------------------------------------

Rocket Project
Human Controlled Digital Control Station
https://github.com/jonnyhyman/HDCS

    - Connect to Autonomous DCS
    - Display data intuitively for human observation
    - Provide human override and control switches GUI
    - Log data for debriefs
    - Plot all instrumentation live for human observation
    - Pass test configurations to ADCS for upstream briefing
    - Notify ADCS to do upstream uploading to specific micros

-----------------------------------------------------------------------------
'''

VERSION = 7.30

import sys
import ctypes

myappid = 'hdcs' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid) # for icon

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QPropertyAnimation as QAnimate
from PyQt5.QtCore import QSequentialAnimationGroup as QSeqAnimate

import Plotting as plot
import GUI_design as design
import GUI_colors as colors
import GUI_actions as actions
import GUI_procedures as proc
import Test_definition as TestDef
import Definitions

from GUI_accessories import Dialog, Upload, Reset, Sound
from Actuation import Wireless_Control
from GUI_custom import labelRect
from State_thread import Thread
from ADCS_Link import ADCS_Link
from Log_state import Log

import math
from time import *
import numpy as np
import subprocess
import socket

class Interface(QtWidgets.QMainWindow,design.Ui_MainWindow):
    def __init__(self,parent=None):
        """ Initialize the GUI's interface """
        super(self.__class__, self).__init__()
        self.scene = QtWidgets.QGraphicsScene(QtCore.QRectF(0,0,1260, 1000),self)
        self.stateLabels  = {}
        self.plots        = []
        self.livelog_keys = []
        self.averages     = {}
        self.last_m0_check= time()

        self.setupUi(self)
        self.setupGraphicsView()
        self.refactorUi()
        self.view.setRenderHints(QtGui.QPainter.Antialiasing)

        self.Alarms       = Definitions.Alarms
        self.State        = Definitions.State

        self.Command      = Definitions.Command
        self.l_State      = dict(self.State)
        self.l_Cmd        = dict(self.Command)
        self.l_Alarms     = dict(self.Alarms)
        self.l_Caution    = time() # required for sound timing

        self.State_Hist   = [self.State]
        self.State_Limits = Definitions.State_Limits
        self.State_Limits_keys = Definitions.State_Limits_keys
        self.procs = proc.ProceduresWidget(self.procedures,self)
        self.sound_controller = Sound()

        actions.updateAnnunciator(self,'init')
        actions.updateLiveLog(self,init=True)
        self.tdf = TestDef.TestDefinition()
        self.log = Log([self.State,self.Command])

        self._Thread = Thread(self)

        # This mega-block connects buttons with functions
        self.f1_button.clicked.connect(self.f1_trigger)
        self.f2_button.clicked.connect(self.f2_trigger)
        self.log_button.clicked.connect(self.log_toggle)
        self.testdef_button.clicked.connect(self.tdf.open)
        self.fire_button.clicked.connect(self.fire_trigger)
        self.livelog_expand.clicked.connect(self.livelog_toggle)
        self.reconnect_button.clicked.connect(self.adcs_reconnect)
        self.livelog_clear_button.clicked.connect(self.livelog_clear)
        self.livelog_freeze_button.clicked.connect(self.livelog_freeze)
        self.proc_next_button.clicked.connect(self.procs.next_procedure)
        self.tdf.uploadButton.clicked.connect(self.testDefinition_upload)
        self.count_set_button_expand.clicked.connect(self.count_set_toggle)
        self.count_set_button.clicked.connect(self.count_set_command)
        self.upload_button.clicked.connect(self.open_uploads_window)
        self.warning_alarm.clicked.connect(self.reset_warning)
        self.caution_alarm.clicked.connect(self.reset_caution)
        self.reset_button.clicked.connect(self.reset_device)
        self.count_button.clicked.connect(self.count_toggle)
        self.stop_button.clicked.connect(self.stop_toggle)
        self.arm_button.clicked.connect(self.arm_toggle)
        self.b1_toggle.clicked.connect(self.b1_trigger)
        self.b2_toggle.clicked.connect(self.b2_trigger)

        self.newplot_button.clicked.connect(lambda: actions.addPlot(self))
        self.stopplots_button.clicked.connect(lambda: actions.closePlots(self))
        self.plotfreeze_button.clicked.connect(lambda x: actions.freezePlots(self,x))
        self._Thread.state_emitter.connect(lambda x: actions.updateState(self,x))

        self.animations   = []
        self.f1_toggle(independently_animated=False,force_deactivate=True)
        self.f2_toggle(independently_animated=False,force_deactivate=True)

        self.dt_timer = QtCore.QTimer()
        self.dt_timer.timeout.connect(lambda: actions.updateState(self,
                                                                  self.State))
        self.dt_timer.start(500)

        # Establish wireless control link(s)
        self.Command_F2  = Wireless_Control(ip="192.168.2.1",port=18015)

        self._Thread.get_gui(self)
        self._Thread.start()

    def setupGraphicsView(self):
        ''' Initialize the line visual dynamic lines between objects '''

        self.view = QtWidgets.QGraphicsView(self.scene,parent=self.centralwidget)
        self.view.setMinimumSize(QtCore.QSize(1260, 1000))
        self.view.setStyleSheet("background-color: transparent;")
        self.lines = actions.makeLines(self,self.scene,self.view)
        self.view.lower() # "send to the back" so we can click our buttons
        self.plotDropFrame.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents)

    def refactorLabel(self,label_name,label,cmd):
        """ Convert a specific QLabel into QGraphicsItems """

        # Get proper global position for the label (only works 1 level deep)
        if label.parent()!=self.centralwidget:
            xpos = (label.x()+label.parent().x())
            ypos = (label.y()+label.parent().y())
        else:
            xpos = label.x()
            ypos = label.y()

        # Extract attributes in the stylesheet, if they aren't there, make transparent
        try:
            txcolor = actions.extractCSS(label.styleSheet(),'color')
        except ValueError:
            txcolor = 'transparent'

        try:
            bgcolor = actions.extractCSS(label.styleSheet(),'background-color')
        except ValueError:
            bgcolor = 'transparent'

        try:
            bdcolor = actions.extractCSS(label.styleSheet(),'border')
        except ValueError:
            bdcolor = 'transparent'

        try:
            bdcolor = bdcolor[bdcolor.index('solid')+len('solid'):]
        except ValueError:
            bdcolor = 'transparent'


        # Replace spaces with empty so QColor can parse
        txcolor = txcolor.replace(' ','')
        bgcolor = bgcolor.replace(' ','')
        bdcolor = bdcolor.replace(' ','')

        # Grab the text and font from the label, as well as the width and height
        text = label.text()
        font = label.font()
        wide = label.width()
        high = label.height()

        # Create the pen and brush for the background + foreground rects
        bgpen    = QtGui.QPen(QtGui.QColor(bdcolor))
        bgbrush  = QtGui.QBrush(QtGui.QColor(bgcolor), QtCore.Qt.SolidPattern)
        fgbrush  = QtGui.QBrush( QtGui.QColor(txcolor), QtCore.Qt.SolidPattern )

        # Create the label background, shift width by 2 because graphics items
        # have OUTER borders and labels have INNER borders! :)
        bg_label = labelRect(self, label_name,
                             xpos, ypos, wide-2, high-2, bgpen, bgbrush)

        self.scene.addItem(bg_label)

        fg_label = self.scene.addSimpleText(text, font)

        fg_rect = fg_label.boundingRect()

        if not cmd:
            # Not-command blocks are left-justified
            fg_label.setX( xpos + 0.1*wide  )
        else:
            # Command blocks have their names in the middle
            fg_label.setX( xpos-1 + wide/2 - fg_rect.width()/2)

        # All blocks have the same Y position rules (center)
        fg_label.setY( ypos-1 + high/2 - fg_rect.height()/2 )

        # Color the foreground text + Turn the template label off... We're done!
        fg_label.setBrush( fgbrush )
        label.setVisible(0)

        # Determine the type of display this is, and flag it
        if bgcolor.lower() == 'white':
            if 'xxx.' in label.text():
                flag = 'csd1' # color-state & display text as state
            else:
                flag = 'csd0' # color-state & don't display text as state
        else:
            if 'xxx.' in label.text():
                flag = 'bsd1' # background-color-state & display text as state
            else:
                flag = 'bsd0' # background-color-state & don't display text as state

        self.stateLabels[label_name] = (flag,fg_label,bg_label)

    def refactorUi(self):
        """ Convert all state labels into graphics elements for quicker realtime
            updates, and hide the old labels
        """

        All = self.centralwidget.findChildren(QtWidgets.QLabel)
        Labels = {obj.objectName():obj for obj in All}

        for name,label in Labels.items():
            if name in Definitions.State.keys():
                cmd = (name in Definitions.Control_Keys)
                self.refactorLabel(name,label,cmd)

        self.stateLabel_keys = self.stateLabels.keys()

    def adcs_reconnect(self):
        """ Force reconnect to the ADCS after a disconnect """
        try:
            print('Interface.adcs_reconnect')
            self._Thread.ADCS.reconnect()
        except Exception as e:
            self.d=Dialog(reason=e,function='adcs_reconnect')

    def open_uploads_window(self):
        """ Instantiate and open the micro uploads window """
        self.uploadsWindow = Upload(self.Command)

    def reset_device(self):
        """ Reset button call """
        self.resetWindow = Reset(self)

    def sound(self,selection):
        self.sound_controller.play(selection)

    def testDefinition_upload(self):
        """ Connected to the UPLOAD button in the Test Def window, this function
            commands a test matrix upload, and the actual UPLOAD occurs when the
            TM ("Test Matrix") State Variable is detected == 1 in actions.updateState.
        """
        if self.tdf.TestMatrix: # will be NONE if max length is exceeded
            if self._Thread.ADCS.connected:
                self.Command['TM'] = 1 # Command a test matrix upload
                print('>>TM COMMAND QUEUED<<')
            else:
                self.d=Dialog(reason='ADCS not yet connected!',
                            function='testDefinition_upload')

    def look_for_linekey(self, node1, node2):
        ''' Look for the line with node1 and node2 keys as its nodes'''
        for key in self.lines.keys():
             if (node1 in key) and (node2 in key):
                 return key

    def geometry_animate_setup(self,obj,start,end,reverse=False):
        ''' Register all animations to be played soon '''

        if type(start) in [list,tuple]:
            try:
                start = QtCore.QRect(start[0],start[1],start[2],start[3])
            except KeyError:
                raise('KeyError: start too few arguments, needs 4 for geometry')
        if type(end) in [list,tuple]:
            try:
                end = QtCore.QRect(end[0],end[1],end[2],end[3])
            except KeyError:
                raise('KeyError: end too few arguments, needs 4 for geometry')

        self.animations += [QAnimate(obj,b'geometry')]
        if not reverse:
            self.animations[len(self.animations)-1].setStartValue(start)
            self.animations[len(self.animations)-1].setEndValue  (end)
        else:
            self.animations[len(self.animations)-1].setStartValue(end)
            self.animations[len(self.animations)-1].setEndValue  (start)
        self.animations[len(self.animations)-1].setEasingCurve(QtCore.QEasingCurve.OutQuint)

    def geometry_animate_start(self):
        ''' Start all recently registered animations '''
        for animation in self.animations:
            animation.start()

    def shake_animate(self,shake_me):
        ''' Make the "shake_me" input object shake breifly '''
        start = QtCore.QPointF(shake_me.x(),shake_me.y())
        end   = QtCore.QPointF(shake_me.x()+5,shake_me.y())
        self.animation_seq = QSeqAnimate()

        for n in range(5):
            animation = QAnimate(shake_me,b'pos')
            animation.setDuration(50)
            if n % 2 == 0:
                animation.setStartValue(end)
                animation.setEndValue  (start)
            else:
                animation.setStartValue(start)
                animation.setEndValue  (end)
            animation.setEasingCurve(QtCore.QEasingCurve.OutQuint)
            self.animation_seq.addAnimation(animation)
        self.animation_seq.start()

    def count_set_toggle(self):
        ''' Open/close hidden menu "count_set_toggle" '''

        if self.count_set.width()==0:

            self.animations = []
            self.geometry_animate_setup(self.count_set_button_expand,(950, 686, 31, 41),(854, 686, 31, 41))
            self.geometry_animate_setup(self.count_set_button,(981, 686,  0, 41),(950, 686, 31, 41))
            self.geometry_animate_setup(self.count_set,(981, 686,  0, 41),(883, 686, 69, 41))
            self.geometry_animate_start()

            self.count_set_button_expand.setText(">")

        else:

            self.animations = []
            self.geometry_animate_setup(self.count_set_button_expand,(950, 686, 31, 41),(854, 686, 31, 41),reverse=True)
            self.geometry_animate_setup(self.count_set_button,(981, 686,  0, 41),(950, 686, 31, 41),reverse=True)
            self.geometry_animate_setup(self.count_set,(981, 686,  0, 41),(883, 686, 69, 41),reverse=True)
            self.geometry_animate_start()

            self.count_set_button_expand.setText("<")

    def log_toggle(self,value):
        """ Turn on/off actions.updateState data logging to file """
        if value:
            self.log.begin()
        else:
            self.log.stop()

    def livelog_toggle(self):
        """ Open/Close the "live-log" state view pane """
        if self.livelog.width()==0:
            self.animations = []
            self.geometry_animate_setup(self.livelog_freeze_button,(980, 927,  0, 19),(640, 927, 170, 19))
            self.geometry_animate_setup(self.livelog_clear_button,(980, 927,  0, 19),(810, 927, 170, 19))
            self.geometry_animate_setup(self.livelog_expand,(950, 866,  31, 41),(610, 866, 31, 41))
            self.geometry_animate_setup(self.livelog,(980, 842,  0, 85),(640, 842, 341, 85))
            self.geometry_animate_start()
            self.livelog_expand.setText(">")
        else:
            self.livelog_clear()
            self.animations = []
            self.geometry_animate_setup(self.livelog_freeze_button,(980, 927,  0, 19),(640, 927, 170, 19),reverse=True)
            self.geometry_animate_setup(self.livelog_clear_button,(980, 927,  0, 19),(810, 927, 170, 19),reverse=True)
            self.geometry_animate_setup(self.livelog_expand,(950, 866,  31, 41),(610, 866, 31, 41),reverse=True)
            self.geometry_animate_setup(self.livelog,(980, 842,  0, 85),(640, 842, 341, 85),reverse=True)
            self.geometry_animate_start()
            self.livelog_expand.setText("<")

    def livelog_freeze(self,value):
        """ Pause/unpause the live-log stream """
        self.live_log_frozen = int(value)

    def livelog_clear(self):
        """ Clear the live-log pane """
        self.livelog.clear()

    def f1_toggle(self, independently_animated=True,  force_activate=False, force_deactivate=False):
        ''' Trigger the F1 button state '''

        if independently_animated:
            self.animations = []

        if (self.f1.width()==0 or force_activate) and not force_deactivate:
            self.geometry_animate_setup(self.f1,(980, 585, 0, 41),(870, 585, 111, 41))
            self.geometry_animate_start()
            self.u2_2.setVisible(1)
            self.u2_f1.setVisible(1)
            self.f1_u2.setVisible(1)
            self.f1_v2.setVisible(1)

            self.f1_button.setChecked(1)

             # line keys are dynamic, so we need to search for ours
            linekey = self.look_for_linekey('u2','f1')
            [line.setVisible(1) for line in self.lines[linekey]]

            linekey = self.look_for_linekey('v2','f1')
            [line.setVisible(1) for line in self.lines[linekey]]
        else:
            self.geometry_animate_setup(self.f1,(980, 585, 0, 41),(870, 585, 111, 41),reverse=True)
            self.geometry_animate_start()
            self.u2_2.setVisible(0)
            self.u2_f1.setVisible(0)
            self.f1_u2.setVisible(0)
            self.f1_v2.setVisible(0)

            self.f1_button.setChecked(0)

            linekey = self.look_for_linekey('u2','f1')
            [line.setVisible(0) for line in self.lines[linekey]]

            linekey = self.look_for_linekey('v2','f1')
            [line.setVisible(0) for line in self.lines[linekey]]

    def f2_toggle(self, independently_animated=True, force_activate=False, force_deactivate=False):
        ''' Trigger the F2 button state '''

        if independently_animated:
            self.animations = []

        if (self.f2.width()==0 or force_activate) and not force_deactivate:
            self.geometry_animate_setup(self.f2,(980, 625, 0, 41),(870, 625, 111, 41))
            self.geometry_animate_start()

            self.f2_button.setChecked(1)

        else:
            self.geometry_animate_setup(self.f2,(980, 625, 0, 41),(870, 625, 111, 41),reverse=True)
            self.geometry_animate_start()

            self.f2_button.setChecked(0)

    def f1_trigger(self,value,no_toggle=False):
        """ Fire Suppression 1 Trigger """
        self.Command['F1']=int(value)

    def f2_trigger(self,value,no_toggle=False):
        """ Fire Suppression 1 Trigger """
        self.Command['F2']=int(value)

    def fire_trigger(self,value):
        ''' Master Fire Suppression Trigger'''
        self.Command['F1']=int(value)
        self.Command['F2']=int(value)

    def b1_trigger(self,value):
        """ Electrical Bus 1 Relay Trigger """
        if value:
            self.Command['B1'] = 1
            self.Command['B2'] = 1
            self.b2_toggle.setChecked(1)
        else:
            self.Command['B1'] = 0
            self.Command['B2'] = 0
            self.b2_toggle.setChecked(0)

    def b2_trigger(self,value):
        """ Electrical Bus 2 Relay Trigger """
        if value:
            self.Command['B1'] = 1
            self.Command['B2'] = 1
            self.b1_toggle.setChecked(1)
        else:
            self.Command['B1'] = 0
            self.Command['B2'] = 0
            self.b1_toggle.setChecked(0)

    def stop_toggle(self,state):
        """ Stop button call """
        self.Command['E'] = int(state) # bool -> int

    def arm_toggle(self,state):
        """ Arm button call """
        self.Command['a'] = int(state) # bool -> int

    def count_toggle(self,state):
        """ Count button call """
        self.Command['Cm'] = int(state)

    def reset_warning(self):
        self.Alarms['warning'] = []

    def reset_caution(self):
        self.Alarms['caution'] = []

    def count_set_command(self):
        """ Take count setting value and command count mode 2 (SET)"""
        decimal_count_set   = - self.count_set.value()
        self.Command['c1']  = int(math.modf(decimal_count_set)[1])
        self.Command['c1_'] = int(math.modf(decimal_count_set)[0]*1000)
        self.Command['c2']  = int(math.modf(decimal_count_set)[1])
        self.Command['c2_'] = int(math.modf(decimal_count_set)[0]*1000)
        self.Command['Cm']  = 2

    def closeSpecificPlot(self,plot):
        plot.remove()
        self.scene.removeItem(plot)
        self.plots.remove(plot)
        del plot

    def closeEvent(self,event):
        actions.closePlots(self)

def main():
    app = QtWidgets.QApplication(sys.argv)
    gui  = Interface()
    gui.show()
    app.exec_()

if __name__=='__main__':
    main()
