"""
# coding:utf-8
@Time    : 2021/11/05
@Author  : jiangwei
@File    : screenwidget.py
@Desc    : screenwidget
@email   : qq804022023@gmail.com
@Software: PyCharm
"""
import datetime

from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget, QMenu, QAction, QApplication, qApp, QFileDialog
from PyQt5.QtCore import QSize, QPoint, Qt
from PyQt5.QtGui import QPainter, QPen, QPixmap, QColor
from enum import Enum


def now():
    return datetime.datetime.now().strftime('%Y%m%d%H%M%S')


class STATUS(Enum):
    SELECT = 0
    MOV = 1
    SET_W_H = 2


class Screen:

    def __init__(self, size: QSize):
        self.max_width = size.width()
        self.max_height = size.height()

        self.start_pos = QPoint(-1, -1)
        self.end_pos = self.start_pos
        self.left_up_pos = self.start_pos
        self.right_down_pos = self.start_pos
        self.status = STATUS.SELECT

    def width(self):
        return self.max_width

    def height(self):
        return self.max_height

    def get_status(self):
        return self.status

    def set_status(self, status: STATUS):
        self.status = status

    def set_end(self, pos: QPoint):
        self.end_pos = pos
        self.left_up_pos = self.start_pos
        self.right_down_pos = self.end_pos
        self.cmp_point(self.left_up_pos, self.right_down_pos)

    def set_start(self, pos: QPoint):
        self.start_pos = pos

    def get_end(self):
        return self.end_pos

    def get_start(self):
        return self.start_pos

    def get_left_up(self):
        return self.left_up_pos

    def get_right_down(self):
        return self.right_down_pos

    def is_in_area(self, pos: QPoint):
        if self.left_up_pos.x() < pos.x() < self.right_down_pos.x() and self.left_up_pos.y() < pos.y() < \
                self.right_down_pos.y():
            return True
        return False

    def move(self, p: QPoint):
        lx = self.left_up_pos.x() + p.x()
        ly = self.left_up_pos.y() + p.y()
        rx = self.right_down_pos.x() + p.x()
        ry = self.right_down_pos.y() + p.y()

        if lx < 0:
            lx = 0
            rx -= p.x()

        if ly < 0:
            ly = 0
            ry -= p.y()

        if rx > self.max_width:
            rx = self.max_width
            ry -= p.y()

        if ry > self.max_height:
            ry = self.max_height
            ly -= p.y()

        self.left_up_pos = QPoint(lx, ly)
        self.right_down_pos = QPoint(rx, ry)
        self.start_pos = self.left_up_pos
        self.end_pos = self.right_down_pos

    def cmp_point(self, left_top: QPoint, right_down: QPoint):
        l = left_top
        r = right_down

        if l.x() <= r.x():
            if l.y() <= r.y():
                pass
            else:

                left_top.setY(r.y())
                right_down.setY(l.y())
        else:
            if l.y() < r.y():
                left_top.setX(r.x())
                right_down.setX(l.x())
            else:
                self.left_up_pos = right_down
                self.right_down_pos = left_top
                # left_top, right_down = right_down, left_top


