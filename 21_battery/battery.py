"""
# coding:utf-8
@Time    : 2021/11/08
@Author  : jiangwei
@File    : battery.py
@Desc    : battery
@email   : qq804022023@gmail.com
@Software: PyCharm
"""
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QTimer, QPointF, QRectF, Qt, QSize
from PyQt5.QtGui import QColor, QPainter, QPen, QLinearGradient
from PyQt5.QtWidgets import QWidget


class Battery(QWidget):
    def __init__(self):
        super(Battery, self).__init__()

        self.battery_rect = QRectF()

        self.min_value = 0
        self.max_value = 100
        self.value = 0
        self.alarm_value = 30
        self.step = 0.5

        self.border_width = 5
        self.border_radius = 8
        self.bg_radius = 5
        self.head_radius = 3

        self.border_color_start = QColor(100, 100, 100)
        self.border_color_end = QColor(80, 80, 80)
        self.alarm_color_start = QColor(250, 118, 113)
        self.alarm_color_end = QColor(204, 38, 38)
        self.normal_color_start = QColor(50, 205, 51)
        self.normal_color_end = QColor(60, 179, 133)

        self.is_forward = False
        self.current_value = 0

        self.timer = QTimer(self)
        self.timer.setInterval(10)
        self.timer.timeout.connect(self.update_value)

    def paintEvent(self, e: QtGui.QPaintEvent) -> None:
        painter = QPainter(self)
        painter.setRenderHints(QPainter.Antialiasing | QPainter.TextAntialiasing)
        self.draw_border(painter)
        self.draw_bg(painter)
        self.draw_head(painter)

    def draw_border(self, painter: QPainter):
        painter.save()
        head_width = self.width() / 15
        battery_width = self.width() - head_width

        top_left = QPointF(self.border_width, self.border_width)
        bottom_right = QPointF(battery_width, self.height() - self.border_width)
        self.battery_rect = QRectF(top_left, bottom_right)

        painter.setPen(QPen(self.border_color_start, self.border_width))
        painter.setBrush(Qt.NoBrush)
        painter.drawRoundedRect(self.battery_rect, self.border_radius, self.border_radius)

        painter.restore()

    def draw_bg(self, painter: QPainter):
        if self.value == self.min_value:
            return

        painter.save()

        battery_gradient = QLinearGradient(QPointF(0, 0), QPointF(0, self.height()))
        if self.current_value <= self.alarm_value:
            battery_gradient.setColorAt(0.0, self.alarm_color_start)
            battery_gradient.setColorAt(1.0, self.alarm_color_end)
        else:
            battery_gradient.setColorAt(0.0, self.normal_color_start)
            battery_gradient.setColorAt(1.0, self.normal_color_end)

        margin = min(self.width(), self.height()) / 20
        unit = (self.battery_rect.width() - (margin * 2)) / 100
        width = self.current_value * unit

        top_left = QPointF(self.battery_rect.topLeft().x() + margin, self.battery_rect.topLeft().y() + margin)
        bottom_right = QPointF(width + margin + self.border_width, self.battery_rect.bottomRight().y() - margin)
        rect = QRectF(top_left, bottom_right)

        painter.setPen(Qt.NoPen)
        painter.setBrush(battery_gradient)
        painter.drawRoundedRect(rect, self.bg_radius, self.border_radius)

        painter.restore()

    def draw_head(self, painter: QPainter):
        painter.save()

        head_rect_top_left = QPointF(self.battery_rect.topRight().x(), self.height() / 3)
        head_rect_bottom_right = QPointF(self.width(), self.height() - self.height() / 3)
        head_rect = QRectF(head_rect_top_left, head_rect_bottom_right)

        head_rect_gradient = QLinearGradient(head_rect.topLeft(), head_rect.bottomLeft())
        head_rect_gradient.setColorAt(0.0, self.border_color_start)
        head_rect_gradient.setColorAt(1.0, self.border_color_end)

        painter.setPen(Qt.NoPen)
        painter.setBrush(head_rect_gradient)
        painter.drawRoundedRect(head_rect, self.head_radius, self.head_radius)

        painter.restore()

    def update_value(self):
        if self.is_forward:
            self.current_value -= self.step

            if self.current_value <= self.value:
                self.current_value = self.value
                self.timer.stop()
        else:
            self.current_value += self.step
            if self.current_value >= self.value:
                self.current_value = self.value
                self.timer.stop()

        self.update()

    def get_min_value(self):
        return self.min_value

    def get_max_value(self):
        return self.max_value

    def get_value(self):
        return self.value

    def get_alarm_value(self):
        return self.alarm_value

    def get_step(self):
        return self.step

    def get_border_width(self):
        return self.border_width

    def get_border_radius(self):
        return self.border_radius

    def get_bg_radius(self):
        return self.bg_radius

    def get_head_radius(self):
        return self.head_radius

    def get_border_color_start(self):
        return self.border_color_start

    def get_border_color_end(self):
        return self.border_color_end

    def get_alarm_color_start(self):
        return self.alarm_color_start

    def get_alarm_color_end(self):
        return self.alarm_color_end

    def get_normal_color_start(self):
        return self.normal_color_start

    def get_normal_color_end(self):
        return self.normal_color_end

    def sizeHint(self) -> QSize:
        return QSize(150, 80)

    def minimumSizeHint(self) -> QtCore.QSize:
        return QSize(30, 10)

    def set_range(self, min_value, max_value):
        if min_value >= max_value:
            return

        self.min_value = min_value
        self.max_value = max_value
        if self.value < min_value:
            self.set_value(min_value)
        elif self.value > max_value:
            self.set_value(max_value)
        self.update()

    def set_min_value(self, min_value):
        self.set_range(min_value, self.max_value)

    def set_max_value(self, max_value):
        self.set_range(self.min_value, max_value)

    def set_value(self, value):
        if value == self.value:
            return
        if value > self.current_value:
            self.is_forward = False
        elif value < self.current_value:
            self.is_forward = True
        else:
            self.value = value
            self.update()
            return

        self.value = value
        self.update()
        # TODO emit value change signal
        self.timer.stop()
        self.timer.start()

    def set_alarm_value(self, alarm_value):
        if self.alarm_value != alarm_value:
            self.alarm_value = alarm_value
            self.update()

    def set_step(self, step):
        if self.step != step:
            self.step = step
            self.update()

    def set_border_width(self, border_width):
        if self.border_width != border_width:
            self.border_width = border_width
            self.update()

    def set_border_radius(self, border_radius):
        if self.border_radius != border_radius:
            self.border_radius = border_radius
            self.update()

    def set_bg_radius(self, bg_radius):
        if self.bg_radius != bg_radius:
            self.bg_radius = bg_radius
            self.update()

    def set_head_radius(self, head_radius):
        if self.head_radius != head_radius:
            self.head_radius = head_radius
            self.update()

    def set_border_color_start(self, border_color_start):
        if self.border_color_start != border_color_start:
            self.border_color_start = border_color_start
            self.update()

    def set_border_color_end(self, border_color_end):
        if self.border_color_end != border_color_end:
            self.border_color_end = border_color_end
            self.update()

    def set_alarm_color_start(self, alarm_color_start):
        if self.alarm_color_start != alarm_color_start:
            self.alarm_color_start = alarm_color_start
            self.update()

    def set_alarm_color_end(self, alarm_color_end):
        if self.alarm_color_end != alarm_color_end:
            self.alarm_color_end = alarm_color_end
            self.update()

    def set_normal_color_start(self, normal_color_start):
        if self.normal_color_start != normal_color_start:
            self.normal_color_start = normal_color_start
            self.update()

    def set_normal_color_end(self, normal_color_end):
        if self.normal_color_end != normal_color_end:
            self.normal_color_end = normal_color_end
            self.update()


if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication
    import sys
    app = QApplication(sys.argv)
    win = Battery()
    win.current_value = 35
    win.show()
    sys.exit(app.exec_())
