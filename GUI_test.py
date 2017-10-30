# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testdefwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1056, 730)
        MainWindow.setMinimumSize(QtCore.QSize(500, 500))
        MainWindow.setMaximumSize(QtCore.QSize(1920, 1080))
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.502975, y1:0, x2:0.473, y2:1, stop:0 rgba(2, 11, 16, 255), stop:1 rgba(4, 26, 37, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.testProfileView = GraphicsLayoutWidget(self.centralwidget)
        self.testProfileView.setMinimumSize(QtCore.QSize(750, 1))
        self.testProfileView.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.testProfileView.setStyleSheet("color: white;\n"
"border: 1px solid #4589b2;")
        self.testProfileView.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.testProfileView.setFrameShadow(QtWidgets.QFrame.Plain)
        self.testProfileView.setLineWidth(0)
        self.testProfileView.setMidLineWidth(0)
        self.testProfileView.setObjectName("testProfileView")
        self.horizontalLayout.addWidget(self.testProfileView)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_5 = QtWidgets.QWidget(self.centralwidget)
        self.widget_5.setMinimumSize(QtCore.QSize(273, 1))
        self.widget_5.setMaximumSize(QtCore.QSize(273, 999))
        self.widget_5.setStyleSheet("background: transparent;")
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.label_23 = QtWidgets.QLabel(self.widget_5)
        font = QtGui.QFont()
        font.setFamily("HUN-din 1451")
        font.setPointSize(10)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("color: white;background-color: transparent;")
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setObjectName("label_23")
        self.gridLayout_9.addWidget(self.label_23, 0, 0, 1, 1)
        self.A_del_slide = QtWidgets.QSlider(self.widget_5)
        self.A_del_slide.setStyleSheet("QSlider{\n"
"    background-color: transparent;\n"
"} \n"
"QSlider::groove:horizontal {\n"
"     border: 0px solid #999999;\n"
"     height: 8px;\n"
"     background: rgba(78, 96, 131, 50);\n"
"     margin: 2px 0;\n"
" }\n"
"\n"
"QSlider::groove:horizontal:hover {\n"
"    background-color: rgba(255,255,255,.2);\n"
" }\n"
"\n"
" QSlider::handle:horizontal {\n"
"     background: transparent;\n"
"     border: 1px solid #4589b2;\n"
"     width: 18px;\n"
"     margin: -2px 0;\n"
"     border-radius: 3px;\n"
" }\n"
"\n"
" QSlider::handle:horizontal:hover {\n"
"     background-color: rgba(255,255,255,.2);\n"
"     border: 1px solid #00ce35;\n"
" }")
        self.A_del_slide.setOrientation(QtCore.Qt.Horizontal)
        self.A_del_slide.setObjectName("A_del_slide")
        self.gridLayout_9.addWidget(self.A_del_slide, 0, 2, 1, 1)
        self.A_del = QtWidgets.QDoubleSpinBox(self.widget_5)
        self.A_del.setStyleSheet("QDoubleSpinBox{\n"
"    color: white;\n"
"    background-color: transparent;\n"
"    border: 1px solid #4589b2;\n"
"    padding: 1px;\n"
"}\n"
"\n"
"\n"
"\n"
"QDoubleSpinBox::hover{\n"
"    border: 1px solid #00ce35;\n"
"    background-color: rgba(0,0,0,.3);\n"
"}")
        self.A_del.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.A_del.setObjectName("A_del")
        self.gridLayout_9.addWidget(self.A_del, 0, 3, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.widget_5)
        font = QtGui.QFont()
        font.setFamily("HUN-din 1451")
        font.setPointSize(11)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("color: white;background-color: transparent;")
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")
        self.gridLayout_9.addWidget(self.label_24, 0, 4, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.widget_5)
        font = QtGui.QFont()
        font.setFamily("HUN-din 1451")
        font.setPointSize(10)
        self.label_29.setFont(font)
        self.label_29.setStyleSheet("color: white;background-color: transparent;")
        self.label_29.setAlignment(QtCore.Qt.AlignCenter)
        self.label_29.setObjectName("label_29")
        self.gridLayout_9.addWidget(self.label_29, 0, 1, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_9)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_17 = QtWidgets.QLabel(self.widget_5)
        font = QtGui.QFont()
        font.setFamily("HUN-din 1451")
        font.setPointSize(10)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("color: white;background-color: transparent;")
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 0, 0, 1, 1)
        self.A_dur = QtWidgets.QDoubleSpinBox(self.widget_5)
        self.A_dur.setStyleSheet("QDoubleSpinBox{\n"
"    color: white;\n"
"    background-color: transparent;\n"
"    border: 1px solid #4589b2;\n"
"    padding: 1px;\n"
"}\n"
"\n"
"\n"
"\n"
"QDoubleSpinBox::hover{\n"
"    border: 1px solid #00ce35;\n"
"    background-color: rgba(0,0,0,.3);\n"
"}")
        self.A_dur.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.A_dur.setObjectName("A_dur")
        self.gridLayout.addWidget(self.A_dur, 0, 3, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.widget_5)
        font = QtGui.QFont()
        font.setFamily("HUN-din 1451")
        font.setPointSize(11)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("color: white;background-color: transparent;")
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.gridLayout.addWidget(self.label_21, 0, 4, 1, 1)
        self.A_dur_slide = QtWidgets.QSlider(self.widget_5)
        self.A_dur_slide.setStyleSheet("QSlider{\n"
"    background-color: transparent;\n"
"} \n"
"QSlider::groove:horizontal {\n"
"     border: 0px solid #999999;\n"
"     height: 8px;\n"
"     background: rgba(78, 96, 131, 50);\n"
"     margin: 2px 0;\n"
" }\n"
"\n"
"QSlider::groove:horizontal:hover {\n"
"    background-color: rgba(255,255,255,.2);\n"
" }\n"
"\n"
" QSlider::handle:horizontal {\n"
"     background: transparent;\n"
"     border: 1px solid #4589b2;\n"
"     width: 18px;\n"
"     margin: -2px 0;\n"
"     border-radius: 3px;\n"
" }\n"
"\n"
" QSlider::handle:horizontal:hover {\n"
"     background-color: rgba(255,255,255,.2);\n"
"     border: 1px solid #00ce35;\n"
" }")
        self.A_dur_slide.setOrientation(QtCore.Qt.Horizontal)
        self.A_dur_slide.setObjectName("A_dur_slide")
        self.gridLayout.addWidget(self.A_dur_slide, 0, 2, 1, 1)
        self.label_30 = QtWidgets.QLabel(self.widget_5)
        font = QtGui.QFont()
        font.setFamily("HUN-din 1451")
        font.setPointSize(10)
        self.label_30.setFont(font)
        self.label_30.setStyleSheet("color: white;background-color: transparent;")
        self.label_30.setAlignment(QtCore.Qt.AlignCenter)
        self.label_30.setObjectName("label_30")
        self.gridLayout.addWidget(self.label_30, 0, 1, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        self.gridLayout_12 = QtWidgets.QGridLayout()
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.label_31 = QtWidgets.QLabel(self.widget_5)
        font = QtGui.QFont()
        font.setFamily("HUN-din 1451")
        font.setPointSize(10)
        self.label_31.setFont(font)
        self.label_31.setStyleSheet("color: white;background-color: transparent;")
        self.label_31.setAlignment(QtCore.Qt.AlignCenter)
        self.label_31.setObjectName("label_31")
        self.gridLayout_12.addWidget(self.label_31, 0, 0, 1, 1)
        self.B_del = QtWidgets.QDoubleSpinBox(self.widget_5)
        self.B_del.setStyleSheet("QDoubleSpinBox{\n"
"    color: white;\n"
"    background-color: transparent;\n"
"    border: 1px solid #4589b2;\n"
"    padding: 1px;\n"
"}\n"
"\n"
"\n"
"\n"
"QDoubleSpinBox::hover{\n"
"    border: 1px solid #00ce35;\n"
"    background-color: rgba(0,0,0,.3);\n"
"}")
        self.B_del.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.B_del.setObjectName("B_del")
        self.gridLayout_12.addWidget(self.B_del, 0, 3, 1, 1)
        self.B_del_slide = QtWidgets.QSlider(self.widget_5)
        self.B_del_slide.setStyleSheet("QSlider{\n"
"    background-color: transparent;\n"
"} \n"
"QSlider::groove:horizontal {\n"
"     border: 0px solid #999999;\n"
"     height: 8px;\n"
"     background: rgba(78, 96, 131, 50);\n"
"     margin: 2px 0;\n"
" }\n"
"\n"
"QSlider::groove:horizontal:hover {\n"
"    background-color: rgba(255,255,255,.2);\n"
" }\n"
"\n"
" QSlider::handle:horizontal {\n"
"     background: transparent;\n"
"     border: 1px solid #4589b2;\n"
"     width: 18px;\n"
"     margin: -2px 0;\n"
"     border-radius: 3px;\n"
" }\n"
"\n"
" QSlider::handle:horizontal:hover {\n"
"     background-color: rgba(255,255,255,.2);\n"
"     border: 1px solid #00ce35;\n"
" }")
        self.B_del_slide.setOrientation(QtCore.Qt.Horizontal)
        self.B_del_slide.setObjectName("B_del_slide")
        self.gridLayout_12.addWidget(self.B_del_slide, 0, 2, 1, 1)
        self.label_32 = QtWidgets.QLabel(self.widget_5)
        font = QtGui.QFont()
        font.setFamily("HUN-din 1451")
        font.setPointSize(11)
        self.label_32.setFont(font)
        self.label_32.setStyleSheet("color: white;background-color: transparent;")
        self.label_32.setAlignment(QtCore.Qt.AlignCenter)
        self.label_32.setObjectName("label_32")
        self.gridLayout_12.addWidget(self.label_32, 0, 4, 1, 1)
        self.label_33 = QtWidgets.QLabel(self.widget_5)
        font = QtGui.QFont()
        font.setFamily("HUN-din 1451")
        font.setPointSize(10)
        self.label_33.setFont(font)
        self.label_33.setStyleSheet("color: white;background-color: transparent;")
        self.label_33.setAlignment(QtCore.Qt.AlignCenter)
        self.label_33.setObjectName("label_33")
        self.gridLayout_12.addWidget(self.label_33, 0, 1, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_12)
        self.gridLayout_13 = QtWidgets.QGridLayout()
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.label_34 = QtWidgets.QLabel(self.widget_5)
        font = QtGui.QFont()
        font.setFamily("HUN-din 1451")
        font.setPointSize(10)
        self.label_34.setFont(font)
        self.label_34.setStyleSheet("color: white;background-color: transparent;")
        self.label_34.setAlignment(QtCore.Qt.AlignCenter)
        self.label_34.setObjectName("label_34")
        self.gridLayout_13.addWidget(self.label_34, 0, 0, 1, 1)
        self.B_dur = QtWidgets.QDoubleSpinBox(self.widget_5)
        self.B_dur.setStyleSheet("QDoubleSpinBox{\n"
"    color: white;\n"
"    background-color: transparent;\n"
"    border: 1px solid #4589b2;\n"
"    padding: 1px;\n"
"}\n"
"\n"
"\n"
"\n"
"QDoubleSpinBox::hover{\n"
"    border: 1px solid #00ce35;\n"
"    background-color: rgba(0,0,0,.3);\n"
"}")
        self.B_dur.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.B_dur.setObjectName("B_dur")
        self.gridLayout_13.addWidget(self.B_dur, 0, 3, 1, 1)
        self.B_dur_slide = QtWidgets.QSlider(self.widget_5)
        self.B_dur_slide.setStyleSheet("QSlider{\n"
"    background-color: transparent;\n"
"} \n"
"QSlider::groove:horizontal {\n"
"     border: 0px solid #999999;\n"
"     height: 8px;\n"
"     background: rgba(78, 96, 131, 50);\n"
"     margin: 2px 0;\n"
" }\n"
"\n"
"QSlider::groove:horizontal:hover {\n"
"    background-color: rgba(255,255,255,.2);\n"
" }\n"
"\n"
" QSlider::handle:horizontal {\n"
"     background: transparent;\n"
"     border: 1px solid #4589b2;\n"
"     width: 18px;\n"
"     margin: -2px 0;\n"
"     border-radius: 3px;\n"
" }\n"
"\n"
" QSlider::handle:horizontal:hover {\n"
"     background-color: rgba(255,255,255,.2);\n"
"     border: 1px solid #00ce35;\n"
" }")
        self.B_dur_slide.setOrientation(QtCore.Qt.Horizontal)
        self.B_dur_slide.setObjectName("B_dur_slide")
        self.gridLayout_13.addWidget(self.B_dur_slide, 0, 2, 1, 1)
        self.label_35 = QtWidgets.QLabel(self.widget_5)
        font = QtGui.QFont()
        font.setFamily("HUN-din 1451")
        font.setPointSize(11)
        self.label_35.setFont(font)
        self.label_35.setStyleSheet("color: white;background-color: transparent;")
        self.label_35.setAlignment(QtCore.Qt.AlignCenter)
        self.label_35.setObjectName("label_35")
        self.gridLayout_13.addWidget(self.label_35, 0, 4, 1, 1)
        self.label_36 = QtWidgets.QLabel(self.widget_5)
        font = QtGui.QFont()
        font.setFamily("HUN-din 1451")
        font.setPointSize(10)
        self.label_36.setFont(font)
        self.label_36.setStyleSheet("color: white;background-color: transparent;")
        self.label_36.setAlignment(QtCore.Qt.AlignCenter)
        self.label_36.setObjectName("label_36")
        self.gridLayout_13.addWidget(self.label_36, 0, 1, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_13)
        self.gridLayout_14 = QtWidgets.QGridLayout()
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.label_37 = QtWidgets.QLabel(self.widget_5)
        font = QtGui.QFont()
        font.setFamily("HUN-din 1451")
        font.setPointSize(10)
        self.label_37.setFont(font)
        self.label_37.setStyleSheet("color: white;background-color: transparent;")
        self.label_37.setAlignment(QtCore.Qt.AlignCenter)
        self.label_37.setObjectName("label_37")
        self.gridLayout_14.addWidget(self.label_37, 0, 0, 1, 1)
        self.I_del = QtWidgets.QDoubleSpinBox(self.widget_5)
        self.I_del.setStyleSheet("QDoubleSpinBox{\n"
"    color: white;\n"
"    background-color: transparent;\n"
"    border: 1px solid #4589b2;\n"
"    padding: 1px;\n"
"}\n"
"\n"
"\n"
"\n"
"QDoubleSpinBox::hover{\n"
"    border: 1px solid #00ce35;\n"
"    background-color: rgba(0,0,0,.3);\n"
"}")
        self.I_del.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.I_del.setObjectName("I_del")
        self.gridLayout_14.addWidget(self.I_del, 0, 3, 1, 1)
        self.I_del_slide = QtWidgets.QSlider(self.widget_5)
        self.I_del_slide.setStyleSheet("QSlider{\n"
"    background-color: transparent;\n"
"} \n"
"QSlider::groove:horizontal {\n"
"     border: 0px solid #999999;\n"
"     height: 8px;\n"
"     background: rgba(78, 96, 131, 50);\n"
"     margin: 2px 0;\n"
" }\n"
"\n"
"QSlider::groove:horizontal:hover {\n"
"    background-color: rgba(255,255,255,.2);\n"
" }\n"
"\n"
" QSlider::handle:horizontal {\n"
"     background: transparent;\n"
"     border: 1px solid #4589b2;\n"
"     width: 18px;\n"
"     margin: -2px 0;\n"
"     border-radius: 3px;\n"
" }\n"
"\n"
" QSlider::handle:horizontal:hover {\n"
"     background-color: rgba(255,255,255,.2);\n"
"     border: 1px solid #00ce35;\n"
" }")
        self.I_del_slide.setOrientation(QtCore.Qt.Horizontal)
        self.I_del_slide.setObjectName("I_del_slide")
        self.gridLayout_14.addWidget(self.I_del_slide, 0, 2, 1, 1)
        self.label_38 = QtWidgets.QLabel(self.widget_5)
        font = QtGui.QFont()
        font.setFamily("HUN-din 1451")
        font.setPointSize(11)
        self.label_38.setFont(font)
        self.label_38.setStyleSheet("color: white;background-color: transparent;")
        self.label_38.setAlignment(QtCore.Qt.AlignCenter)
        self.label_38.setObjectName("label_38")
        self.gridLayout_14.addWidget(self.label_38, 0, 4, 1, 1)
        self.label_39 = QtWidgets.QLabel(self.widget_5)
        font = QtGui.QFont()
        font.setFamily("HUN-din 1451")
        font.setPointSize(10)
        self.label_39.setFont(font)
        self.label_39.setStyleSheet("color: white;background-color: transparent;")
        self.label_39.setAlignment(QtCore.Qt.AlignCenter)
        self.label_39.setObjectName("label_39")
        self.gridLayout_14.addWidget(self.label_39, 0, 1, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_14)
        self.gridLayout_15 = QtWidgets.QGridLayout()
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.label_40 = QtWidgets.QLabel(self.widget_5)
        font = QtGui.QFont()
        font.setFamily("HUN-din 1451")
        font.setPointSize(10)
        self.label_40.setFont(font)
        self.label_40.setStyleSheet("color: white;background-color: transparent;")
        self.label_40.setAlignment(QtCore.Qt.AlignCenter)
        self.label_40.setObjectName("label_40")
        self.gridLayout_15.addWidget(self.label_40, 0, 0, 1, 1)
        self.I_dur = QtWidgets.QDoubleSpinBox(self.widget_5)
        self.I_dur.setStyleSheet("QDoubleSpinBox{\n"
"    color: white;\n"
"    background-color: transparent;\n"
"    border: 1px solid #4589b2;\n"
"    padding: 1px;\n"
"}\n"
"\n"
"\n"
"\n"
"QDoubleSpinBox::hover{\n"
"    border: 1px solid #00ce35;\n"
"    background-color: rgba(0,0,0,.3);\n"
"}")
        self.I_dur.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.I_dur.setObjectName("I_dur")
        self.gridLayout_15.addWidget(self.I_dur, 0, 3, 1, 1)
        self.I_dur_slide = QtWidgets.QSlider(self.widget_5)
        self.I_dur_slide.setStyleSheet("QSlider{\n"
"    background-color: transparent;\n"
"} \n"
"QSlider::groove:horizontal {\n"
"     border: 0px solid #999999;\n"
"     height: 8px;\n"
"     background: rgba(78, 96, 131, 50);\n"
"     margin: 2px 0;\n"
" }\n"
"\n"
"QSlider::groove:horizontal:hover {\n"
"    background-color: rgba(255,255,255,.2);\n"
" }\n"
"\n"
" QSlider::handle:horizontal {\n"
"     background: transparent;\n"
"     border: 1px solid #4589b2;\n"
"     width: 18px;\n"
"     margin: -2px 0;\n"
"     border-radius: 3px;\n"
" }\n"
"\n"
" QSlider::handle:horizontal:hover {\n"
"     background-color: rgba(255,255,255,.2);\n"
"     border: 1px solid #00ce35;\n"
" }")
        self.I_dur_slide.setMaximum(99)
        self.I_dur_slide.setOrientation(QtCore.Qt.Horizontal)
        self.I_dur_slide.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.I_dur_slide.setObjectName("I_dur_slide")
        self.gridLayout_15.addWidget(self.I_dur_slide, 0, 2, 1, 1)
        self.label_41 = QtWidgets.QLabel(self.widget_5)
        font = QtGui.QFont()
        font.setFamily("HUN-din 1451")
        font.setPointSize(11)
        self.label_41.setFont(font)
        self.label_41.setStyleSheet("color: white;background-color: transparent;")
        self.label_41.setAlignment(QtCore.Qt.AlignCenter)
        self.label_41.setObjectName("label_41")
        self.gridLayout_15.addWidget(self.label_41, 0, 4, 1, 1)
        self.label_42 = QtWidgets.QLabel(self.widget_5)
        font = QtGui.QFont()
        font.setFamily("HUN-din 1451")
        font.setPointSize(10)
        self.label_42.setFont(font)
        self.label_42.setStyleSheet("color: white;background-color: transparent;")
        self.label_42.setAlignment(QtCore.Qt.AlignCenter)
        self.label_42.setObjectName("label_42")
        self.gridLayout_15.addWidget(self.label_42, 0, 1, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_15)
        self.gridLayout_17 = QtWidgets.QGridLayout()
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.label_44 = QtWidgets.QLabel(self.widget_5)
        font = QtGui.QFont()
        font.setFamily("HUN-din 1451")
        font.setPointSize(11)
        self.label_44.setFont(font)
        self.label_44.setStyleSheet("color: white;background-color: transparent;")
        self.label_44.setAlignment(QtCore.Qt.AlignCenter)
        self.label_44.setObjectName("label_44")
        self.gridLayout_17.addWidget(self.label_44, 0, 4, 1, 1)
        self.label_45 = QtWidgets.QLabel(self.widget_5)
        font = QtGui.QFont()
        font.setFamily("HUN-din 1451")
        font.setPointSize(10)
        self.label_45.setFont(font)
        self.label_45.setStyleSheet("color: white;background-color: transparent;")
        self.label_45.setAlignment(QtCore.Qt.AlignCenter)
        self.label_45.setObjectName("label_45")
        self.gridLayout_17.addWidget(self.label_45, 0, 1, 1, 1)
        self.R_dur = QtWidgets.QDoubleSpinBox(self.widget_5)
        self.R_dur.setStyleSheet("QDoubleSpinBox{\n"
"    color: white;\n"
"    background-color: transparent;\n"
"    border: 1px solid #4589b2;\n"
"    padding: 1px;\n"
"}\n"
"\n"
"\n"
"\n"
"QDoubleSpinBox::hover{\n"
"    border: 1px solid #00ce35;\n"
"    background-color: rgba(0,0,0,.3);\n"
"}")
        self.R_dur.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.R_dur.setObjectName("R_dur")
        self.gridLayout_17.addWidget(self.R_dur, 0, 3, 1, 1)
        self.label_43 = QtWidgets.QLabel(self.widget_5)
        font = QtGui.QFont()
        font.setFamily("HUN-din 1451")
        font.setPointSize(10)
        self.label_43.setFont(font)
        self.label_43.setStyleSheet("color: white;background-color: transparent;")
        self.label_43.setAlignment(QtCore.Qt.AlignCenter)
        self.label_43.setObjectName("label_43")
        self.gridLayout_17.addWidget(self.label_43, 0, 0, 1, 1)
        self.R_dur_slide = QtWidgets.QSlider(self.widget_5)
        self.R_dur_slide.setStyleSheet("QSlider{\n"
"    background-color: transparent;\n"
"} \n"
"QSlider::groove:horizontal {\n"
"     border: 0px solid #999999;\n"
"     height: 8px;\n"
"     background: rgba(78, 96, 131, 50);\n"
"     margin: 2px 0;\n"
" }\n"
"\n"
"QSlider::groove:horizontal:hover {\n"
"    background-color: rgba(255,255,255,.2);\n"
" }\n"
"\n"
" QSlider::handle:horizontal {\n"
"     background: transparent;\n"
"     border: 1px solid #4589b2;\n"
"     width: 18px;\n"
"     margin: -2px 0;\n"
"     border-radius: 3px;\n"
" }\n"
"\n"
" QSlider::handle:horizontal:hover {\n"
"     background-color: rgba(255,255,255,.2);\n"
"     border: 1px solid #00ce35;\n"
" }")
        self.R_dur_slide.setMaximum(99)
        self.R_dur_slide.setOrientation(QtCore.Qt.Horizontal)
        self.R_dur_slide.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.R_dur_slide.setObjectName("R_dur_slide")
        self.gridLayout_17.addWidget(self.R_dur_slide, 0, 2, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_17)
        self.regulatorSetup = QtWidgets.QPushButton(self.widget_5)
        font = QtGui.QFont()
        font.setFamily("Futura BQ")
        font.setPointSize(9)
        self.regulatorSetup.setFont(font)
        self.regulatorSetup.setStyleSheet("QPushButton{\n"
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
        self.regulatorSetup.setObjectName("regulatorSetup")
        self.verticalLayout_3.addWidget(self.regulatorSetup)
        self.widget_4 = QtWidgets.QWidget(self.widget_5)
        self.widget_4.setObjectName("widget_4")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.widget_4)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_16 = QtWidgets.QLabel(self.widget_4)
        font = QtGui.QFont()
        font.setFamily("Futura BQ")
        font.setPointSize(11)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("color: white;background-color: transparent;")
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.verticalLayout.addWidget(self.label_16)
        self.testNotes = QtWidgets.QPlainTextEdit(self.widget_4)
        font = QtGui.QFont()
        font.setFamily("GOST Common")
        font.setPointSize(8)
        self.testNotes.setFont(font)
        self.testNotes.setStyleSheet("color: white;\n"
"background-color: transparent;\n"
"border: 1px solid #4589b2;\n"
"padding: 5px;")
        self.testNotes.setObjectName("testNotes")
        self.verticalLayout.addWidget(self.testNotes)
        self.gridLayout_6.addLayout(self.verticalLayout, 2, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.widget_4)
        self.widget_3 = QtWidgets.QWidget(self.widget_5)
        self.widget_3.setStyleSheet("background: transparent;")
        self.widget_3.setObjectName("widget_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget_3)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_15 = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("Futura BQ")
        font.setPointSize(11)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color:  white;")
        self.label_15.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.gridLayout_4.addWidget(self.label_15, 0, 0, 1, 1)
        self.cancelButton = QtWidgets.QPushButton(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("Futura BQ")
        font.setPointSize(9)
        self.cancelButton.setFont(font)
        self.cancelButton.setStyleSheet("QPushButton{\n"
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
        self.cancelButton.setObjectName("cancelButton")
        self.gridLayout_4.addWidget(self.cancelButton, 1, 0, 1, 1)
        self.uploadButton = QtWidgets.QPushButton(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("Futura BQ")
        font.setPointSize(9)
        self.uploadButton.setFont(font)
        self.uploadButton.setStyleSheet("QPushButton{\n"
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
        self.uploadButton.setObjectName("uploadButton")
        self.gridLayout_4.addWidget(self.uploadButton, 1, 1, 1, 1)
        self.tminus = QtWidgets.QDoubleSpinBox(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("Futura BQ")
        font.setPointSize(9)
        self.tminus.setFont(font)
        self.tminus.setStyleSheet("QDoubleSpinBox{\n"
"    color: white;\n"
"    background-color: transparent;\n"
"    border: 1px solid #4589b2;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"\n"
"\n"
"QDoubleSpinBox::hover{\n"
"    border: 1px solid #00ce35;\n"
"    background-color: rgba(0,0,0,.3);\n"
"}")
        self.tminus.setAlignment(QtCore.Qt.AlignCenter)
        self.tminus.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.tminus.setMaximum(32767.0)
        self.tminus.setSingleStep(0.01)
        self.tminus.setProperty("value", 20.0)
        self.tminus.setObjectName("tminus")
        self.gridLayout_4.addWidget(self.tminus, 0, 1, 1, 1)
        self.verticalLayout_3.addWidget(self.widget_3)
        self.verticalLayout_2.addWidget(self.widget_5)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setStyleSheet("background-color:transparent;")
        self.frame_4.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_4.setLineWidth(0)
        self.frame_4.setMidLineWidth(0)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_2.addWidget(self.frame_4, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1056, 34))
        font = QtGui.QFont()
        font.setFamily("GOST Common")
        self.menuBar.setFont(font)
        self.menuBar.setStyleSheet("color:white;\n"
"background: rgba(255,255,255,.2);\n"
"padding:5px;")
        self.menuBar.setDefaultUp(False)
        self.menuBar.setNativeMenuBar(True)
        self.menuBar.setObjectName("menuBar")
        self.menuSave = QtWidgets.QMenu(self.menuBar)
        self.menuSave.setObjectName("menuSave")
        MainWindow.setMenuBar(self.menuBar)
        self.openFile = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("GOST Common")
        self.openFile.setFont(font)
        self.openFile.setObjectName("openFile")
        self.actionSave_Definition = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("GOST Common")
        self.actionSave_Definition.setFont(font)
        self.actionSave_Definition.setObjectName("actionSave_Definition")
        self.menuSave.addAction(self.openFile)
        self.menuBar.addAction(self.menuSave.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Test Definition Dialog"))
        self.label_23.setText(_translate("MainWindow", "a"))
        self.label_24.setText(_translate("MainWindow", "sec"))
        self.label_29.setText(_translate("MainWindow", "delay"))
        self.label_17.setText(_translate("MainWindow", "a"))
        self.label_21.setText(_translate("MainWindow", "sec"))
        self.label_30.setText(_translate("MainWindow", "durat"))
        self.label_31.setText(_translate("MainWindow", "b"))
        self.label_32.setText(_translate("MainWindow", "sec"))
        self.label_33.setText(_translate("MainWindow", "delay"))
        self.label_34.setText(_translate("MainWindow", "b"))
        self.label_35.setText(_translate("MainWindow", "sec"))
        self.label_36.setText(_translate("MainWindow", "durat"))
        self.label_37.setText(_translate("MainWindow", "i"))
        self.label_38.setText(_translate("MainWindow", "sec"))
        self.label_39.setText(_translate("MainWindow", "delay"))
        self.label_40.setText(_translate("MainWindow", "i"))
        self.label_41.setText(_translate("MainWindow", "sec"))
        self.label_42.setText(_translate("MainWindow", "durat"))
        self.label_44.setText(_translate("MainWindow", "sec"))
        self.label_45.setText(_translate("MainWindow", "durat"))
        self.label_43.setText(_translate("MainWindow", "r"))
        self.regulatorSetup.setText(_translate("MainWindow", "REGULATOR SETUP"))
        self.label_16.setText(_translate("MainWindow", "TEST NOTES"))
        self.label_15.setText(_translate("MainWindow", "START AT T -"))
        self.cancelButton.setText(_translate("MainWindow", "CANCEL"))
        self.uploadButton.setText(_translate("MainWindow", "UPLOAD"))
        self.menuSave.setTitle(_translate("MainWindow", "File"))
        self.openFile.setText(_translate("MainWindow", "Open Definition File"))
        self.actionSave_Definition.setText(_translate("MainWindow", "Save Definition"))

from pyqtgraph import GraphicsLayoutWidget

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
