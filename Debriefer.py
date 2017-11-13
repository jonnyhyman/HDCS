import sys
import importlib
import numpy as np
import pandas as pd
from random import randint
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from pyqtgraph.Qt import QtGui, QtCore
import pyqtgraph as pg

import Debriefer_UI as design
from Definitions import State

class TableModel(QAbstractTableModel):
    def __init__(self, datain, headerdata, parent=None):
        """
        Args:
            datain: a list of lists
            headerdata: a list of strings
        """
        QAbstractTableModel.__init__(self, parent)
        self.arraydata = datain
        self.headerdata = headerdata

    def rowCount(self, parent):
        return len(self.arraydata)

    def columnCount(self, parent):
        if len(self.arraydata) > 0:
            return len(self.arraydata[0])
        return 0

    def data(self, index, role):
        if not index.isValid():
            return QVariant()
        elif role != Qt.DisplayRole:
            return QVariant()
        return QVariant(self.arraydata[index.row()][index.column()])

    def setData(self, index, value, role):
        pass         # not sure what to put here

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return QVariant(self.headerdata[col])
        return QVariant()


class Debriefer(QtWidgets.QMainWindow,design.Ui_MainWindow):
    def __init__(self,parent=None):
        """ Initialize the GUI's interface """
        super(self.__class__, self).__init__()
        self.setupUi(self)

        self.keys_to_plot = ['C1','C2','A','B','I','R',
                             'v1','v2','i1','i2',
                             'zf','z0','z1','z2',
                             'Fa1','Fa2',
                             'm0','p0','p1','t0','t1','t2',
                             'u1','u2','u3','u4']

        if self.openFile_window():  # force select at startup
            self.make_tableView()
            self.make_graphicsView()
            self.show()

    def openFile_window(self):
        """ open file selection window """
        self.defname = QtGui.QFileDialog.getOpenFileName(self,'Open Definition File',
                                                       filter='*.py',
                                                       directory='./logs/')[0]

        if self.defname != '':

            self.defname = self.defname[self.defname.rindex('/')+1:self.defname.rindex('.py')]
            self.deffile = importlib.import_module('logs.' + self.defname)

            self.logname = ['./logs/',self.defname.replace('def','log'),'.csv']
            self.logname = ''.join(self.logname)

            try:
                self.build_dataframe()
            except FileNotFoundError:
                return 0

            return 1
        else:
            return 0

    def build_dataframe(self):
        """ build the dataframe used for graphicsview and tableview """

        # get the indices between T-1 and T+end+1

        frst_test_time = self.deffile.TestMatrix[1][0]  - 1
        last_test_time = self.deffile.TestMatrix[-1][0] + 1

        self.dataframe = pd.read_csv(self.logname)[self.keys_to_plot]

        # filter dataframe by start and end times

        relevant_indices = [list(np.where(self.dataframe["C1"] >= frst_test_time))]
        relevant_indices+= [list(np.where(self.dataframe["C1"] <= last_test_time))]
        relevant_indices = np.intersect1d(relevant_indices[0],relevant_indices[1])

        self.dataframe = self.dataframe.iloc[relevant_indices]

        return True

    def make_tableView(self):
        """ draw the table view """

        self.data_frame_plot = self.dataframe
        self.data_array = self.dataframe.as_matrix().tolist()
        self.header     = self.dataframe.columns.tolist()

        self.tablemodel = TableModel(self.data_array,self.header,self)
        self.tableView.setModel(self.tablemodel)

        self.tableView.selectionModel().selectionChanged.connect(self.selected_columns)

    def make_graphicsView(self):
        """ draw the graphics view """


        self.data_array_plot = self.data_frame_plot.as_matrix().tolist()
        self.header_plot     = self.data_frame_plot.columns.tolist()

        rows = len(self.data_array_plot)
        columns = len(self.data_array_plot[0])

        self.graphicsView.clear()

        self.plotView = self.graphicsView.addPlot()
        pg.setConfigOptions(antialias=True)
        self.plotView.addLegend()

        self.lines, n, cn = [], 0, 0
        for c in range(columns):

            color = (randint(0,255),randint(0,255),randint(0,255))

            if all(color) == 0:
                color = (255,0,0)

            (self.plotView.plot(pen=color,name=self.header_plot[c])
            ).setData([n for n in range(rows)],
                      [float(self.data_array_plot[r][c]) for r in range(rows)])

            n+=1
            cn+=1

    def selected_columns(self, selected, deselected):
        """ figure out which columns to filter the graph by """

        selection = self.tableView.selectedIndexes()

        self.selected = []

        for n in [item.column() for item in selection]:
            if self.header[n] not in self.selected:
                self.selected.append(self.header[n])

        self.data_frame_plot = self.dataframe[self.selected]

        self.make_graphicsView()


def main():
    app = QtWidgets.QApplication(sys.argv)
    gui  = Debriefer()
    gui.show()
    app.exec_()

if __name__=='__main__':
    main()
