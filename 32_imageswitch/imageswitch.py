"""
# coding:utf-8
@Time    : 2021/11/08
@Author  : jiangwei
@File    : imageswitch.py
@Desc    : imageswitch
@email   : qq804022023@gmail.com
@Software: PyCharm
"""
from enum import Enum

from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt, QPoint, QSize
from PyQt5.QtGui import QPainter, QImage
from PyQt5.QtWidgets import QWidget


class ButtonStyle(Enum):
    ButtonStyle_1 = 0
    ButtonStyle_2 = 1
    ButtonStyle_3 = 2


class ImageSwitch(QWidget):
    def __init__(self):
        super(ImageSwitch, self).__init__()
        self.is_checked = False
        self.button_style = ButtonStyle.ButtonStyle_2
        self.img_off_file = 'image/imageswitch/btncheckoff2.png'
        self.img_on_file = 'image/imageswitch/btncheckon2.png'
        self.img_file = self.img_off_file

    def mousePressEvent(self, e: QtGui.QMouseEvent) -> None:
        self.img_file = self.img_off_file if self.is_checked else self.img_on_file
        self.is_checked = not self.is_checked
        self.update()

    def paintEvent(self, e: QtGui.QPaintEvent) -> None:
        painter = QPainter(self)
        painter.setRenderHint(QPainter.SmoothPixmapTransform)
        img = QImage(self.img_file)
        img = img.scaled(self.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)

        pix_x = self.rect().center().x() - img.width() / 2
        pix_y = self.rect().center().y() - img.height() / 2

        point = QPoint(pix_x, pix_y)
        painter.drawImage(point, img)

    def get_checked(self):
        return self.is_checked

    def get_button_style(self):
        return self.button_style

    def sizeHint(self) -> QtCore.QSize:
        return QSize(87, 28)

    def minimumSizeHint(self) -> QtCore.QSize:
        return QSize(87, 28)

    def set_checked(self, is_checked):
        if self.is_checked != is_checked:
            self.is_checked = is_checked
            self.img_file = self.img_on_file if self.is_checked else self.img_off_file
            self.update()

    def set_button_style(self, button_style: ButtonStyle):
        if self.button_style != button_style:
            self.button_style = button_style

            if self.button_style == ButtonStyle.ButtonStyle_1:
                self.img_off_file = 'image/imageswitch/btncheckoff1.png'
                self.img_on_file = 'image/imageswitch/btncheckon1.png'
                self.resize(87, 28)

            elif self.button_style == ButtonStyle.ButtonStyle_2:
                self.img_off_file = 'image/imageswitch/btncheckoff2.png'
                self.img_on_file = 'image/imageswitch/btncheckon2.png'
                self.resize(87, 28)

            else:
                self.img_off_file = 'image/imageswitch/btncheckoff3.png'
                self.img_on_file = 'image/imageswitch/btncheckon3.png'
                self.resize(87, 28)
        self.img_file = self.img_on_file if self.is_checked else self.img_off_file
        self.set_checked(self.is_checked)
        self.update()
        self.updateGeometry()


