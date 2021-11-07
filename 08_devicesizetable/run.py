"""
coding:utf-8
file: run.py
@author: jiangwei
@contact: jiangwei_1994124@163.com
@time: 2021/11/7 22:36
@desc:
"""
from PyQt5.QtWidgets import QApplication
import sys
from devicesizetable import DeviceSizeTable

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = DeviceSizeTable()
    win.setWindowTitle('Device Size Table')
    win.show()
    sys.exit(app.exec_())
