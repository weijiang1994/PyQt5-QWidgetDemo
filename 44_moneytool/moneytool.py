"""
# coding:utf-8
@Time    : 2021/11/12
@Author  : jiangwei
@File    : moneytool.py
@Desc    : moneytool
@email   : qq804022023@gmail.com
@Software: PyCharm
"""
import sys

from widget import Ui_Widget
from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox


class MoneyTool(QWidget, Ui_Widget):
    def __init__(self):
        super(MoneyTool, self).__init__()
        self.setupUi(self)
        self.btnOk.clicked.connect(self.calculate)

    def calculate(self):
        current_money = int(self.txtMoneyCurrent.text())
        rate = float(self.txtRate.text())
        year = int(self.cboxYear.currentText()[0])
        years = int(self.txtYears.text())

        if years % year != 0:
            self.txtYears.setFocus()
            QMessageBox.critical(self, '错误', '总年费必须是期限的整数倍数!')
            return
        if self.cboxType.currentIndex() == 0:
            all_money = current_money + (current_money * rate * years)
        else:
            count = int(years / year)
            for i in range(count):
                current_money = current_money + (current_money * rate * year)
            all_money = current_money
        self.txtMoneyAll.setText(str(all_money))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MoneyTool()
    win.setWindowTitle('存款计算器')
    win.show()
    sys.exit(app.exec_())
