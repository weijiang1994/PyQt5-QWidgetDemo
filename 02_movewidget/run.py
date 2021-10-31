"""
coding:utf-8
file: run.py
@author: jiangwei
@contact: jiangwei_1994124@163.com
@time: 2021/10/31 22:05
@desc:
"""
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout
import sys
from movewidget import MoveWidget
import traceback


class MoveWidgetWin(QWidget):
    def __init__(self):
        try:
            super(MoveWidgetWin, self).__init__()
            self.layout = QHBoxLayout()
            self.btn1 = QPushButton(self)
            self.btn1.setGeometry(10, 10, 250, 25)
            self.btn1.setText('按住我拖动(仅限左键拖动)')
            self.mv1 = MoveWidget(self)
            self.mv1.set_widget(self.btn1)
            self.layout.addWidget(self.btn1)
            self.setLayout(self.layout)
        except:
            traceback.print_exc()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MoveWidgetWin()
    win.show()
    sys.exit(app.exec_())
