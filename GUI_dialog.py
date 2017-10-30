# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        Dialog.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("graphics/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStatusTip("")
        Dialog.setStyleSheet("background: qlineargradient(spread:pad, x1:0.502975, y1:0, x2:0.473, y2:1, stop:0 rgba(2, 11, 16, 255), stop:1 rgba(4, 26, 37, 255));")
        self.button = QtWidgets.QDialogButtonBox(Dialog)
        self.button.setGeometry(QtCore.QRect(-2, 250, 403, 31))
        self.button.setStyleSheet("QPushButton{\n"
"    color: white;\n"
"    background-color: transparent;\n"
"    border: 1px solid #4589b2;\n"
"    padding: 5px;\n"
"    padding-left: 45px;\n"
"    padding-right: 45px;\n"
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
        self.button.setOrientation(QtCore.Qt.Horizontal)
        self.button.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.button.setCenterButtons(True)
        self.button.setObjectName("button")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(36, 92, 331, 151))
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setStyleSheet("color:white;\n"
"background:transparent;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(0, 22, 399, 53))
        font = QtGui.QFont()
        font.setFamily("HUN-din 1451")
        font.setPointSize(28)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: #4A94C0;\n"
"background:transparent;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(-2, 84, 407, 4))
        self.line.setStyleSheet("border: 1px solid #4589b2;\n"
"background-color: transparent;")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.retranslateUi(Dialog)
        self.button.accepted.connect(Dialog.accept)
        self.button.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Oops!"))
        self.label.setText(_translate("Dialog", "Something went wrong within the turbo encabulator.\n"
" \n"
" Check the non-reversible cardinal grammeter tremie pipe."))
        self.label_2.setText(_translate("Dialog", "ERROR"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

