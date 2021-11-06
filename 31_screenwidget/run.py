"""
# coding:utf-8
@Time    : 2021/11/05
@Author  : jiangwei
@File    : run.py
@Desc    : run
@email   : qq804022023@gmail.com
@Software: PyCharm
"""
from PyQt5.QtWidgets import QWidget, QApplication
import sys

from frmscreenwidget import Ui_frmScreenWidget
from screenwidget import ScreenWidget


class ScreenWidgetWin(Ui_frmScreenWidget, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.start_grab)

    def start_grab(self):
        self.screen_widget = ScreenWidget(self)
        self.screen_widget.showFullScreen()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = ScreenWidgetWin()
    win.setWindowTitle('ScreenShot')
    win.show()
    sys.exit(app.exec_())
