"""
# coding:utf-8
@Time    : 2021/11/12
@Author  : jiangwei
@File    : hotkey.py
@Desc    : hotkey
@email   : qq804022023@gmail.com
@Software: PyCharm
"""
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout
from PyQt5.QtCore import pyqtSignal, Qt
from system_hotkey import SystemHotkey
import sys


class HotKey(QWidget):
    hotkey_down = pyqtSignal(str)

    def __init__(self):
        super(HotKey, self).__init__()
        self.hot_key = SystemHotkey()
        self.hot_key.register(('control', 'x'), callback=lambda x: self.do_hotkey('Send'))
        self.label = QLabel('按Ctrl+x最小化窗口')
        self.lay = QVBoxLayout()
        self.lay.setAlignment(Qt.AlignHCenter)
        self.lay.addWidget(self.label)
        self.setLayout(self.lay)
        self.hotkey_down.connect(self.action)

    def do_hotkey(self, send):
        self.hotkey_down.emit(send)

    def action(self, send):
        if self.isMinimized():
            self.showNormal()
            self.activateWindow()
        else:
            self.showMinimized()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = HotKey()
    win.setMinimumSize(200, 150)
    win.setWindowTitle('HotKey')
    win.show()
    sys.exit(app.exec_())
