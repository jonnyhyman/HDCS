# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'refdefwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(555, 273)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.502975, y1:0, x2:0.473, y2:1, stop:0 rgba(2, 11, 16, 255), stop:1 rgba(4, 26, 37, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.regProfileView = GraphicsLayoutWidget(self.centralwidget)
        self.regProfileView.setMinimumSize(QtCore.QSize(0, 0))
        self.regProfileView.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.regProfileView.setStyleSheet("color: white;\n"
"border: 1px solid #4589b2;")
        self.regProfileView.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.regProfileView.setFrameShadow(QtWidgets.QFrame.Plain)
        self.regProfileView.setLineWidth(0)
        self.regProfileView.setMidLineWidth(0)
        self.regProfileView.setObjectName("regProfileView")
        self.horizontalLayout.addWidget(self.regProfileView)
        self.widget_5 = QtWidgets.QWidget(self.centralwidget)
        self.widget_5.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_5.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widget_5.setStyleSheet("background: transparent;")
        self.widget_5.setObjectName("widget_5")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.widget_5)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_16 = QtWidgets.QLabel(self.widget_5)
        font = QtGui.QFont()
        font.setFamily("Futura BQ")
        font.setPointSize(11)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("color: white;background-color: transparent;")
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.gridLayout_7.addWidget(self.label_16, 0, 1, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.widget_5)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(9)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("color: white;\n"
"background: rgba(255,255,255,.2);\n"
"padding: 5px;")
        self.textEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_7.addWidget(self.textEdit, 2, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.set = QtWidgets.QPushButton(self.widget_5)
        font = QtGui.QFont()
        font.setFamily("Futura BQ")
        font.setPointSize(9)
        self.set.setFont(font)
        self.set.setStyleSheet("QPushButton{\n"
"    color: white;\n"
"    background-color: transparent;\n"
"    border: 1px solid #4589b2;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"    background-color: rgba(255,255,255,.2);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"    border: 1px solid #00ce35;\n"
"    background-color: rgba(0,0,0,.3);\n"
"}")
        self.set.setObjectName("set")
        self.horizontalLayout_2.addWidget(self.set)
        self.syntaxState = QtWidgets.QLabel(self.widget_5)
        self.syntaxState.setMaximumSize(QtCore.QSize(30, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.syntaxState.setFont(font)
        self.syntaxState.setStyleSheet("background-color: #00ce35;\n"
"border-radius: 15px;")
        self.syntaxState.setText("")
        self.syntaxState.setAlignment(QtCore.Qt.AlignCenter)
        self.syntaxState.setObjectName("syntaxState")
        self.horizontalLayout_2.addWidget(self.syntaxState)
        self.gridLayout_7.addLayout(self.horizontalLayout_2, 4, 1, 1, 1)
        self.horizontalLayout.addWidget(self.widget_5)
        self.gridLayout_16.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Test Definition Dialog"))
        self.label_16.setText(_translate("MainWindow", "REGULATOR SCRIPT"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Courier New\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">import math</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">end=5</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; color:#ffffff;\">if t &gt;= 0 and t&lt;end:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; color:#ffffff;\">    return math.exp(-t)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; color:#ffffff;\">if t &gt;= 5:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; color:#ffffff;\">    return 0</span></p></body></html>"))
        self.set.setText(_translate("MainWindow", "SET"))

from pyqtgraph import GraphicsLayoutWidget

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

