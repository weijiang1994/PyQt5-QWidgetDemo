"""
# coding:utf-8
@Time    : 2021/11/08
@Author  : jiangwei
@File    : run.py
@Desc    : run
@email   : qq804022023@gmail.com
@Software: PyCharm
"""
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QApplication
import sys
from imageswitch import ImageSwitch, ButtonStyle


class ImageSwitchWin(QWidget):
    def __init__(self):
        super(ImageSwitchWin, self).__init__()
        self.layout = QHBoxLayout()
        self.image_switch_btn1 = ImageSwitch()
        self.image_switch_btn2 = ImageSwitch()
        self.image_switch_btn3 = ImageSwitch()

        self.image_switch_btn1.set_checked(True)
        self.image_switch_btn2.set_checked(True)
        self.image_switch_btn3.set_checked(True)

        self.image_switch_btn1.setFixedSize(87, 28)
        self.image_switch_btn2.setFixedSize(87, 28)
        self.image_switch_btn3.setFixedSize(87, 28)

        self.image_switch_btn1.set_button_style(ButtonStyle.ButtonStyle_1)
        self.image_switch_btn2.set_button_style(ButtonStyle.ButtonStyle_2)
        self.image_switch_btn3.set_button_style(ButtonStyle.ButtonStyle_3)
        self.layout.addWidget(self.image_switch_btn1)
        self.layout.addWidget(self.image_switch_btn2)
        self.layout.addWidget(self.image_switch_btn3)
        self.setLayout(self.layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = ImageSwitchWin()
    win.setWindowTitle('Image Switch')
    win.show()
    sys.exit(app.exec_())
