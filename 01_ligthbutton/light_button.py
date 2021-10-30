"""
# coding:utf-8
@Time    : 2021/10/29
@Author  : jiangwei
@File    : light_button.py
@Desc    : light_button
@Software: PyCharm
"""
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QColor, QPainter, QFont, QLinearGradient, QPaintEvent
from PyQt5.QtCore import QTimer, QPoint, Qt, QRect
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
        self.timer_alarm.setInterval(1000)

    def eventFilter(self, watch: 'QObject', event: 'QEvent') -> bool:
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
        super().eventFilter(watch, event)

    def paintEvent(self, a0: QPaintEvent) -> None:
        width = self.width()
        height = self.height()
        side = min(width, height)

        painter = QPainter()
        painter.setRenderHint(QPainter.Antialiasing | QPainter.TextAntialiasing)

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
            return
        radius = 100
        painter.save()

        font = QFont()
        font.setPixelSize(85)
        painter.setFont(font)
        painter.setPen(self.text_color)
        rect = QRect(-radius, -radius, radius * 2, radius * 2)
        painter.drawText(rect, Qt.AlignCenter, text=self.text)
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
        small_circle.addEllipse(-radius, -radius, radius*2, radius*2)
        radius *= 2
        big_circle.addEllipse(-radius, -radius+140, radius * 2, radius * 2)
        highlight = small_circle - big_circle

        linear_gradient = QLinearGradient(0, -radius / 2, 0, 0 )
        self.overlay_color.setAlpha(100)
        linear_gradient.setColorAt(0.0, self.overlay_color)
        self.overlay_color.setAlpha(30)
        linear_gradient.setColorAt(1.0, self.overlay_color)
        painter.setBrush(linear_gradient)
        painter.rotate(-20)
        painter.drawPath(highlight)
        painter.restore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = LightButton()
    win.show()
    sys.exit(app.exec_())
