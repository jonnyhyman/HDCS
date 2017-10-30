"""
    This file is part of HDCS.

    HDCS is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    HDCS is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with HDCS.  If not, see <http://www.gnu.org/licenses/>.
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph.Qt import QtGui, QtCore
import pyqtgraph as pg

from Log_state import def_logging
import GUI_test_reg as reg
import GUI_test as test
import GUI_colors as colors
import GUI_actions as actions
from GUI_animate import shake_animate
from GUI_accessories import Dialog

import numpy as np
import math

import importlib
import py_compile as pyc
import os

from socket import *
from time import time

"""-----------------------------------------------------------------------------

  This pillar of code is important to define the
  parameters over time during a test.

  Some variables are 1/0 integers, while others are variable (0<->1) floats.

  Max float precision is double, because we have to upload to ADCS & Micros with
  integer values.
   -----------------------------------------------------------------------------
"""

class TestDefinition(QtWidgets.QMainWindow,test.Ui_MainWindow):
    def __init__(self):
        """ This class operates the test definition window, and initiates
            test matrix specification upload to ADCS """

        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.Definition = {
            'tminus'  :0,
            'I_del'   :0.0,
            'I_dur'   :0.0,
            'A_del'   :0.0,
            'A_dur'   :0.0,
            'B_del'   :0.0,
            'B_dur'   :0.0,
            'R_pos'   :lambda x: x,
            'R_dur'   :0.0,
        }

        self.TestMatrix = convertDefToMatrix(self.Definition)

        self.uploadButton.clicked.connect(self.save)
        self.cancelButton.clicked.connect(self.cancel)

        self.plotView = self.testProfileView.addPlot(title='''Test Profile''')
        pg.setConfigOptions(antialias=True)
        self.I_line = self.plotView.plot(pen=colors.electricity,name='ignition')
        self.A_line = self.plotView.plot(pen=colors.active_blue,name='relay A')
        self.B_line = self.plotView.plot(pen=colors.sensorok,name='relay B')
        self.R_line = self.plotView.plot(pen=colors.control,name='relay R')

        self.tminus.setValue(self.Definition['tminus'])
        self.I_del.setValue(self.Definition['I_del'])
        self.I_dur.setValue(self.Definition['I_dur'])
        self.A_del.setValue(self.Definition['A_del'])
        self.A_dur.setValue(self.Definition['A_dur'])
        self.B_del.setValue(self.Definition['B_del'])
        self.B_dur.setValue(self.Definition['B_dur'])
        self.refreshPlot(self.Definition)

        self.regulatorSetup.clicked.connect(self.regSetup)
        self.openFile.setShortcut('Ctrl+o')
        self.openFile.triggered.connect(self.openFile_window)
        self.connect_things()

    def connect_things(self):
        """ Make the multitude of signal/slot connections """
        self.tminus.valueChanged.connect(lambda value:self.updDef(value,'tminus'))
        self.A_del.valueChanged.connect(lambda value: self.updDef(value,'A_del'))
        self.A_dur.valueChanged.connect(lambda value: self.updDef(value,'A_dur'))
        self.B_del.valueChanged.connect(lambda value: self.updDef(value,'B_del'))
        self.B_dur.valueChanged.connect(lambda value: self.updDef(value,'B_dur'))
        self.I_del.valueChanged.connect(lambda value: self.updDef(value,'I_del'))
        self.I_dur.valueChanged.connect(lambda value: self.updDef(value,'I_dur'))
        self.R_dur.valueChanged.connect(lambda value: self.updDef(value,'R_dur'))

        self.A_del_slide.valueChanged.connect(lambda x: self.A_del.setValue(x/10))
        self.A_dur_slide.valueChanged.connect(lambda x: self.A_dur.setValue(x/10))
        self.B_del_slide.valueChanged.connect(lambda x: self.B_del.setValue(x/10))
        self.B_dur_slide.valueChanged.connect(lambda x: self.B_dur.setValue(x/10))
        self.I_del_slide.valueChanged.connect(lambda x: self.I_del.setValue(x/10))
        self.I_dur_slide.valueChanged.connect(lambda x: self.I_dur.setValue(x/10))
        self.R_dur_slide.valueChanged.connect(lambda x: self.R_dur.setValue(x/10))

    def openFile_window(self):
        """ Sets all values in the window to the chosen save file """

        name = QtGui.QFileDialog.getOpenFileName(self,'Open Python File',
                                                       filter='*.py',
                                                       directory='./logs/')
        name = name[0]
        name = name[name.rindex('/')+1:name.rindex('.py')]

        try:
            self.saveFile = importlib.import_module('logs.' + name)

            for key,value in self.saveFile.TestParams.items():
                if key != 'R_pos':
                    getattr(self,key).setValue(value)

            self.testNotes.setPlainText( self.saveFile.TestNotes )

            with open('./logs/'+name+'.py','r') as savedFunc:

                function = savedFunc.read()
                function = function[function.rindex('def'):]
                with open('RegulatorScript.py','w') as rewriteF:
                    rewriteF.write(function)

            try:
                self.regulatorChanged()
            except AttributeError:
                self.regSetup()

        except Exception as e:
            self.d = Dialog(reason='file ./logs/'+name+'.py import error '+str(e),
                            function='openFile_window')

    def regSetup(self):
        """ Initialize the RegulatorSetup class & open the window """
        self.regSet = RegulatorSetup(endT=self.Definition['R_dur'])
        self.regSet.set.clicked.connect(self.regulatorChanged)

    def regulatorChanged(self):
        """ Handler for regulator SET event, displays and saves final values """
        if self.regSet.finalize():

            import RegulatorScript
            self.Definition['R_dur'] = self.regSet.endT
            self.Definition['R_pos'] = RegulatorScript.Regulator

            self.regSet.close()
            self.refreshPlot(self.Definition)

    def updDef(self,value,obj):
        """ Update the self.Definition master variable and all the GUI sliders """

        self.Definition[obj]=value
        self.refreshPlot(self.Definition)

        # update sliders to match double spin boxes
        try:
            slider = getattr(self,obj+'_slide')
            slider.setValue(value*10)
        except AttributeError: # some values don't have sliders
            pass

    def refreshPlot(self,definition):
        """ Update the test definition plot """
        try:
            mat = convertDefToMatrix(definition)
        except TypeError as e:
            self.d = Dialog(reason='regulator function not being defined',
                            function='TestDefinition.save')
            return

        ts, Is,As,Bs,Rs = [],[],[],[],[]
        for n in range(len(mat)):
            if n>0:
                ts.append(mat[n][0]+mat[n][1]/1000-0.001) # For vertical lines,
                Is.append(mat[n-1][2])                     # instead of slopes
                As.append(mat[n-1][3])
                Bs.append(mat[n-1][4])
                Rs.append(mat[n-1][5]/100) # keep in range
            ts.append(mat[n][0]+mat[n][1]/1000)
            Is.append(mat[n][2])
            As.append(mat[n][3])
            Bs.append(mat[n][4])
            Rs.append(mat[n][5]/100) # keep in range

        self.I_line.setData(ts,Is)
        self.A_line.setData(ts,As)
        self.B_line.setData(ts,Bs)
        self.R_line.setData(ts,Rs) # values between 0<->1

    def open(self):
        self.show()

    def save(self):
        self.TestMatrix = convertDefToMatrix(self.Definition)
        if len(self.TestMatrix)<42:
            self.TestNotes = self.testNotes.toPlainText()

            def_logging(convertDefToMatrix(self.Definition),self.Definition,self.TestNotes)
            self.close()

        else:

            self.d = Dialog(reason='test matrix length '+str(len(self.TestMatrix))+
                                    ' exceeding 42',
                            function='TestDefinition.save')

            self.TestMatrix=None # prevent from uploading and overloading

    def cancel(self):
        self.close()

class RegulatorSetup(QtWidgets.QMainWindow,reg.Ui_MainWindow):
    def __init__(self,endT=1):
        """ This class operates the regulator setup window, allowing for Python
            defined regulator control
        """
        super(self.__class__, self).__init__()
        self.setupUi(self)

        last_script_text = open('RegulatorScript.py','r').read()
        last_script_text = last_script_text[last_script_text.index(':')+1:]

        # set text to function header-less version
        self.textEdit.setPlainText(last_script_text)

        self.endT = endT
        self.textEdit.setTabStopWidth(18)
        self.textEdit.textChanged.connect(self.updatedScript)
        self.textEdit.cursorPositionChanged.connect(self.cursor)

        self.plotView = self.regProfileView.addPlot(title='''Regulator Profile''')
        pg.setConfigOptions(antialias=True)
        self.Rplot = self.plotView.plot(pen=colors.electricity,name='Regulator')
        self.updatedScript()

        self.show()

    def updatedScript(self):
        """ Occurs any time text is changed, writes QTextEdit contents to a
            Python file, compiles it to check Syntax, then executes it to plot
        """

        first = 'def Regulator(t):\n\n'
        text  = '\t'
        text += self.textEdit.toPlainText()

        snam = 'RegulatorScript.py'
        try:
            os.remove(snam)
        except FileNotFoundError:
            pass

        text = text.replace('\n','\n\t')
        text = text.replace('\t','   ')

        save = open(snam,'w')
        save.write(first)
        save.write(text)
        save.close()

        try:
            error = pyc.compile(snam,doraise=True)

            actions.changeCSS(self.syntaxState,self.syntaxState.styleSheet(),
                        'color',colors.active_green)

            self.updatePlot() # can error out if not returning quite right

            return True

        except Exception as e:

            actions.changeCSS(self.syntaxState,self.syntaxState.styleSheet(),
                        'color',colors.critical)

            return False

    def updatePlot(self):
        """ Reloads the RegulatorScript python, executes, and plots if possible """

        import RegulatorScript
        importlib.reload(RegulatorScript)

        ts = np.arange(0,self.endT,0.001)
        xs = []

        for t in ts:
            val = RegulatorScript.Regulator(t)
            if val is None:
                val=0
            xs.append(val)

        xs = np.array(xs)
        typ = [type(item)==np.int32 or type(item)==np.float32
            or type(item)==np.int64 or type(item)==np.float64 for item in xs]
        if all(typ):
            self.Rplot.setData(ts,xs)
        else:
            raise('Not all regulator values have a numerical type')

    def finalize(self):
        if self.updatedScript():
            return True
        else:
            shake_animate(self,self.set)

def convertDefToMatrix(d):
    """ Converts the definition values (durations, delays, etc...) into a
        time indexed matrix of control values """

    ''' test matrix, given d=Definition has the following form:
        [  (Time of Event SEC,  Time of Event MSEC  ,    Actuator Positions ),
           (Time of Event    ,  Time of Event MSEC  ,    Actuator Positions ),
                ...                     ...                     ...            ]

        it always starts at T=tminus
    '''
    Commands = [0,0,0,0] #I,A,B,R
    Stepped  = [0,1,2] # Actuator cmd indices which are step functions (on/off)
    Variable = {3:'R_pos'}     # Actuator cmd indices which are variable in their amount

    t        = -d['tminus']

    '''
        absolute means w.r.t. T=0
            Istart,Iend = absolute
            Astart = relative to I, Aend = absolute
            Bstart,Bend = relative to A
            Rstart = 0 , Rend = relative to A
    '''
                        #------------- Determine start/end times

    I_se = [ d['I_del']         , d['I_del']+d['I_dur'] ]
    A_se = [ d['A_del']+I_se[0] ,(d['A_del']+I_se[0])+d['A_dur'] ]
    B_se = [ d['B_del']+A_se[0] ,(d['B_del']+A_se[0])+d['B_dur'] ]
    R_se = [ 0                  , d['R_dur']   ]

    Times=[I_se,A_se,B_se,R_se]
    endT=0              #-------------- Find the highest end time
    if I_se[1]>endT:
        endT = I_se[1]
    if A_se[1]>endT:
        endT = A_se[1]
    if B_se[1]>endT:
        endT = B_se[1]
    if R_se[1]>endT:
        endT = R_se[1]
                        #------------- Go through all time steps
                        #------------- Append to matrix if a change event occured
    matrix=[]
    matrix.append([t,0,Commands[0],Commands[1],Commands[2],Commands[3]])
    while t < endT:
        t+=0.001 # 1ms precision
        for n in range(len(Times)):

            if t >= Times[n][0] and t < Times[n][1] and Commands[n]==0 and n in Stepped:
                Commands[n]=1
            elif t >= Times[n][1] and Commands[n]==1 and n in Stepped:
                Commands[n]=0

            try:
                if (t >= Times[n][0] and t < Times[n][1] and n not in Stepped and
                    d[Variable[n]](t) != Commands[n]):
                    Commands[n]=d[Variable[n]](t)
                elif t >= Times[n][1] and n not in Stepped:
                    Commands[n]=0
            except Exception as e:
                print('EXCEPTION >>',e)

        newline = (   [int(math.modf(t)[1]),      # Time in seconds
                       int(math.modf(t)[0]*1000), # Time's milliseconds
                       int(Commands[0]),          # Ignition State        #------------- definition of test matrix here!
                       int(Commands[1]),          # A States
                       int(Commands[2]),          # B State
                       int(Commands[3]*100)])     # R State in percent

        if newline[2:] != matrix[len(matrix)-1][2:]: # if new != last
            matrix.append(newline)

    for row in matrix:
        print(' ',row)
    print('----',len(matrix))
    return matrix

def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    gui  = TestDefinition()
    gui.show()
    app.exec_()

if __name__ == '__main__':
    main()
