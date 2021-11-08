"""
# coding:utf-8
@Time    : 2021/11/08
@Author  : jiangwei
@File    : colorwidget.py
@Desc    : colorwidget
@email   : qq804022023@gmail.com
@Software: PyCharm
"""
from PyQt5 import QtGui
from PyQt5.QtCore import Qt, QSize, QTimer
from PyQt5.QtGui import QFont, QCursor, QPixmap, QColor
from PyQt5.QtWidgets import qApp, QWidget, QGridLayout, QVBoxLayout, QLabel, QSizePolicy, QFrame, QLineEdit, \
    QApplication


class ColorWidget(QWidget):
    def __init__(self):
        super(ColorWidget, self).__init__()
        self.grid_layout = QGridLayout(self)
        self.grid_layout.setSpacing(6)
        self.grid_layout.setContentsMargins(11, 11, 11, 11)

        self.vertical_layout = QVBoxLayout()
        self.vertical_layout.setSpacing(0)

        self.label_color = QLabel(self)
        self.label_color.setText('')
        self.label_color.setStyleSheet("background-color: rgb(255, 107, 107);color: rgb(250, 250, 250);")
        self.label_color.setAlignment(Qt.AlignCenter)
        self.font = QFont()
        self.font.setPixelSize(35)
        self.font.setBold(True)
        self.label_color.setFont(self.font)

        self.size_policy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

        self.size_policy.setHorizontalStretch(0)
        self.size_policy.setVerticalStretch(0)
        self.size_policy.setHeightForWidth(self.label_color.sizePolicy().hasHeightForWidth())
        self.label_color.setSizePolicy(self.size_policy)
        self.label_color.setMinimumSize(QSize(80, 70))
        self.label_color.setMaximumSize(80, 70)
        self.label_color.setCursor(QCursor(Qt.CrossCursor))
        self.label_color.setFrameShape(QFrame.StyledPanel)
        self.label_color.setFrameShadow(QFrame.Sunken)

        self.vertical_layout.addWidget(self.label_color)

        self.label = QLabel(self)
        self.label.setMinimumSize(QSize(0, 18))
        self.label.setStyleSheet("background-color: rgb(0, 0, 0);color: rgb(200, 200, 200);")
        self.label.setAlignment(Qt.AlignCenter)

        self.vertical_layout.addWidget(self.label)
        self.grid_layout.addLayout(self.vertical_layout, 0, 0, 3, 1)

        self.lab_web = QLabel(self)
        self.grid_layout.addWidget(self.lab_web, 0, 1, 1, 1)

        self.txt_web = QLineEdit(self)
        self.grid_layout.addWidget(self.txt_web, 0, 2, 1, 1)

        self.lab_rgb = QLabel(self)
        self.grid_layout.addWidget(self.lab_rgb, 1, 1, 1, 1)

        self.txt_rgb = QLineEdit(self)
        self.grid_layout.addWidget(self.txt_rgb, 1, 2, 1, 1)

        self.lab_point = QLabel(self)
        self.grid_layout.addWidget(self.lab_point, 2, 1, 1, 1)

        self.txt_point = QLineEdit(self)
        self.grid_layout.addWidget(self.txt_point, 2, 2, 1, 1)

        self.label.setText('当前颜色')
        self.lab_web.setText('web值:')
        self.lab_rgb.setText('rgb值:')
        self.lab_point.setText('坐标值:')

        self.setLayout(self.grid_layout)
        self.setWindowTitle('屏幕拾色器')
        self.setFixedSize(300, 108)

        self.cp = QApplication.clipboard()
        self.pressed = False

        self.timer = QTimer(self)
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.show_color_value)
        self.timer.start()

    def mousePressEvent(self, e: QtGui.QMouseEvent) -> None:
        if self.label_color.rect().contains(e.pos()):
            self.pressed = True

    def mouseReleaseEvent(self, e: QtGui.QMouseEvent) -> None:
        self.pressed = False

    def show_color_value(self):
        if not self.pressed:
            return
        x = QCursor.pos().x()
        y = QCursor.pos().y()

        self.txt_point.setText("X:%s Y:%s" % (x, y))
        screen = qApp.primaryScreen()
        pixmap = screen.grabWindow(qApp.desktop().winId(), x, y, 2, 2)
        if not pixmap.isNull():
            image = pixmap.toImage()
            if not image.isNull():
                if image.valid(0, 0):
                    color = image.pixelColor(0, 0)
                    red = color.red()
                    green = color.green()
                    blue = color.blue()

                    str_decimal_value = '%s, %s, %s' % (red, green, blue)

                    color = QColor(red, green, blue)
                    hex_color = '%s%s%s' % (hex(red)[2:], hex(green)[2:], hex(blue)[2:])
                    gray = (0.299 * color.red() + 0.587 * color.green() + 0.114 * color.blue()) / 255
                    text_color = Qt.black if gray > 0.5 else Qt.white

                    qss = "background:rgb(%s);color:%s" % (str_decimal_value, text_color)
                    self.label_color.setStyleSheet(qss)
                    self.txt_rgb.setText(str_decimal_value)
                    self.txt_web.setText(hex_color.upper())


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    win = ColorWidget()
    win.show()
    sys.exit(app.exec_())
