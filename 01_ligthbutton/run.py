"""
coding:utf-8
file: run.py
@author: jiangwei
@contact: jiangwei_1994124@163.com
@time: 2021/10/30 20:38
@desc:
"""
from PyQt5.QtGui import QColor

from light_button import LightButton
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.Qt import QHBoxLayout
import sys


class LightButtonWin(QWidget):
    def __init__(self):
        super(LightButtonWin, self).__init__()
        self.ltbn1 = LightButton()
        self.ltbn2 = LightButton()
        self.ltbn3 = LightButton()
        self.layout = QHBoxLayout()
        self.ltbn2.set_bg_color(QColor(255, 107, 107))
        self.ltbn3.set_bg_color(QColor(24, 189, 155))
        self.layout.addWidget(self.ltbn1)
        self.layout.addWidget(self.ltbn2)
        self.layout.addWidget(self.ltbn3)
        self.setLayout(self.layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = LightButtonWin()
    win.setWindowTitle('LightButton')
    win.show()
    sys.exit(app.exec_())
