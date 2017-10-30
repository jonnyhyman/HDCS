# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resetting.ui'
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
        self.uploadlabel.setPixmap(QtGui.QPixmap("graphics/resetting_head.png"))
        self.uploadlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.uploadlabel.setWordWrap(True)
        self.uploadlabel.setObjectName("uploadlabel")
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(170, 110, 85, 91))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Micros = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.Micros.setStyleSheet("color:white;")
        self.Micros.setTristate(False)
        self.Micros.setObjectName("Micros")
        self.verticalLayout.addWidget(self.Micros)
        self.ADCS = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.ADCS.setStyleSheet("color:white;")
        self.ADCS.setObjectName("ADCS")
        self.verticalLayout.addWidget(self.ADCS)
        self.ADCS_STOP = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.ADCS_STOP.setStyleSheet("color:white;")
        self.ADCS_STOP.setObjectName("ADCS_STOP")
        self.verticalLayout.addWidget(self.ADCS_STOP)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(130, 210, 141, 31))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.GO = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.GO.setObjectName("GO")
        self.verticalLayout_2.addWidget(self.GO)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Upload"))
        self.Micros.setText(_translate("Dialog", "Micros"))
        self.ADCS.setText(_translate("Dialog", "ADCS"))
        self.ADCS_STOP.setText(_translate("Dialog", "ADCS OFF"))
        self.GO.setText(_translate("Dialog", "Make It So"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

