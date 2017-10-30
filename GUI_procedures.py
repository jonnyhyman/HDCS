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

from PyQt5 import QtCore, QtWidgets, QtWidgets, QtGui
import Procedure_specification as spec
from GUI_actions import changeCSS
import GUI_colors as colors
import importlib

import time

class ProceduresWidget(QtWidgets.QTreeWidget):
    def __init__(self,parent=None,gui=None):
        super(self.__class__, self).__init__(parent)
        self.gui=gui
        self.autoFillBackground()
        self.setStyleSheet('''color: white; border: 0px solid transparent;''')
        self.setGeometry(QtCore.QRect(10, 15, 260, 340))
        self.setHeaderHidden(1)
        self.setItemsExpandable(0)
        self.setRootIsDecorated(0)
        self.setVerticalScrollBarPolicy( QtCore.Qt.ScrollBarAlwaysOff )

        self.gui.proc_grad_top.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents)
        self.gui.proc_grad_bot.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents)

        self.make_procedure(0.00)

        self.itemClicked.connect(self.setItemCheckState)
        self.gui.proc_set.valueChanged.connect(self.make_procedure)

    def make_procedure(self,proc_no):
        ''' Populate the procedure with given number identifier '''
        self.clear()
        self.current_proc_num = proc_no
        changeCSS(self.gui.proc_set,self.gui.proc_set.styleSheet(), # reset
                  'border','1px solid '+colors.active_blue)
        self.line_check = [] # line objects + their associated software check(s)
        self.steps,self.substeps = [],[]
        try:
            proc = spec.Procedures[proc_no]
        except KeyError:
            # if we tried navigating to a non-existing procedure
            # shake the procedure number spin-box to indicate error
            self.gui.shake_animate(self.gui.proc_set)
            return

        for step in proc:

            if len(step) == 1: # if no referenced states to check for
                #print(step[0])
                # check kind (step/substep/note) and check text
                kind,text = tuple(step[0].split(':'))

                if 'Stp' in kind: # step == 'stp'
                    self.steps += [self.new(text)]

                elif 'Sub' in kind: # substep with last step as parent
                    self.substeps += [self.new(text,
                                        substep=self.steps[len(self.steps)-1])]

                elif 'Nte' in kind: # note with last step as parent
                    if len(self.steps)>0:
                        self.substeps += [self.new(text,
                                            substep=self.steps[len(self.steps)-1],
                                            note=True)]
                    else:
                        self.substeps += [self.new(text,note=True)]
            else:
                checks = []
                check_evals = []
                for check_eval in step:
                    if 'Stp' in check_eval or 'Sub' in check_eval:
                        continue
                    else:
                        # check kind (step/substep/note) and check text
                        kind,text   = tuple(step[0].split(':'))
                        check       = int(eval(check_eval))
                        checks     += [ check ]
                        check_evals+= [ check_eval ]

                check_state = all(checks)
                if check_state==1:
                    check_state==2 # make into a "legit" checkmark (not square)

                if 'Stp' in kind:  # step == 'stp'
                    line = self.new(text,check=check_state)
                    self.steps += [line]

                elif 'Sub' in kind: # substep with last step as parent
                    line = self.new(text,substep=self.steps[-1],check=check_state)
                    self.substeps += [line]

                self.line_check.append( (line,check_evals) )

    def next_procedure(self):
        ''' Populate the procedure with the next one in line '''
        try:
            importlib.reload(spec)
        except:
            pass

        proc_nums = sorted(spec.Procedures.keys())
        next_num  = proc_nums.index(self.current_proc_num)+1
        if next_num < len(proc_nums):
            self.make_procedure(proc_nums[next_num])
            self.gui.proc_set.setValue(proc_nums[next_num])
        else:
            self.gui.shake_animate(self.gui.proc_next_button)

    def new(self,text,substep=False,note=False,check=0):
        ''' Create a new checklist line item '''
        font = QtGui.QFont()
        font.setFamily("GOST Common")
        font.setPointSize(9)

        if substep:
            line = QtWidgets.QTreeWidgetItem(substep)
            self.expandItem(substep)
        else:
            line = QtWidgets.QTreeWidgetItem(self)

        line.setFont(0,font)
        line.setText(0,text)
        if not note:
            line.setFlags(QtCore.Qt.ItemIsUserCheckable)
            line.setFlags(QtCore.Qt.ItemIsEnabled)
            line.setCheckState(0,check) # column, state
            brush = QtGui.QBrush()
            brush.setColor(QtGui.QColor(colors.white))
            line.setForeground(0,brush)
        else:
            line.setText(0,"Note: "+text)
            brush = QtGui.QBrush()
            brush.setColor(QtGui.QColor(colors.active_blue))
            line.setForeground(0,brush)

        return line

    def autoChecks(self):
        """ Do an auto check of all checklist items, if they have a
            software-defined procedure tied to it """

        column = 0

        for line_check_evals in self.line_check:
            line,check_evals = line_check_evals
            checks = []
            for check in check_evals:
                checks += [int(eval(check))]
            if all(checks):
                line.setCheckState(column,2)
            else:
                line.setCheckState(column,0)

        # If all items in a procedure are complete, inicate it by changing
        # the color of the proc_set window
        check_states = []
        for step in self.steps:
            check_states.append(step.checkState(column))

        if all(check_states):
            changeCSS(self.gui.proc_set,self.gui.proc_set.styleSheet(),
                      'border','1px solid '+colors.active_green)
        else:
            changeCSS(self.gui.proc_set,self.gui.proc_set.styleSheet(),
                      'border','1px solid '+colors.active_blue)

    def setItemCheckState(self,item,column):
        ''' Set the checklist item check state '''
        # Don't allow for notes:
        if 'Note:' not in item.text(column):
            if item.checkState(column):
                item.setCheckState(column,0)
                # Set color, too
                brush = QtGui.QBrush()
                brush.setColor(QtGui.QColor(colors.white))
                item.setForeground(column,brush)
            else:
                if item.childCount()==0:
                    item.setCheckState(column,2)
                    brush = QtGui.QBrush()
                    brush.setColor(QtGui.QColor(colors.disabled))
                    item.setForeground(column,brush)
                else:
                    checked=[]
                    for i in range(item.childCount()):
                        if "Note:" not in item.child(i).text(column):
                            checked.append( (item.child(i)).checkState(column) )
                    if all(checked):
                        item.setCheckState(column,2)
                        # Set color, too
                        brush = QtGui.QBrush()
                        brush.setColor(QtGui.QColor(colors.disabled))
                        item.setForeground(column,brush)
                    else:
                        item.setCheckState(column,1)
                        # Set color, too
                        brush = QtGui.QBrush()
                        brush.setColor(QtGui.QColor(colors.disabled_lite))
                        item.setForeground(column,brush)

        self.scrollToItem(item, QtWidgets.QAbstractItemView.PositionAtCenter )

        self.autoChecks()

def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    gui  = Procedures()
    gui.show()
    app.exec_()

if __name__ == '__main__':
    main()
