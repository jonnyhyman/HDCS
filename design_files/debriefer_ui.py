# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'debriefer_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(944, 590)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("graphics/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.502975, y1:0, x2:0.473, y2:1, stop:0 rgba(2, 11, 16, 255), stop:1 rgba(4, 26, 37, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.graphicsView = GraphicsLayoutWidget(self.centralwidget)
        self.graphicsView.setStyleSheet("background-color:rgb(230, 230, 230);\n"
"color: white;\n"
"border: 1px solid white;")
        self.graphicsView.setObjectName("graphicsView")
        self.horizontalLayout.addWidget(self.graphicsView)
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(8)
        self.tableView.setFont(font)
        self.tableView.setStyleSheet("QAbstractItemView{    \n"
"    background: #C7CCC5;\n"
"}\n"
"QAbstractItemView::QScrollBar:vertical {              \n"
"    border: 1px solid #999999;\n"
"    background:white;\n"
"    width:10px;    \n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"QAbstractItemView::QScrollBar::handle:vertical {\n"
"    background: #4589b2;\n"
"    min-height: 0px;\n"
"}\n"
"QAbstractItemView::QScrollBar::add-line:vertical {\n"
"    background: #4589b2;\n"
"    height: 0px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QAbstractItemView::QScrollBar::sub-line:vertical {\n"
"    background: #4589b2;\n"
"    height: 0 px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}")
        self.tableView.setGridStyle(QtCore.Qt.NoPen)
        self.tableView.setObjectName("tableView")
        self.tableView.horizontalHeader().setDefaultSectionSize(49)
        self.tableView.verticalHeader().setDefaultSectionSize(30)
        self.horizontalLayout.addWidget(self.tableView)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Debriefer"))

from pyqtgraph import GraphicsLayoutWidget

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

