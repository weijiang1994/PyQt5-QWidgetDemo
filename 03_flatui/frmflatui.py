# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmflatui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_frmFlatUI(object):
    def setupUi(self, frmFlatUI):
        frmFlatUI.setObjectName("frmFlatUI")
        frmFlatUI.resize(800, 600)
        frmFlatUI.setStyleSheet("")
        self.gridLayout = QtWidgets.QGridLayout(frmFlatUI)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.rbtn1 = QtWidgets.QRadioButton(frmFlatUI)
        self.rbtn1.setChecked(True)
        self.rbtn1.setObjectName("rbtn1")
        self.gridLayout.addWidget(self.rbtn1, 7, 0, 1, 1)
        self.btn3 = QtWidgets.QPushButton(frmFlatUI)
        self.btn3.setStyleSheet("")
        self.btn3.setObjectName("btn3")
        self.gridLayout.addWidget(self.btn3, 0, 2, 1, 1)
        self.txt3 = QtWidgets.QLineEdit(frmFlatUI)
        self.txt3.setObjectName("txt3")
        self.gridLayout.addWidget(self.txt3, 1, 2, 1, 1)
        self.btn2 = QtWidgets.QPushButton(frmFlatUI)
        self.btn2.setStyleSheet("")
        self.btn2.setObjectName("btn2")
        self.gridLayout.addWidget(self.btn2, 0, 1, 1, 1)
        self.slider3 = QtWidgets.QSlider(frmFlatUI)
        self.slider3.setOrientation(QtCore.Qt.Vertical)
        self.slider3.setInvertedControls(False)
        self.slider3.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.slider3.setObjectName("slider3")
        self.gridLayout.addWidget(self.slider3, 0, 4, 9, 1)
        self.rbtn2 = QtWidgets.QRadioButton(frmFlatUI)
        self.rbtn2.setObjectName("rbtn2")
        self.gridLayout.addWidget(self.rbtn2, 7, 1, 1, 1)
        self.bar2 = QtWidgets.QProgressBar(frmFlatUI)
        self.bar2.setMinimumSize(QtCore.QSize(0, 16))
        self.bar2.setProperty("value", 24)
        self.bar2.setObjectName("bar2")
        self.gridLayout.addWidget(self.bar2, 2, 2, 1, 2)
        self.horizontalScrollBar = QtWidgets.QScrollBar(frmFlatUI)
        self.horizontalScrollBar.setStyleSheet("")
        self.horizontalScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar.setObjectName("horizontalScrollBar")
        self.gridLayout.addWidget(self.horizontalScrollBar, 5, 0, 1, 4)
        self.rbtn4 = QtWidgets.QRadioButton(frmFlatUI)
        self.rbtn4.setObjectName("rbtn4")
        self.gridLayout.addWidget(self.rbtn4, 7, 3, 1, 1)
        self.rbtn3 = QtWidgets.QRadioButton(frmFlatUI)
        self.rbtn3.setObjectName("rbtn3")
        self.gridLayout.addWidget(self.rbtn3, 7, 2, 1, 1)
        self.btn4 = QtWidgets.QPushButton(frmFlatUI)
        self.btn4.setStyleSheet("")
        self.btn4.setObjectName("btn4")
        self.gridLayout.addWidget(self.btn4, 0, 3, 1, 1)
        self.txt2 = QtWidgets.QLineEdit(frmFlatUI)
        self.txt2.setObjectName("txt2")
        self.gridLayout.addWidget(self.txt2, 1, 1, 1, 1)
        self.txt4 = QtWidgets.QLineEdit(frmFlatUI)
        self.txt4.setObjectName("txt4")
        self.gridLayout.addWidget(self.txt4, 1, 3, 1, 1)
        self.btn1 = QtWidgets.QPushButton(frmFlatUI)
        self.btn1.setStyleSheet("")
        self.btn1.setObjectName("btn1")
        self.gridLayout.addWidget(self.btn1, 0, 0, 1, 1)
        self.txt1 = QtWidgets.QLineEdit(frmFlatUI)
        self.txt1.setObjectName("txt1")
        self.gridLayout.addWidget(self.txt1, 1, 0, 1, 1)
        self.bar1 = QtWidgets.QProgressBar(frmFlatUI)
        self.bar1.setMinimumSize(QtCore.QSize(0, 16))
        self.bar1.setProperty("value", 24)
        self.bar1.setObjectName("bar1")
        self.gridLayout.addWidget(self.bar1, 2, 0, 1, 2)
        self.verticalScrollBar = QtWidgets.QScrollBar(frmFlatUI)
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.gridLayout.addWidget(self.verticalScrollBar, 0, 5, 9, 1)
        self.slider1 = QtWidgets.QSlider(frmFlatUI)
        self.slider1.setMinimumSize(QtCore.QSize(0, 20))
        self.slider1.setOrientation(QtCore.Qt.Horizontal)
        self.slider1.setObjectName("slider1")
        self.gridLayout.addWidget(self.slider1, 3, 0, 1, 2)
        self.slider2 = QtWidgets.QSlider(frmFlatUI)
        self.slider2.setMinimumSize(QtCore.QSize(0, 20))
        self.slider2.setMaximum(255)
        self.slider2.setOrientation(QtCore.Qt.Horizontal)
        self.slider2.setObjectName("slider2")
        self.gridLayout.addWidget(self.slider2, 3, 2, 1, 2)
        self.tableWidget = QtWidgets.QTableWidget(frmFlatUI)
        self.tableWidget.setStyleSheet("")
        self.tableWidget.setGridStyle(QtCore.Qt.DashDotLine)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 9, 0, 1, 6)

        self.retranslateUi(frmFlatUI)
        QtCore.QMetaObject.connectSlotsByName(frmFlatUI)

    def retranslateUi(self, frmFlatUI):
        _translate = QtCore.QCoreApplication.translate
        frmFlatUI.setWindowTitle(_translate("frmFlatUI", "Form"))
        self.rbtn1.setText(_translate("frmFlatUI", "??????"))
        self.btn3.setText(_translate("frmFlatUI", "????????????"))
        self.btn2.setText(_translate("frmFlatUI", "????????????"))
        self.rbtn2.setText(_translate("frmFlatUI", "??????"))
        self.rbtn4.setText(_translate("frmFlatUI", "??????"))
        self.rbtn3.setText(_translate("frmFlatUI", "??????"))
        self.btn4.setText(_translate("frmFlatUI", "????????????"))
        self.btn1.setText(_translate("frmFlatUI", "????????????"))
