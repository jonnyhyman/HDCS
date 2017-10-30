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

from time import time
from ADCS_Link import ADCS_Link
from PyQt5 import QtCore

class Thread(QtCore.QThread):

    compare       = ['F1','F2']
    state_emitter = QtCore.pyqtSignal(dict)
    ADCS          = ADCS_Link()
    lasttime=time()

    def get_gui(self,gui):
        """ Obtain a link to the GUI object for the command variable """
        self.GUI = gui

    def run(self):
        """ Operate the state thread: check for changes, emit if there are """

        INIT = True
        while True:

            new_state = self.ADCS.tranceive_and_parse(self.GUI.Command,
                                                      self.GUI.State)

            if new_state:

                self.compare = [key for key,value in new_state.items()
                               if new_state[key]!=self.GUI.State[key]]

                # Can't do new_state!=State b/c ADCS doesn't have the same keys
                if len(self.compare) or INIT:
                    self.state_emitter.emit(new_state)
                    INIT = 0

                self.lasttime=time()
