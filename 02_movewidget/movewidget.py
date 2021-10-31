"""
coding:utf-8
file: movewidget.py
@author: jiangwei
@contact: jiangwei_1994124@163.com
@time: 2021/10/31 21:52
@desc:
"""
from PyQt5.QtCore import QObject, QPoint, Qt
from PyQt5.QtWidgets import QWidget
from PyQt5.Qt import QEvent, QMouseEvent
import traceback


class MoveWidget(QObject):
    def __init__(self, parent=0):
        super(MoveWidget, self).__init__(parent=parent)
        self.last_point = QPoint(0, 0)
        self.pressed = False
        self.left_button = True
        self.in_control = True
        self.widget = 0

    def eventFilter(self, watched: QObject, event: QEvent) -> bool:
        try:
            if self.widget != 0 and watched == self.widget:
                # mouse_event = QMouseEvent(event)
                print(event)
                mouse_event = event
                if mouse_event.type() == QEvent.MouseButtonPress:
                    if self.left_button and mouse_event.button() == Qt.LeftButton:
                        return False

                    if self.widget.rect().contains(mouse_event.pos()):
                        self.last_point = mouse_event.pos()
                        self.pressed = True
                elif mouse_event.type() == QEvent.MouseMove and self.pressed:
                    offset_x = mouse_event.pos().x() - self.last_point.x()
                    offset_y = mouse_event.pos().y() - self.last_point.y()
                    x = self.widget.x() + offset_x
                    y = self.widget.y() + offset_y

                    if self.in_control:
                        offset = 20
                        xy_out = (x + self.widget.width() < offset or y + self.widget.height())
                        wh_out = False
                        w = QWidget(self.widget.parent())
                        if w != 0:
                            wh_out = w.width() - x < offset or w.height() - y < offset

                        if xy_out or wh_out:
                            return False
                    self.widget.move(x, y)
                elif mouse_event.type() == QEvent.MouseButtonRelease and self.pressed:
                    self.pressed = False
        except:
            traceback.print_exc()
        return super(MoveWidget, self).eventFilter(watched, event)

    def set_left_button(self, left_button):
        self.left_button = left_button

    def set_in_control(self, in_control):
        self.in_control = in_control

    def set_widget(self, widget: QWidget):
        if self.widget == 0:
            self.widget = widget
            self.widget.installEventFilter(self)
