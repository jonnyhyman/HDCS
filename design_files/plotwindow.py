# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'plotwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Plot(object):
    def setupUi(self, Plot):
        Plot.setObjectName("Plot")
        Plot.resize(600, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("graphics/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Plot.setWindowIcon(icon)
        Plot.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.502975, y1:0, x2:0.473, y2:1, stop:0 rgba(2, 11, 16, 255), stop:1 rgba(4, 26, 37, 255));")
        self.centralwidget = QtWidgets.QWidget(Plot)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.graphicsView = GraphicsLayoutWidget(self.centralwidget)
        self.graphicsView.setStyleSheet("background-color:rgb(230, 230, 230);\n"
"color: white;\n"
"border: 1px solid white;")
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 0, 0, 1, 1)
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setStyleSheet("QSlider{\n"
"    background-color: transparent;\n"
"} \n"
"QSlider::groove:horizontal {\n"
"     border: 0px solid #999999;\n"
"     height: 8px;\n"
"     background: rgba(78, 96, 131, 50);\n"
"     margin: 2px 0;\n"
" }\n"
"\n"
" QSlider::handle:horizontal {\n"
"     background: #999999;\n"
"     border: 1px solid #5c5c5c;\n"
"     width: 18px;\n"
"     margin: -2px 0;\n"
"     border-radius: 3px;\n"
" }")
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.gridLayout.addWidget(self.horizontalSlider, 1, 0, 1, 1)
        Plot.setCentralWidget(self.centralwidget)

        self.retranslateUi(Plot)
        QtCore.QMetaObject.connectSlotsByName(Plot)

    def retranslateUi(self, Plot):
        _translate = QtCore.QCoreApplication.translate
        Plot.setWindowTitle(_translate("Plot", "Plot"))

from pyqtgraph import GraphicsLayoutWidget

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Plot = QtWidgets.QMainWindow()
    ui = Ui_Plot()
    ui.setupUi(Plot)
    Plot.show()
    sys.exit(app.exec_())

