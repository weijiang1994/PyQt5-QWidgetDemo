"""
# coding:utf-8
@Time    : 2021/11/08
@Author  : jiangwei
@File    : mouseline.py
@Desc    : mouseline
@email   : qq804022023@gmail.com
@Software: PyCharm
"""
from PyQt5 import QtGui
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtWidgets import QWidget, QApplication
from widget import Ui_Widget
import sys


class MouseLine(QWidget, Ui_Widget):
    def __init__(self):
        super(MouseLine, self).__init__()
        self.setupUi(self)
        self.last_pos = QPoint()

    def mouseMoveEvent(self, e: QtGui.QMouseEvent) -> None:
        self.last_pos = e.pos()
        self.update()

    def mouseReleaseEvent(self, e: QtGui.QMouseEvent) -> None:
        self.last_pos = e.pos()
        self.update()

    def paintEvent(self, e: QtGui.QPaintEvent) -> None:
        painter = QPainter(self)

        pen = QPen()
        pen.setWidth(5)
        pen.setColor(Qt.red)

        painter.drawLine(0, self.last_pos.y(), self.width(), self.last_pos.y())
        painter.drawLine(self.last_pos.x(), 0, self.last_pos.x(), self.height())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MouseLine()
    win.show()
    sys.exit(app.exec_())
