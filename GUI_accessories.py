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
from multiprocessing import Process

import GUI_reset  as reset
import GUI_dialog as dialog
import GUI_upload as upload

from pygame import mixer

class Dialog(QtWidgets.QDialog,dialog.Ui_Dialog):
    def __init__(self,reason,function):
        """ This class creates an error dialog with a reason and origin func """
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.button.accepted.connect(self.closed)
        error_message=("An error occured due to "+reason+" in the "+function+" call")
        self.label.setText(error_message)
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)
        self.show()

    def open(self):
        """ Open window, stay on top! """
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)
        self.show()

    def closed(self):
        self.close()

class Upload(QtWidgets.QDialog,upload.Ui_Dialog):
    def __init__(self,cmd):
        """ This class provides the upload window and control to trigger
            Microuploads on ADCS
        """

        super(self.__class__, self).__init__()
        self.setupUi(self)

        self.movie = QtGui.QMovie("./graphics/uploading_bg.gif")
        self.loadlabel_stars.setMovie(self.movie)
        self.movie.start()
        self.UP.clicked.connect(self.upload)

        self.setWindowFlags(self.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)
        self.show()
        self.cmd = cmd

    def checkyoself(self):
        """ Determine who is checked/not checked """
        who = {}
        whos_who = {self.U1:'Micro1',self.U2:'Micro2',self.U3:'Micro3',self.U4:'Micro4'}
        for obj,progname in whos_who.items():
            if obj.isChecked():
                who[progname]=1
            else:
                who[progname]=0
        return who

    def upload(self):
        """ Actuate the uploads """
        micros=[]
        for key,value in self.checkyoself().items():
            if value==1:
                micros.append(key)

        send=''
        for m in micros:
            send += m
            send += '&'

        # Queue for upload at next ADCS iteration
        self.cmd['UC'] = send
        self.close()

class Reset(QtWidgets.QDialog,reset.Ui_Dialog):
    def __init__(self,gui):
        """ This class allows for resetting of the Micros. A critical task
            to retare sensors and reset buffers of devices on the 5V bus
        """
        super(self.__class__, self).__init__()
        self.setupUi(self)

        self.gui = gui
        self.movie = QtGui.QMovie("./graphics/uploading_bg.gif")
        self.loadlabel_stars.setMovie(self.movie)
        self.movie.start()
        self.GO.clicked.connect(self.reset)

        self.setWindowFlags(self.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)
        self.show()

    def reset(self):
        """ Actuate the reset, signalled by self.GO button click"""

        resetADCS   = self.ADCS.isChecked()
        resetMICROS = self.Micros.isChecked()
        stopADCS    = self.ADCS_STOP.isChecked()

        if resetADCS:
            self.gui.Command['RS'] = 'ADCS'
        elif not resetADCS and resetMICROS:
            self.gui.Command['RS'] = 'MICRO'

        if stopADCS:
            self.gui.Command['RS'] = 'ADCS_OFF'

        self.close()

class Sound(object):

    def __init__(self):
        self.chs = {'warning':0,
                    'caution':1,
                    'silence':2}

        mixer.init(channels=len(self.chs))

    def play(self,selection):
        s = mixer.Sound('./sounds/'+selection+'.wav')
        mixer.Channel(self.chs[selection]).play(s)
