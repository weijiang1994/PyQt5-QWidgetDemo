"""
# coding:utf-8
@Time    : 2021/11/01
@Author  : jiangwei
@File    : flatui.py
@Desc    : flatui
@Software: PyCharm
"""
from PyQt5.QtWidgets import QWidget, QPushButton, QProgressBar, QLineEdit, QSlider, QRadioButton
from frmflatui import Ui_frmFlatUI


class FlatUI:

    def set_pushbutton_qss(
            self,
            btn: QPushButton,
            radius=5,
            padding=8,
            normal_color="#34495E",
            normal_text_color="#FFFFFF",
            hover_color="#4E6D8C",
            hover_text_color="#F0F0F0",
            pressed_color="#2D3E50",
            pressed_text_color="#B8C6D1"
    ):
        qss = list()
        qss.append(
            "QPushButton{border-style:none;padding:%spx;border-radius:%spx;color:%s;background:%s;}" % (
                padding, radius, normal_text_color, normal_color
            ))
        qss.append("QPushButton:hover{color:%s;background:%s;}" % (
            hover_text_color, hover_color
        ))
        qss.append("QPushButton:pressed{color:%s;background:%s;}" % (
            pressed_text_color, pressed_color
        ))
        qss = ' '.join(qss)
        btn.setStyleSheet(qss)
        return qss

    def set_lineedit_qss(
            self,
            txt: QLineEdit,
            radius=3,
            border_width=2,
            normal_color="#DCE4EC",
            focus_color="#34495E"
    ):
        qss = list()
        qss.append(
            "QLineEdit{border - style:none;padding:3px;border-radius:%spx;border:%spx solid %s;}" % (
                radius, border_width, normal_color))
        qss.append("QLineEdit:focus{border:%spx solid %s;}" % (border_width, focus_color))

        qss = ' '.join(qss)
        txt.setStyleSheet(qss)
        return qss

    def set_progress_qss(
            self,
            bar: QProgressBar,
            bar_height=0,
            bar_radius=5,
            font_size=9,
            normal_color="#E8EDF2",
            chunk_color="#E74C3C"
    ):
        qss = list()
        qss.append(
            "QProgressBar{font:%spt;background:%s;max-height:%spx;border-radius:%spx;text-align:center;border:1px solid %s;}" % (
                font_size, normal_color, bar_height, bar_radius, normal_color
            ))
        qss.append("QProgressBar:chunk{border-radius:%spx;background-color:%s;}" % (
            bar_radius, chunk_color
        ))
        qss = ' '.join(qss)
        bar.setStyleSheet(qss)
        return qss

    def set_slider_qss(
            self,
            slider: QSlider,
            slider_height=8,
            normal_color="#E8EDF2",
            groove_color="#1ABC9C",
            handle_border_color="#1ABC9C",
            handle_color="#FFFFFF"
    ):
        slider_radius = slider_height / 2
        handle_width = (slider_height * 3) / 2 + (slider_height / 5)
        handle_radius = handle_width / 2
        handle_offset = handle_radius / 2

        qss = list()
        qss.append("QSlider::horizontal{min-height:%spx;}" % (slider_height * 2))
        qss.append(
            "QSlider::groove:horizontal{background:%s;height:%spx;border-radius:%spx;}" % (
                normal_color, slider_height, slider_radius
            ))
        qss.append(
            "QSlider::add-page:horizontal{background:%s;height:%spx;border-radius:%spx;}" % (
                normal_color, slider_height, slider_radius
            ))
        qss.append(
            "QSlider::sub-page:horizontal{background:%s;height:%spx;border-radius:%spx;}" % (
                groove_color, slider_height, slider_radius
            ))
        qss.append(
            "QSlider::handle:horizontal{width:%spx;margin-top:-%spx;margin-bottom:-%spx;border-radius:%spx; background:qradialgradient(spread:pad,cx:0.5,cy:0.5,radius:0.5,fx:0.5,fy:0.5,stop:0.6 %s,stop:0.8 %s);}" % (
                handle_width, handle_offset, handle_offset, handle_radius, handle_color, handle_border_color
            ))

        handle_width = handle_width + 1
        qss.append("QSlider::vertical{min-width:%spx;}" % (slider_height * 2))
        qss.append(
            "QSlider::groove:vertical{background:%s;width:%spx;border-radius:%spx;}" % (
                normal_color, slider_height, slider_radius))
        qss.append(
            "QSlider::add-page:vertical{background:%s;width:%spx;border-radius:%spx;}" % (
                groove_color, slider_height, slider_radius))
        qss.append(
            "QSlider::sub-page:vertical{background:%s;width:%spx;border-radius:%spx;}" % (
                normal_color, slider_height, slider_radius))
        qss.append(
            "QSlider::handle:vertical{height:%spx;margin-left:-%spx;margin-right:-%spx;border-radius:%spx; background:qradialgradient(spread:pad,cx:0.5,cy:0.5,radius:0.5,fx:0.5,fy:0.5,stop:0.6 %s,stop:0.8 %s);}" % (
                handle_width, handle_offset, handle_offset, handle_radius, handle_color, handle_border_color
            ))

        qss = ' '.join(qss)
        slider.setStyleSheet(qss)
        return qss

    def set_radiobutton_qss(
            self,
            rbtn: QRadioButton,
            indicator_radius=8,
            normal_color="#D7DBDE",
            check_color="#34495E"
    ):
        indicator_width = indicator_radius * 2
        qss = list()
        qss.append(
            "QRadioButton::indicator{border-radius:%spx;width%spx;height:%spx;}" % (
                indicator_radius, indicator_width, indicator_width
            ))
        qss.append(
            "QRadioButton::indicator::unchecked{background:qradialgradient(spread:pad,cx:0.5,cy:0.5,radius:0.5,fx:0.5,fy:0.5,stop:0.6 #FFFFFF,stop:0.7 %s);}" % normal_color)
        qss.append(
            "QRadioButton::indicator::checked{background:qradialgradient(spread:pad,cx:0.5,cy:0.5,radius:0.5,fx:0.5,fy:0.5,stop:0 %s,stop:0.3 %s,stop:0.4 #FFFFFF,stop:0.6 #FFFFFF,stop:0.7 %s);}" % (
                check_color, check_color, check_color
            ))

        qss = ' '.join(qss)
        rbtn.setStyleSheet(qss)
        return qss

    def set_scrollbar_qss(
            self,
            scroll: QWidget,
            radius=6,
            min=120,
            max=12,
            bg_color="#606060",
            handle_normal_color="#34495E",
            handle_hover_color="#1ABC9C",
            handle_pressed_color="#E74C3C"
    ):
        padding = 0
        qss = list()
        qss.append(
            "QScrollBar:horizontal{background:%s;padding:%spx;border-radius:%spx;min-height:%spx;max-height:%spx;}" % (
                bg_color, padding, radius, max, max
            ))
        qss.append(
            "QScrollBar::handle:horizontal{background:%s;min-width:%spx;border-radius:%spx;}" % (
                handle_normal_color, min, radius
            ))
        qss.append("QScrollBar::handle:horizontal:hover{background:%s;}" % handle_hover_color)
        qss.append("QScrollBar::handle:horizontal:pressed{background:%s;}" % handle_pressed_color)
        qss.append("QScrollBar::add-page:horizontal{background:none;}")
        qss.append("QScrollBar::sub-page:horizontal{background:none;}")
        qss.append("QScrollBar::add-line:horizontal{background:none;}")
        qss.append("QScrollBar::sub-line:horizontal{background:none;}")

        # 纵向滚动条
        qss.append(
            "QScrollBar:vertical{background:%s;padding:%spx;border-radius:%spx;min-width:%spx;max-width:%spx;}" %(
                bg_color, padding, radius, max, max
            ))
        qss.append(
            "QScrollBar::handle:vertical{background:%s;min-height:%spx;border-radius:%spx;}" % (
                handle_normal_color, min, radius
            ))
        qss.append("QScrollBar::handle:vertical:hover{background:%s;}" % handle_hover_color)
        qss.append("QScrollBar::handle:vertical:pressed{background:%s;}" % handle_pressed_color)
        qss.append("QScrollBar::add-page:vertical{background:none;}")
        qss.append("QScrollBar::sub-page:vertical{background:none;}")
        qss.append("QScrollBar::add-line:vertical{background:none;}")
        qss.append("QScrollBar::sub-line:vertical{background:none;}")

        qss = ' '.join(qss)
        scroll.setStyleSheet(qss)
        return qss
