"""
coding:utf-8
file: devicebutton.py
@author: jiangwei
@contact: jiangwei_1994124@163.com
@time: 2021/11/8 23:04
@desc:
"""
from PyQt5 import QtGui
from PyQt5.QtCore import QTimer, Qt, QRectF, QPoint, QEvent, QObject
from PyQt5.QtGui import QPainter, QImage, QFont
from PyQt5.QtWidgets import QWidget
from enum import Enum

class ButtonStyle(Enum):
    ButtonStyle_Circle = 0
    ButtonStyle_Police = 1
    ButtonStyle_Bubble = 2
    ButtonStyle_Bubble2 = 3
    ButtonStyle_Msg = 4
    ButtonStyle_Msg2 = 5


class ButtonColor(Enum):
    ButtonColor_Green = 0
    ButtonColor_Blue = 1
    ButtonColor_Red = 2
    ButtonColor_Gray = 3
    ButtonColor_Black = 4
    ButtonColor_Purple = 5
    ButtonColor_Yellow = 6


class DeviceButton(QWidget):
    def __init__(self):
        super(DeviceButton, self).__init__()
        self.can_move = False
        self.button_style = ButtonStyle.ButtonStyle_Police
        self.button_color = ButtonColor.ButtonColor_Green
        self.text = ''

        self.type = 'police'
        self.img_name = 'image/devicebutton/devicebutton_green_%s.ong' % self.type
        self.is_dark = False

        self.timer = QTimer(self)
        self.timer.setInterval(500)
        self.timer.timeout.connect(self.check_alarm)
        self.installEventFilter(self)

    def paintEvent(self, e: QtGui.QPaintEvent) -> None:
        width = self.width()
        height = self.height()

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        img = QImage(self.img_name)

        if not img.isNull():
            img = img.scaled(width, height, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
            painter.drawImage(0, 0, img)

        font = QFont()
        font.setPixelSize(height * 0.37)
        font.setBold(True)

        rect = self.rect()

        if self.button_style == ButtonStyle.ButtonStyle_Police:
            y = 30 * height / 60
            rect = QRectF(0, y, width, height - y)
        elif self.button_style == ButtonStyle.ButtonStyle_Bubble:
            y = 8 * height / 60
            rect = QRectF(0, 0, width, height - y)
        elif self.button_style == ButtonStyle.ButtonStyle_Bubble2:
            y = 13 * height / 60
            rect = QRectF(0, 0, width, height - y)
            font.setPixelSize(width * 0.33)
        elif self.button_style == ButtonStyle.ButtonStyle_Msg:
            y = 17 * height / 60
            rect = QRectF(0, 0, width, height - y)
        elif self.button_style == ButtonStyle.ButtonStyle_Msg2:
            y = 17 * height / 60
            rect = QRectF(0, 0, width, height - y)

        painter.setFont(font)
        painter.setPen(Qt.white)
        painter.drawText(rect, Qt.AlignCenter, text=self.text)

    def eventFilter(self, watched: QObject, event: QEvent) -> bool:

        if self.can_move:
            last_point = QPoint()
            is_pressed = False

            if event.type() == QEvent.MouseButtonPress:
                pass