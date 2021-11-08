"""
# coding:utf-8
@Time    : 2021/11/08
@Author  : jiangwei
@File    : run.py
@Desc    : run
@email   : qq804022023@gmail.com
@Software: PyCharm
"""
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget, QSlider
import sys
from battery import Battery
from PyQt5.QtCore import Qt


class BatteryWin(QWidget):
    def __init__(self):
        super(BatteryWin, self).__init__()
        self.bar = QSlider()
        self.bar.setOrientation(Qt.Horizontal)
        self.v_layout = QVBoxLayout()
        self.battery = Battery()
        self.v_layout.addWidget(self.battery)
        self.v_layout.addWidget(self.bar)
        self.setLayout(self.v_layout)
        self.bar.valueChanged.connect(self.battery.set_value)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = BatteryWin()
    win.setMinimumSize(250, 103)
    win.setWindowTitle('Battery')
    win.show()
    sys.exit(app.exec_())
