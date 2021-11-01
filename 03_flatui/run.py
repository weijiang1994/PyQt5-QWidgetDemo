"""
# coding:utf-8
@Time    : 2021/11/01
@Author  : jiangwei
@File    : run.py
@Desc    : run
@Software: PyCharm
"""
from PyQt5.QtWidgets import QApplication, QWidget, QAbstractItemView, QTableWidgetItem
import sys
from flatui import FlatUI
from frmflatui import *
import datetime


class FlatWin(QWidget, Ui_frmFlatUI):
    def __init__(self):
        super(FlatWin, self).__init__()
        self.setupUi(self)
        self.init_form()

    def init_form(self):
        self.bar1.setRange(0, 100)
        self.bar2.setRange(0, 100)
        self.slider1.setRange(0, 100)
        self.slider2.setRange(0, 100)

        self.slider1.valueChanged[int].connect(lambda: self.set_value(self.slider1.value(), self.bar1))
        self.slider2.valueChanged[int].connect(lambda: self.set_value(self.slider2.value(), self.bar2))
        self.slider1.setValue(30)
        self.slider2.setValue(30)

        self.setStyleSheet("*{outline:0px;}QWidget#frmFlatUI{background:#FFFFFF;}")
        self.flat_ui = FlatUI()
        self.flat_ui.set_pushbutton_qss(self.btn1)
        self.flat_ui.set_pushbutton_qss(self.btn2, 5, 8, "#1ABC9C", "#E6F8F5", "#2EE1C1", "#FFFFFF", "#16A086",
                                        "#A7EEE6")
        self.flat_ui.set_pushbutton_qss(self.btn3, 5, 8, "#3498DB", "#FFFFFF", "#5DACE4", "#E5FEFF", "#2483C7",
                                        "#A0DAFB")
        self.flat_ui.set_pushbutton_qss(self.btn4, 5, 8, "#E74C3C", "#FFFFFF", "#EC7064", "#FFF5E7", "#DC2D1A",
                                        "#F5A996")

        self.flat_ui.set_lineedit_qss(self.txt1)
        self.flat_ui.set_lineedit_qss(self.txt2, 5, 2, "#DCE4EC", "#1ABC9C")
        self.flat_ui.set_lineedit_qss(self.txt3, 3, 1, "#DCE4EC", "#3498DB")
        self.flat_ui.set_lineedit_qss(self.txt4, 3, 1, "#DCE4EC", "#E74C3C")

        self.flat_ui.set_progress_qss(self.bar1)
        self.flat_ui.set_progress_qss(self.bar2, 8, 5, 9, "#E8EDF2", "#1ABC9C")

        self.flat_ui.set_slider_qss(self.slider1)
        self.flat_ui.set_slider_qss(self.slider2, 10, "#E8EDF2", "#E74C3C", "#E74C3C")
        self.flat_ui.set_slider_qss(self.slider3, 10, "#E8EDF2", "#34495E", "#34495E")

        self.flat_ui.set_radiobutton_qss(self.rbtn1)
        self.flat_ui.set_radiobutton_qss(self.rbtn2, 8, "#D7DBDE", "#1ABC9C")
        self.flat_ui.set_radiobutton_qss(self.rbtn3, 8, "#D7DBDE", "#3498DB")
        self.flat_ui.set_radiobutton_qss(self.rbtn4, 8, "#D7DBDE", "#E74C3C")

        self.flat_ui.set_scrollbar_qss(self.horizontalScrollBar)
        self.flat_ui.set_scrollbar_qss(self.verticalScrollBar, 8, 120, 20, "#606060", "#34495E", "#1ABC9C", "#E74C3C")

        width = 1920
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setColumnWidth(0, int(width * 0.06))
        self.tableWidget.setColumnWidth(1, int(width * 0.10))
        self.tableWidget.setColumnWidth(2, int(width * 0.06))
        self.tableWidget.setColumnWidth(3, int(width * 0.10))
        self.tableWidget.setColumnWidth(4, int(width * 0.20))

        head_text = ["设备编号", "设备名称", "设备地址", "告警内容", "告警时间"]
        self.tableWidget.setHorizontalHeaderLabels(head_text)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)

        self.tableWidget.setRowCount(300)

        for i in range(300):
            self.tableWidget.setRowHeight(i, 24)
            item_device_id = QTableWidgetItem(str(i + 1))
            item_device_name = QTableWidgetItem('测试设备%s' % i)
            item_device_addr = QTableWidgetItem(str(i + 1))
            item_content = QTableWidgetItem('防区告警')
            item_time = QTableWidgetItem(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

            self.tableWidget.setItem(i, 0, item_device_id)
            self.tableWidget.setItem(i, 1, item_device_name)
            self.tableWidget.setItem(i, 2, item_device_addr)
            self.tableWidget.setItem(i, 3, item_content)
            self.tableWidget.setItem(i, 4, item_time)

    def set_value(self, value, obj):
        obj.setValue(value)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = FlatWin()
    win.show()
    sys.exit(app.exec_())
