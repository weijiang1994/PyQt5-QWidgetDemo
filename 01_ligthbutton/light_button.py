"""
# coding:utf-8
@Time    : 2021/10/29
@Author  : jiangwei
@File    : light_button.py
@Desc    : light_button
@Software: PyCharm
"""
from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QColor, QPainter, QFont, QLinearGradient, QPaintEvent
from PyQt5.QtCore import QTimer, QPoint, Qt, QRect, QObject
from PyQt5.Qt import QMouseEvent, QEvent, QPainterPath
import sys


class LightButton(QWidget):
    def __init__(self):
        super().__init__()
        self.text = ""
        self.text_color = QColor(255, 255, 255)
        self.alarm_color = QColor(255, 107, 107)
        self.norma_color = QColor(10, 10, 10)

        self.border_out_color_start = QColor(255, 255, 255)
        self.border_out_color_end = QColor(166, 166, 166)

        self.border_in_color_start = QColor(166, 166, 166)
        self.border_in_color_end = QColor(255, 255, 255)

        self.bg_color = QColor(100, 184, 255)

        self.show_rect = False
        self.show_overlay = True

        self.overlay_color = QColor(255, 255, 255)

        self.can_move = False
        self.installEventFilter(self)

        self.is_alarm = False
        self.timer_alarm = QTimer(self)
        self.timer_alarm.setInterval(500)

    def eventFilter(self, watch: QObject, event: QEvent):
        if self.can_move:
            last_point = QPoint()
            pressed = False
            mouse_event = QMouseEvent(event)
            if mouse_event.type() == QEvent.MouseButtonPress:
                if self.rect().contains(mouse_event.pos()) and mouse_event.button() == Qt.LeftButton:
                    last_point = mouse_event.pos()
                    pressed = True
            elif mouse_event.type() == QEvent.MouseMove and pressed:
                dx = mouse_event.pos().x() - last_point.x()
                dy = mouse_event.pos().y() - last_point.y()
                self.move(self.x() + dx, self.y() + dy)
            elif mouse_event.type() == QEvent.MouseButtonRelease and pressed:
                pressed = False
        return super().eventFilter(watch, event)

    def paintEvent(self, a0: QPaintEvent) -> None:
        width = self.width()
        height = self.height()
        side = min(width, height)

        painter = QPainter(self)
        painter.setRenderHints(QPainter.Antialiasing | QPainter.TextAntialiasing)

        if self.show_rect:
            painter.setPen(Qt.NoPen)
            painter.setBrush(self.bg_color)
            painter.drawRoundedRect(self.rect(), 5, 5)
            if not self.text == '':
                font = QFont()
                font.setPixelSize(side - 20)
                painter.setFont(font)
                painter.setPen(self.text_color)
                painter.drawText(self.rect(), Qt.AlignCenter, self.text)
        else:
            painter.translate(width / 2, height / 2)
            painter.scale(side / 200.0, side / 200.0)
            self.draw_border_out(painter)
            self.draw_border_in(painter)
            self.draw_bg(painter)
            self.draw_text(painter)
            self.draw_overlay(painter)

    def draw_border_out(self, painter: QPainter):
        radius = 90
        painter.save()
        painter.setPen(Qt.NoPen)
        border_gradient = QLinearGradient(0, -radius, 0, radius)
        border_gradient.setColorAt(0, self.border_out_color_start)
        border_gradient.setColorAt(1, self.border_out_color_end)
        painter.setBrush(border_gradient)
        painter.drawEllipse(-radius, -radius, radius * 2, radius * 2)
        painter.restore()

    def draw_border_in(self, painter: QPainter):
        radius = 90
        painter.save()
        painter.setPen(Qt.NoPen)
        border_gradient = QLinearGradient(0, -radius, 0, radius)
        border_gradient.setColorAt(0, self.border_in_color_start)
        border_gradient.setColorAt(1, self.border_in_color_end)
        painter.setBrush(border_gradient)
        painter.drawEllipse(-radius, -radius, radius * 2, radius * 2)
        painter.restore()

    def draw_bg(self, painter: QPainter):
        radius = 80
        painter.save()
        painter.setPen(Qt.NoPen)
        painter.setBrush(self.bg_color)
        painter.drawEllipse(-radius, -radius, radius * 2, radius * 2)
        painter.restore()

    def draw_text(self, painter: QPainter):
        if self.text == '':
            return False
        radius = 100
        painter.save()

        font = QFont()
        font.setPixelSize(50)
        painter.setFont(font)
        painter.setPen(self.text_color)
        rect = QRect(-radius, -radius, radius * 2, radius * 2)
        painter.drawText(rect, Qt.AlignCenter, self.text)
        painter.restore()

    def draw_overlay(self, painter: QPainter):
        if not self.show_overlay:
            return
        radius = 80
        painter.save()
        painter.setPen(Qt.NoPen)

        small_circle = QPainterPath()
        big_circle = QPainterPath()

        radius -= 1
        small_circle.addEllipse(-radius, -radius, radius * 2, radius * 2)
        radius *= 2
        big_circle.addEllipse(-radius, -radius + 140, radius * 2, radius * 2)
        highlight = small_circle - big_circle

        linear_gradient = QLinearGradient(0, -radius / 2, 0, 0)
        self.overlay_color.setAlpha(100)
        linear_gradient.setColorAt(0.0, self.overlay_color)
        self.overlay_color.setAlpha(30)
        linear_gradient.setColorAt(1.0, self.overlay_color)
        painter.setBrush(linear_gradient)
        painter.rotate(-20)
        painter.drawPath(highlight)
        painter.restore()

    def get_text(self):
        return self.text

    def get_text_color(self):
        return self.text_color

    def get_alarm_color(self):
        return self.alarm_color

    def get_normal_color(self):
        return self.norma_color

    def get_border_out_color_start(self):
        return self.border_out_color_start

    def get_border_out_color_end(self):
        return self.border_out_color_end

    def get_border_in_color_start(self):
        return self.border_in_color_start

    def get_border_in_color_end(self):
        return self.border_in_color_end

    def get_bg_color(self):
        return self.bg_color

    def get_can_move(self):
        return self.can_move

    def get_show_rect(self):
        return self.show_rect

    def get_show_overlay(self):
        return self.show_overlay

    def get_overlay_color(self):
        return self.overlay_color

    def sizeHint(self) -> QtCore.QSize:
        return QtCore.QSize(100, 100)

    def minimumSizeHint(self) -> QtCore.QSize:
        return QtCore.QSize(10, 10)

    def set_text(self, text):
        if self.text != text:
            self.text = text
            self.update()

    def set_text_color(self, text_color):
        if self.text_color != text_color:
            self.text_color = text_color
            self.update()

    def set_alarm_color(self, alarm_color):
        if self.alarm_color != alarm_color:
            self.alarm_color = alarm_color
            self.update()

    def set_normal_color(self, normal_color):
        if self.norma_color != normal_color:
            self.norma_color = normal_color
            self.update()

    def set_border_out_color_start(self, border_out_color_start):
        if self.border_out_color_start != border_out_color_start:
            self.border_out_color_start = border_out_color_start
            self.update()

    def set_border_out_color_end(self, border_out_color_end):
        if self.border_out_color_end != border_out_color_end:
            self.border_out_color_end = border_out_color_end
            self.update()

    def set_border_in_color_start(self, border_in_color_start):
        if self.border_in_color_start != border_in_color_start:
            self.border_in_color_start = border_in_color_start
            self.update()

    def set_border_in_color_end(self, border_in_color_end):
        if self.border_in_color_end != border_in_color_end:
            self.border_in_color_end = border_in_color_end
            self.update()

    def set_bg_color(self, bg_color):
        if self.bg_color != bg_color:
            self.bg_color = bg_color
            self.update()

    def set_can_move(self, can_move):
        if self.can_move != can_move:
            self.can_move = can_move
            self.update()

    def set_show_rect(self, show_rect):
        if self.show_rect != show_rect:
            self.show_rect = show_rect
            self.update()

    def set_show_overlay(self, show_overlay):
        if self.show_overlay != show_overlay:
            self.show_overlay = show_overlay
            self.update()

    def set_overlay_color(self, overlay_color):
        if self.overlay_color != overlay_color:
            self.overlay_color = overlay_color
            self.update()

    def set_green(self):
        self.text_color = QColor(255, 255, 255)
        self.set_bg_color(QColor(0, 166, 0))

    def set_red(self):
        self.text_color = QColor(255, 255, 255)
        self.set_bg_color(QColor(255, 0, 0))

    def set_yellow(self):
        self.text_color = QColor(25, 50, 7)
        self.set_bg_color(QColor(238, 238, 0))

    def set_black(self):
        self.text_color = QColor(255, 255, 255)
        self.set_bg_color(QColor(10, 10, 10))

    def set_gray(self):
        self.text_color = QColor(255, 255, 255)
        self.set_bg_color(QColor(129, 129, 129))

    def set_blue(self):
        self.text_color = QColor(255, 255, 255)
        self.set_bg_color(QColor(0, 0, 166))

    def set_light_blue(self):
        self.text_color = QColor(255, 255, 255)
        self.set_bg_color(QColor(100, 184, 255))

    def set_light_red(self):
        self.text_color = QColor(255, 255, 255)
        self.set_bg_color(QColor(255, 107, 107))

    def set_light_green(self):
        self.text_color = QColor(255, 255, 255)
        self.set_bg_color(QColor(24, 189, 155))

    def start_alarm(self):
        if not self.timer_alarm.isActive():
            self.timer_alarm.start()

    def stop_alarm(self):
        if self.timer_alarm.isActive():
            self.timer_alarm.stop()

    def alarm(self):
        if self.is_alarm:
            self.text_color = QColor(255, 255, 255)
            self.bg_color = self.norma_color
        else:
            self.text_color = QColor(255, 255, 255)
            self.bg_color = self.alarm_color
        self.update()
        self.is_alarm = not self.is_alarm
