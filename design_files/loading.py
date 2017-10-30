# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loading.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(400, 300))
        Dialog.setMaximumSize(QtCore.QSize(400, 300))
        Dialog.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("graphics/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStatusTip("")
        Dialog.setStyleSheet("")
        self.standby = QtWidgets.QLabel(Dialog)
        self.standby.setGeometry(QtCore.QRect(30, 100, 331, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(9)
        self.standby.setFont(font)
        self.standby.setStyleSheet("color:white;")
        self.standby.setAlignment(QtCore.Qt.AlignCenter)
        self.standby.setWordWrap(True)
        self.standby.setObjectName("standby")
        self.bg = QtWidgets.QLabel(Dialog)
        self.bg.setGeometry(QtCore.QRect(0, 0, 401, 301))
        self.bg.setText("")
        self.bg.setPixmap(QtGui.QPixmap("graphics/loading.png"))
        self.bg.setObjectName("bg")
        self.loadlabel_stars = QtWidgets.QLabel(Dialog)
        self.loadlabel_stars.setEnabled(True)
        self.loadlabel_stars.setGeometry(QtCore.QRect(0, 0, 400, 300))
        self.loadlabel_stars.setText("")
        self.loadlabel_stars.setAlignment(QtCore.Qt.AlignCenter)
        self.loadlabel_stars.setObjectName("loadlabel_stars")
        self.standby_2 = QtWidgets.QLabel(Dialog)
        self.standby_2.setGeometry(QtCore.QRect(40, 40, 321, 61))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(9)
        self.standby_2.setFont(font)
        self.standby_2.setStyleSheet("color:white;")
        self.standby_2.setText("")
        self.standby_2.setPixmap(QtGui.QPixmap("graphics/loading_head.png"))
        self.standby_2.setAlignment(QtCore.Qt.AlignCenter)
        self.standby_2.setWordWrap(True)
        self.standby_2.setObjectName("standby_2")
        self.bg.raise_()
        self.loadlabel_stars.raise_()
        self.standby.raise_()
        self.standby_2.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Loading..."))
        self.standby.setText(_translate("Dialog", "Standby while we load barrels full of kittens"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

