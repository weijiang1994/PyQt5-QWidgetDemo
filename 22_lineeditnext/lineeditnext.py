"""
# coding:utf-8
@Time    : 2021/11/08
@Author  : jiangwei
@File    : lineeditnext.py
@Desc    : lineeditnext
@email   : qq804022023@gmail.com
@Software: PyCharm
"""
from widget import Ui_Widget
from PyQt5.QtWidgets import QWidget, QApplication
import sys


class LineEditNext(QWidget, Ui_Widget):

    def __init__(self):
        super(LineEditNext, self).__init__()
        self.setupUi(self)
        self.lineEdit1.returnPressed.connect(lambda: self.next(1))
        self.lineEdit2.returnPressed.connect(lambda: self.next(2))
        self.lineEdit3.returnPressed.connect(lambda: self.next(3))

    def next(self, tag):
        if tag == 1:
            self.lineEdit2.setFocus()
        elif tag == 2:
            self.lineEdit3.setFocus()
        elif tag == 3:
            self.lineEdit1.setFocus()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = LineEditNext()
    win.show()
    sys.exit(app.exec_())
