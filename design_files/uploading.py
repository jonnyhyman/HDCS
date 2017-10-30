# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uploading.ui'
#
# Created by: PyQt5 UI code generator 5.9
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
        self.loadlabel_stars = QtWidgets.QLabel(Dialog)
        self.loadlabel_stars.setEnabled(True)
        self.loadlabel_stars.setGeometry(QtCore.QRect(0, 0, 400, 300))
        self.loadlabel_stars.setText("")
        self.loadlabel_stars.setAlignment(QtCore.Qt.AlignCenter)
        self.loadlabel_stars.setObjectName("loadlabel_stars")
        self.uploadlabel = QtWidgets.QLabel(Dialog)
        self.uploadlabel.setGeometry(QtCore.QRect(40, 40, 321, 61))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(9)
        self.uploadlabel.setFont(font)
        self.uploadlabel.setStyleSheet("color:white;")
        self.uploadlabel.setText("")
        self.uploadlabel.setPixmap(QtGui.QPixmap("graphics/uploading_head.png"))
        self.uploadlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.uploadlabel.setWordWrap(True)
        self.uploadlabel.setObjectName("uploadlabel")
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(180, 110, 51, 91))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.U1 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.U1.setStyleSheet("color:white;")
        self.U1.setTristate(False)
        self.U1.setObjectName("U1")
        self.verticalLayout.addWidget(self.U1)
        self.U2 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.U2.setStyleSheet("color:white;")
        self.U2.setObjectName("U2")
        self.verticalLayout.addWidget(self.U2)
        self.U3 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.U3.setStyleSheet("color:white;")
        self.U3.setObjectName("U3")
        self.verticalLayout.addWidget(self.U3)
        self.U4 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.U4.setStyleSheet("color:white;")
        self.U4.setObjectName("U4")
        self.verticalLayout.addWidget(self.U4)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(130, 210, 141, 31))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.UP = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.UP.setObjectName("UP")
        self.verticalLayout_2.addWidget(self.UP)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Upload"))
        self.U1.setText(_translate("Dialog", "U1"))
        self.U2.setText(_translate("Dialog", "U2"))
        self.U3.setText(_translate("Dialog", "U3"))
        self.U4.setText(_translate("Dialog", "U4"))
        self.UP.setText(_translate("Dialog", "Make It So"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

