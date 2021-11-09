"""
coding:utf-8
file: devicebutton.py
@author: jiangwei
@contact: jiangwei_1994124@163.com
@time: 2021/11/8 23:04
@desc:
"""
from PyQt5 import QtGui, QtCore
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
    def __init__(self, parent):
        super(DeviceButton, self).__init__(parent)
        self.can_move = False
        self.button_style = ButtonStyle.ButtonStyle_Police
        self.button_color = ButtonColor.ButtonColor_Green
        self.text = '1'
        self.last_point = QPoint()
        self.is_pressed = False

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
        painter.drawText(rect, Qt.AlignCenter, self.text)

    def eventFilter(self, watched: QObject, event: QEvent) -> bool:
        if self.can_move:
            last_point = QPoint()
            if event.type() == QEvent.MouseButtonPress:
                if self.rect().contains(event.pos()) and event.button() == Qt.LeftButton:
                    last_point = event.pos()
                    self.is_pressed = True
            elif event.type() == QEvent.MouseMove and self.is_pressed:
                dx = event.pos().x() - last_point.x()
                dy = event.pos().y() - last_point.y()

                self.move(self.x() + dx, self.x() + dy)
                return True
            elif event.type() == QEvent.MouseButtonRelease and self.is_pressed:
                self.is_pressed = False

        if event.type() == QEvent.MouseButtonPress:
            pass
        elif event.type() == QEvent.MouseButtonDblClick:
            pass
        return super(DeviceButton, self).eventFilter(watched, event)

    def get_can_move(self):
        return self.can_move

    def get_text(self):
        return self.text

    def get_button_style(self):
        return self.button_style

    def get_button_color(self):
        return self.button_color

    def sizeHint(self) -> QtCore.QSize:
        return QtCore.QSize(50, 50)

    def minimumSizeHint(self) -> QtCore.QSize:
        return QtCore.QSize(10, 10)

    def check_alarm(self):
        if self.is_dark:
            self.img_name = "image/devicebutton/devicebutton_black_%s.png" % self.type
        else:
            self.img_name = "image/devicebutton/devicebutton_red_%s.png" % self.type
        self.is_dark = not self.is_dark
        self.update()

    def set_can_move(self, can_move):
        self.can_move = can_move

    def set_text(self, text):
        if self.text != text:
            self.text = text
            self.update()

    def set_button_style(self, button_style):
        self.button_style = button_style
        if self.button_style == ButtonStyle.ButtonStyle_Circle:
            self.type = 'circle'
        elif self.button_style == ButtonStyle.ButtonStyle_Police:
            self.type = 'police'
        elif self.button_style == ButtonStyle.ButtonStyle_Bubble:
            self.type = 'bubble'
        elif self.button_style == ButtonStyle.ButtonStyle_Bubble2:
            self.type = 'bubble2'
        elif self.button_style == ButtonStyle.ButtonStyle_Msg:
            self.type = 'msg'
        elif self.button_style == ButtonStyle.ButtonStyle_Msg2:
            self.type = 'msg2'
        else:
            self.type = 'circle'
        self.set_button_color(self.button_color)

    def set_button_color(self, button_color):
        self.button_color = button_color

        self.is_dark = False

        if self.timer.isActive():
            self.timer.stop()

        if self.button_color == ButtonColor.ButtonColor_Green:
            self.img_name = 'image/devicebutton/devicebutton_green_%s.png' % self.type
        elif self.button_color == ButtonColor.ButtonColor_Blue:
            self.img_name = 'image/devicebutton/devicebutton_blue_%s.png' % self.type
        elif self.button_color == ButtonColor.ButtonColor_Gray:
            self.img_name = 'image/devicebutton/devicebutton_gray_%s.png' % self.type
        elif self.button_color == ButtonColor.ButtonColor_Black:
            self.img_name = 'image/devicebutton/devicebutton_black_%s.png' % self.type
        elif self.button_color == ButtonColor.ButtonColor_Purple:
            self.img_name = 'image/devicebutton/devicebutton_purple_%s.png' % self.type
        elif self.button_color == ButtonColor.ButtonColor_Yellow:
            self.img_name = 'image/devicebutton/devicebutton_yellow_%s.png' % self.type
        elif self.button_color == ButtonColor.ButtonColor_Red:
            self.img_name = 'image/devicebutton/devicebutton_red_%s.png' % self.type
            self.check_alarm()
            if not self.timer.isActive():
                self.timer.start()

        self.update()
