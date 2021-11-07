"""
coding:utf-8
file: devicesizetable.py
@author: jiangwei
@contact: jiangwei_1994124@163.com
@time: 2021/11/6 23:11
@desc:
"""
import sys
from ctypes.wintypes import LPCWSTR

from PyQt5.QtCore import QProcess, QDir, Qt, QSize
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QWidget, QTableWidget, QAbstractItemView, QTableWidgetItem, QProgressBar
from win32api import GetDiskFreeSpaceEx

GB = 1024 * 1024 * 1024


class DeviceSizeTable(QTableWidget):

    def __init__(self):
        super().__init__()
        self.bg_color = QColor(255, 255, 255)
        self.chunk_color1 = QColor(100, 184, 255)
        self.chunk_color2 = QColor(24, 189, 155)
        self.chunk_color3 = QColor(255, 107, 107)

        self.text_color1 = QColor(10, 10, 10)
        self.text_color2 = QColor(255, 255, 255)
        self.text_color3 = QColor(255, 255, 255)

        self.process = QProcess(self)

        self.process.readyRead.connect(self.read_data)
        self.clear()

        # 设置列数和列宽
        self.setColumnCount(5)
        self.setColumnWidth(0, 100)
        self.setColumnWidth(1, 100)
        self.setColumnWidth(2, 100)
        self.setColumnWidth(3, 100)
        self.setColumnWidth(4, 100)

        self.setStyleSheet("QTableWidget::item{padding:0px;}")

        self.head_text = ["盘符", "已用空间", "可用空间", "总大小", "已用百分比"]

        self.setHorizontalHeaderLabels(self.head_text)
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setSelectionMode(QAbstractItemView.SingleSelection)
        self.verticalHeader().setVisible(True)
        self.horizontalHeader().setStretchLastSection(True)

        # TODO TIMER
        self.load()

    def get_bg_color(self):
        return self.bg_color

    def get_chunk_color1(self):
        return self.chunk_color1

    def get_chunk_color2(self):
        return self.chunk_color2

    def get_chunk_color3(self):
        return self.chunk_color3

    def get_text_color1(self):
        return self.text_color1

    def get_text_color2(self):
        return self.text_color2

    def get_text_color3(self):
        return self.text_color3

    def load(self):
        row = self.rowCount()
        for i in range(row):
            self.removeRow(0)

        if sys.platform.startswith('win'):
            drives = QDir.drives()
            for drive in drives:
                dir_name = drive.absolutePath()
                if GetDiskFreeSpaceEx(dir_name):
                    free, total = GetDiskFreeSpaceEx(dir_name)[0], GetDiskFreeSpaceEx(dir_name)[1]
                    use = total - free
                    percent = (use / total) * 100
                    free = '%.2fGB' % (free / GB)
                    use = '%.2fGB' % (use / GB)
                    total = '%.2fGB' % (total / GB)
                    self.insert_size(dir_name, use, free, total, percent)

    def set_bg_color(self, bg_color):
        if self.bg_color != bg_color:
            self.bg_color = bg_color
            self.load()

    def set_chunk_color1(self, chunk_color):
        if self.chunk_color1 != chunk_color:
            self.chunk_color1 = chunk_color
            self.load()

    def set_chunk_color2(self, chunk_color):
        if self.chunk_color2 != chunk_color:
            self.chunk_color2 = chunk_color
            self.load()

    def set_chunk_color3(self, chunk_color):
        if self.chunk_color3 != chunk_color:
            self.chunk_color3 = chunk_color
            self.load()

    def set_text_color1(self, text_color):
        if self.text_color1 != text_color:
            self.text_color1 = text_color
            self.load()

    def set_text_color2(self, text_color):
        if self.text_color2 != text_color:
            self.text_color2 = text_color
            self.load()

    def set_text_color3(self, text_color):
        if self.text_color3 != text_color:
            self.text_color3 = text_color
            self.load()

    def read_data(self):
        while not self.process.start():
            result = self.process.readLine()

    def check_size(self, result: str, name):
        dev, use, free, all = 0, 0, 0, 0
        percent = 0
        lists = result.split(' ')
        index = 0

        for i in range(len(lists)):
            s = i.strip()
            if s == '':
                continue
            index += 1

            if index == 1:
                dev = s
            elif index == 2:
                all = s
            elif index == 3:
                use = s
            elif index == 4:
                free = s
            elif index == 5:
                percent = int(s[len(s) - 1])
                break
        if len(name) > 0:
            dev = name
        self.insert_size(dev, use, free, all, percent)

    def insert_size(self, name, use, free, all, percent):
        row = self.rowCount()
        self.insertRow(row)

        item_name = QTableWidgetItem(name)
        item_use = QTableWidgetItem(use)
        item_use.setTextAlignment(Qt.AlignCenter)
        item_free = QTableWidgetItem(free)
        item_free.setTextAlignment(Qt.AlignCenter)
        item_all = QTableWidgetItem(all)
        item_all.setTextAlignment(Qt.AlignCenter)

        self.setItem(row, 0, item_name)
        self.setItem(row, 1, item_use)
        self.setItem(row, 2, item_free)
        self.setItem(row, 3, item_all)

        bar = QProgressBar()
        bar.setRange(0, 100)
        bar.setValue(percent)

        qss = "QProgressBar{background:%s;border-width:0px;border-radius:0px;text-align:center;}QProgressBar::chunk{" \
              "border-radius:0px;} " % self.bg_color.name()

        if percent < 50:
            qss += "QProgressBar{color:%s;}QProgressBar::chunk{background:%s;}" % (self.text_color1.name(),
                                                                                   self.chunk_color1.name())
        elif percent < 90:
            qss += "QProgressBar{color:%s;}QProgressBar::chunk{background:%s;}" % (self.text_color2.name(),
                                                                                   self.chunk_color2.name())
        else:
            qss += "QProgressBar{color:%s;}QProgressBar::chunk{background:%s;}" % (self.text_color3.name(),
                                                                                   self.chunk_color3.name())

        bar.setStyleSheet(qss)
        self.setCellWidget(row, 4, bar)

    def sizeHint(self) -> QSize:
        return QSize(500, 300)

    def minimumSizeHint(self) -> QSize:
        return QSize(200, 150)
