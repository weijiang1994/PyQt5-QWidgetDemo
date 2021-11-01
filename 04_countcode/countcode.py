"""
# coding:utf-8
@Time    : 2021/11/01
@Author  : jiangwei
@File    : countcode.py
@Desc    : countcode
@Software: PyCharm
"""
from PyQt5.QtWidgets import QWidget, QAbstractItemView, QTableWidgetItem, QApplication
from PyQt5.QtGui import QFont
from PyQt5.Qt import QFileInfo, QDir, QFile, QTextStream, QFileDialog
from frmcountcode import Ui_frmCountCode
from PyQt5.Qt import Qt, qApp
import sys


class CountCode(QWidget, Ui_frmCountCode):
    def __init__(self):
        super(CountCode, self).__init__()
        self.setupUi(self)
        self.list_file = list()
        self.btnClear.clicked.connect(self.on_btn_clear_clicked)
        self.btnOpenFile.clicked.connect(self.on_btn_openfile_clicked)
        self.btnOpenPath.clicked.connect(self.on_btn_openpath_clicked)
        self.init_form()
        self.on_btn_clear_clicked()

    def init_form(self):
        head_text = ["文件名", "类型", "大小", "总行数", "代码行数", "注释行数", "空白行数", "路径"]
        column_width = [130, 50, 70, 80, 70, 70, 70, 150]
        column_count = len(head_text)
        self.tableWidget.setColumnCount(column_count)
        self.tableWidget.setHorizontalHeaderLabels(head_text)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(20)
        self.tableWidget.verticalHeader().setHighlightSections(False)

        for i in range(column_count):
            self.tableWidget.setColumnWidth(i, column_width[i])

        # 设置前景色
        self.txtCount.setStyleSheet('color: #17A086')
        self.txtSize.setStyleSheet("color:#CA5AA6;");
        self.txtRow.setStyleSheet("color:#CD1B19;");
        self.txtCode.setStyleSheet("color:#22A3A9;");
        self.txtNote.setStyleSheet("color:#D64D54;")
        self.txtBlank.setStyleSheet("color:#A279C5;")

        # 设置字体加粗
        font = QFont()
        font.setBold(True)
        if font.pointSize() > 0:
            font.setPointSize(font.pointSize() + 1)
        else:
            font.setPixelSize(font.pixelSize() + 2)

        self.txtCount.setFont(font)
        self.txtSize.setFont(font)
        self.txtRow.setFont(font)
        self.txtCount.setFont(font)
        self.txtNote.setFont(font)
        self.txtBlank.setFont(font)

        self.txtFilter.setPlaceholderText('中间空格隔开，例如*.h *.cpp *.c')

    def check_file(self, filename: str):
        if filename.startswith('moc_') or filename.startswith('ui_') or filename.startswith('qrc_'):
            return False
        file = QFileInfo(filename)
        suffix = '*.' + file.suffix()
        m_filter = self.txtFilter.text().strip()
        filters = m_filter.split(' ')
        return filters.__contains__(suffix)

    def count_code(self, filepath: str):
        m_dir = QDir(filepath)
        file_infos = m_dir.entryInfoList()
        print(file_infos)
        for file_info in file_infos:
            filename = file_info.fileName()
            if file_info.isFile():
                if self.check_file(filename):
                    self.list_file.append(file_info.filePath())
            else:
                if filename == '.' or filename == '..':
                    continue
                self.count_code(file_info.absoluteFilePath())

    def count_code_2(self, files: list):
        line_code = 0
        line_blank = 0
        line_notes = 0
        count = len(files)
        self.on_btn_clear_clicked()
        self.tableWidget.setRowCount(count)

        total_lines = 0
        total_bytes = 0
        total_codes = 0
        total_notes = 0
        total_blanks = 0

        for i in range(count):
            file_info = QFileInfo(files[i])
            line_code, line_notes, line_blank = self.calculate(file_info.filePath())
            line_all = line_code + line_blank + line_notes
            item_name = QTableWidgetItem()
            item_name.setText(file_info.fileName())

            item_suffix = QTableWidgetItem()
            item_suffix.setText(file_info.suffix())

            item_size = QTableWidgetItem()
            item_size.setText(str(file_info.size()))

            item_line = QTableWidgetItem()
            item_line.setText(str(line_all))

            item_code = QTableWidgetItem()
            item_code.setText(str(line_code))

            item_note = QTableWidgetItem()
            item_note.setText(str(line_notes))

            item_blank = QTableWidgetItem()
            item_blank.setText(str(line_blank))

            item_path = QTableWidgetItem()
            item_path.setText(file_info.filePath())

            item_suffix.setTextAlignment(Qt.AlignCenter)
            item_size.setTextAlignment(Qt.AlignCenter)
            item_line.setTextAlignment(Qt.AlignCenter)
            item_code.setTextAlignment(Qt.AlignCenter)
            item_note.setTextAlignment(Qt.AlignCenter)
            item_blank.setTextAlignment(Qt.AlignCenter)

            self.tableWidget.setItem(i, 0, item_name)
            self.tableWidget.setItem(i, 1, item_suffix)
            self.tableWidget.setItem(i, 2, item_size)
            self.tableWidget.setItem(i, 3, item_line)
            self.tableWidget.setItem(i, 4, item_code)
            self.tableWidget.setItem(i, 5, item_note)
            self.tableWidget.setItem(i, 6, item_blank)
            self.tableWidget.setItem(i, 7, item_path)

            total_bytes += file_info.size()
            total_lines += line_all
            total_codes += line_code
            total_notes += line_notes
            total_blanks += line_blank

            if i % 100 == 0:
                qApp.processEvents()

        self.list_file.clear()

        self.txtCount.setText(str(count))
        self.txtSize.setText(str(total_bytes))
        self.txtRow.setText(str(total_lines))
        self.txtCode.setText(str(total_codes))
        self.txtNote.setText(str(total_notes))
        self.txtBlank.setText(str(total_blanks))

        percent = float(total_codes) / float(total_lines) * 100
        self.labPercentCode.setText(str('%.2f' % percent + '%'))

        percent = float(total_notes) / float(total_lines) * 100
        self.labPercentNote.setText(str('%.2f' % percent + '%'))

        percent = float(total_blanks) / float(total_lines) * 100
        self.labPercentBlank.setText(str('%.2f' % percent + '%'))

    def calculate(
            self,
            filename: str,
            line_code: int = 0,
            line_blank: int = 0,
            line_notes: int = 0
    ):
        file = QFile(filename)
        if file.open(QFile.ReadOnly):
            out = QTextStream(file)
            is_note = False
            while not out.atEnd():
                line = out.readLine()

                if line.startswith(' '):
                    line.strip()

                if line.startswith('/*'):
                    is_note = True

                if is_note:
                    line_notes += 1
                else:
                    if line.startswith('//'):
                        line_notes += 1
                    elif line == '':
                        line_blank += 1
                    else:
                        line_code += 1
                if line.endswith('*/'):
                    is_note = False
        return line_code, line_notes, line_blank

    def on_btn_clear_clicked(self):
        self.txtCount.setText('0')
        self.txtSize.setText('0')
        self.txtRow.setText('0')

        self.txtCode.setText('0')
        self.txtNote.setText('0')
        self.txtBlank.setText('0')

        self.labPercentCode.setText('0')
        self.labPercentNote.setText('0')
        self.labPercentBlank.setText('0')
        self.tableWidget.setRowCount(0)

    def on_btn_openfile_clicked(self):
        m_filter = '代码文件(%s)' % self.txtFilter.text().strip()
        files = QFileDialog.getOpenFileNames(self, '选择文件', './', m_filter)
        if len(files[0]) > 0:
            self.txtFile.setText('|'.join(files[0]))
            self.count_code_2(files[0])

    def on_btn_openpath_clicked(self):
        path = QFileDialog.getExistingDirectory(self, '选择目录', './',
                                                QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks)
        print(path)
        if path:
            self.txtPath.setText(path)
            self.list_file.clear()
            self.count_code(path)
            self.count_code_2(self.list_file)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = CountCode()
    win.show()
    sys.exit(app.exec_())