class ScreenWidget(QWidget):

    def __init__(self, parent):
        super().__init__(parent)
        self.menu = QMenu(self)
        self.screen = Screen(qApp.primaryScreen().geometry().size())
        self.full_screen = QPixmap()
        self.bg_screen = QPixmap()
        self.mov_pos = QPoint()
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.show_menu)

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        x = self.screen.get_left_up().x()
        y = self.screen.get_left_up().y()
        w = self.screen.get_right_down().x() - x
        h = self.screen.get_right_down().y() - y

        painter = QPainter(self)

        pen = QPen()
        pen.setColor(Qt.green)
        pen.setWidth(2)
        pen.setStyle(Qt.DotLine)
        painter.setPen(pen)
        painter.drawPixmap(0, 0, self.bg_screen)

        if w != 0 and h != 0:
            painter.drawPixmap(x, y, self.full_screen.copy(x, y, w, h))

        painter.drawRect(x, y, w, h)

        pen.setColor(Qt.white)
        painter.setPen(pen)
        painter.drawText(x + 2, y - 8, f'截图范围：({x} * {y}) - ({x + w} * {y + h}) 图片大小：({w} * {h})')

    def showEvent(self, a0: QtGui.QShowEvent) -> None:
        point = QPoint(-1, -1)
        self.screen.set_start(point)
        self.screen.set_end(point)

        p_screen = QApplication.primaryScreen()
        self.full_screen = p_screen.grabWindow(0, 0, 0, self.screen.width(), self.screen.height())
        pix = QPixmap(self.screen.width(), self.screen.height())
        pix.fill(QColor(10, 160, 160, 200))
        self.bg_screen = QPixmap(self.full_screen)
        p = QPainter(self.bg_screen)
        p.drawPixmap(0, 0, pix)
        self.setGeometry(0, 0, self.bg_screen.width(), self.screen.height())

    def save_screen(self):
        x = self.screen.get_left_up().x()
        y = self.screen.get_left_up().y()
        w = self.screen.get_right_down().x() - x
        h = self.screen.get_right_down().y() - y

        # filename = f'{qApp.applicationDirPath()}/screen_{now()}.png'
        filename = f'screenshot_{now()}.png'
        self.full_screen.copy(x, y, w, h).save(filename, 'png')
        self.close()

    def save_fullscreen(self):
        filename = f'screenshot_{now()}.png'
        self.full_screen.save(filename, 'png')
        self.close()

    def save_screen_other(self):
        name = f'screenshot_{now()}.png'
        filename = QFileDialog.getSaveFileName(self, '保存图片', name, 'png Files (*.png)')
        if filename[0] and not filename[0].endswith('.png'):
            filename += '.png'

        if filename[0]:
            x = self.screen.get_left_up().x()
            y = self.screen.get_left_up().y()
            w = self.screen.get_right_down().x() - x
            h = self.screen.get_right_down().y() - y
            self.full_screen.copy(x, y, w, h).save(filename[0], 'png')
            self.close()

    def save_full_other(self):
        name = f'screenshot_{now()}.png'
        filename = QFileDialog.getSaveFileName(self, "保存图片", name, "png Files (*.png)")

        if not filename[0].endswith('.png'):
            filename += '.png'

        if filename[0]:
            self.full_screen.save(filename[0], 'png')
            self.close()
        print('save full ')

    def mouseMoveEvent(self, e: QtGui.QMouseEvent) -> None:
        if self.screen.get_status() == STATUS.SELECT:
            self.screen.set_end(e.pos())
        elif self.screen.get_status() == STATUS.MOV:
            p = QPoint(e.x() - self.mov_pos.x(), e.y() - self.mov_pos.y())
            self.screen.move(p)
            self.mov_pos = e.pos()
        self.update()

    def mousePressEvent(self, e: QtGui.QMouseEvent) -> None:
        status = self.screen.get_status()
        if status == STATUS.SELECT:
            self.screen.set_start(e.pos())
        elif status == STATUS.MOV:
            if self.screen.is_in_area(e.pos()) is False:
                self.screen.set_start(e.pos())
                self.screen.set_status(STATUS.SELECT)
            else:
                self.mov_pos = e.pos()
                self.setCursor(Qt.SizeAllCursor)
        self.update()

    def mouseReleaseEvent(self, e: QtGui.QMouseEvent) -> None:
        if self.screen.get_status() == STATUS.SELECT:
            self.screen.set_status(STATUS.MOV)
        elif self.screen.get_status() == STATUS.MOV:
            self.setCursor(Qt.ArrowCursor)

    def show_menu(self, point):
        save_action = QAction('保存当前截图')
        self.menu.addAction(save_action)
        save_action.triggered.connect(self.save_screen)

        save_full_action = QAction('保存全屏截图')
        self.menu.addAction(save_full_action)
        save_full_action.triggered.connect(self.save_fullscreen)

        save_screen_other = QAction('截图另存为')
        self.menu.addAction(save_screen_other)
        save_screen_other.triggered.connect(self.save_screen_other)

        save_full_other = QAction('全屏另存为')
        self.menu.addAction(save_full_other)
        save_full_other.triggered.connect(self.save_full_other)

        exit_action = QAction('退出截图')
        self.menu.addAction(exit_action)
        exit_action.triggered.connect(self.hide)
        dest_point = self.mapToGlobal(point)
        self.menu.exec_(dest_point)
