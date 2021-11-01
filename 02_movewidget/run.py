"""
coding:utf-8
file: run.py
@author: jiangwei
@contact: jiangwei_1994124@163.com
@time: 2021/10/31 22:05
@desc:
"""
from mw_frame import Ui_Form
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout
import sys
from movewidget import MoveWidget
import traceback


class MoveWidgetWin(QWidget, Ui_Form):
    def __init__(self):
        super(MoveWidgetWin, self).__init__()
        self.setupUi(self)
        self.btn1.setGeometry(10, 10, 250, 25)
        # self.btn2.setGeometry(10, 40, 250, 25)
        mw1 = MoveWidget(self)
        mv2 = MoveWidget(self)
        mw1.set_widget(self.btn1)
        # mv2.set_widget(self.btn2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MoveWidgetWin()
    win.show()
    sys.exit(app.exec_())
