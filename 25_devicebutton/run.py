"""
# coding:utf-8
@Time    : 2021/11/09
@Author  : jiangwei
@File    : run.py
@Desc    : run
@email   : qq804022023@gmail.com
@Software: PyCharm
"""
from devicebutton import DeviceButton, ButtonColor, ButtonStyle
from frmdevicebutton import Ui_frmDeviceButton
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
import sys


class DeviceButtonWin(Ui_frmDeviceButton, QWidget):
    def __init__(self):
        super(DeviceButtonWin, self).__init__()
        self.setupUi(self)

        self.btn_color_text = [self.btnGreen.text(),
                               self.btnBlue.text(),
                               self.btnRed.text(),
                               self.btnGray.text(),
                               self.btnBlack.text(),
                               self.btnPurple.text(),
                               self.btnYellow.text()]

        self.btn_style_text = [self.btnCircle.text(),
                               self.btnPolice.text(),
                               self.btnBubble.text(),
                               self.btnBubble2.text(),
                               self.btnMsg.text(),
                               self.btnMsg2.text()]
        self.init_form()

    def init_form(self):
        self.labMap.setStyleSheet("border-image:url(image/bg_call.jpg);")

        self.btn1 = DeviceButton(self.labMap)
        self.btn1.set_text('#1')
        self.btn1.setGeometry(5, 5, 35, 35)

        self.btn2 = DeviceButton(self.labMap)
        self.btn2.set_text('#2')
        self.btn2.setGeometry(45, 5, 35, 35)

        self.btn3 = DeviceButton(self.labMap)
        self.btn3.set_text('#3')
        self.btn3.setGeometry(85, 5, 35, 35)

        self.btnCircle.clicked.connect(lambda: self.change_style(self.btnCircle.text()))
        self.btnPolice.clicked.connect(lambda: self.change_style(self.btnPolice.text()))
        self.btnBubble.clicked.connect(lambda: self.change_style(self.btnBubble.text()))
        self.btnBubble2.clicked.connect(lambda: self.change_style(self.btnBubble2.text()))
        self.btnMsg.clicked.connect(lambda: self.change_style(self.btnMsg.text()))
        self.btnMsg2.clicked.connect(lambda: self.change_style(self.btnMsg2.text()))

        self.btnGreen.clicked.connect(lambda: self.change_color(self.btnGreen.text()))
        self.btnBlue.clicked.connect(lambda: self.change_color(self.btnBlue.text()))
        self.btnRed.clicked.connect(lambda: self.change_color(self.btnRed.text()))
        self.btnGray.clicked.connect(lambda: self.change_color(self.btnGray.text()))
        self.btnBlack.clicked.connect(lambda: self.change_color(self.btnBlack.text()))
        self.btnPurple.clicked.connect(lambda: self.change_color(self.btnPurple.text()))
        self.btnYellow.clicked.connect(lambda: self.change_color(self.btnYellow.text()))

        self.ckCanMove.clicked.connect(self.set_can_move)

    def set_can_move(self):
        if self.ckCanMove.isChecked():
            self.btn1.set_can_move(True)
            self.btn2.set_can_move(True)
            self.btn3.set_can_move(True)
        else:
            self.btn1.set_can_move(False)
            self.btn2.set_can_move(False)
            self.btn3.set_can_move(False)

    def change_color(self, text):
        index = self.btn_color_text.index(text)
        style = ButtonColor(index)
        self.btn1.set_button_color(style)
        self.btn2.set_button_color(style)
        self.btn3.set_button_color(style)

    def change_style(self, text):
        index = self.btn_style_text.index(text)
        style = ButtonStyle(index)
        self.btn1.set_button_style(style)
        self.btn2.set_button_style(style)
        self.btn3.set_button_style(style)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = DeviceButtonWin()
    win.setWindowTitle('Device Button')
    win.show()
    sys.exit(app.exec_())
