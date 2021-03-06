from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

import files_rc
import files_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 720)
        MainWindow.setMinimumSize(QSize(1000, 720))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(66, 73, 90, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(55, 61, 75, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(22, 24, 30, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(29, 32, 40, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        brush6 = QBrush(QColor(210, 210, 210, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush7 = QBrush(QColor(0, 0, 0, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush7)
        brush8 = QBrush(QColor(85, 170, 255, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush8)
        palette.setBrush(QPalette.Active, QPalette.Link, brush8)
        brush9 = QBrush(QColor(255, 0, 127, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush4)
        brush10 = QBrush(QColor(44, 49, 60, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
        brush11 = QBrush(QColor(210, 210, 210, 128))
        brush11.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush11)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.Link, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
        brush12 = QBrush(QColor(210, 210, 210, 128))
        brush12.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush7)
        brush13 = QBrush(QColor(51, 153, 255, 255))
        brush13.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Highlight, brush13)
        palette.setBrush(QPalette.Disabled, QPalette.Link, brush8)
        palette.setBrush(QPalette.Disabled, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
        brush14 = QBrush(QColor(210, 210, 210, 128))
        brush14.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush14)
#endif
        MainWindow.setPalette(palette)
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"QMainWindow {background: transparent; }\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(27, 29, 35, 160);\n"
"	border: 1px solid rgb(40, 40, 40);\n"
"	border-radius: 2px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background: transparent;\n"
"color: rgb(210, 210, 210);")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.frame_main = QFrame(self.centralwidget)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setStyleSheet(u"/* LINE EDIT */\n"
"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* SCROLL BARS */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(85, 170, 255);\n"
"    min-width: 25px;\n"
"	border-radius: 7px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
""
                        "	border-top-left-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(85, 170, 255);\n"
"    min-height: 25px;\n"
"	border-radius: 7px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63"
                        ", 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* CHECKBOX */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	background-image: url(:/16x16/icons/16x16/cil-check-alt.png);\n"
"}\n"
"\n"
"/* RADIO BUTTON */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius"
                        ": 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* COMBOBOX */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb("
                        "85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* SLIDERS */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 9px;\n"
"    height: 18px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 9px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:verti"
                        "cal {\n"
"    background-color: rgb(85, 170, 255);\n"
"	border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"")
        self.frame_main.setFrameShape(QFrame.NoFrame)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_main)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_top = QFrame(self.frame_main)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMinimumSize(QSize(0, 65))
        self.frame_top.setMaximumSize(QSize(16777215, 65))
        self.frame_top.setStyleSheet(u"background-color: transparent;")
        self.frame_top.setFrameShape(QFrame.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_top)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.frame_top)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMaximumSize(QSize(70, 16777215))
        self.frame_toggle.setStyleSheet(u"background-color: rgb(27, 29, 35);")
        self.frame_toggle.setFrameShape(QFrame.NoFrame)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_toggle_menu = QPushButton(self.frame_toggle)
        self.btn_toggle_menu.setObjectName(u"btn_toggle_menu")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_toggle_menu.sizePolicy().hasHeightForWidth())
        self.btn_toggle_menu.setSizePolicy(sizePolicy)
        self.btn_toggle_menu.setStyleSheet(u"QPushButton {\n"
"	background-image: url(:/24x24/icons/24x24/cil-menu.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"	border: none;\n"
"	background-color: rgb(27, 29, 35);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_toggle_menu)


        self.horizontalLayout_3.addWidget(self.frame_toggle)

        self.frame_top_right = QFrame(self.frame_top)
        self.frame_top_right.setObjectName(u"frame_top_right")
        self.frame_top_right.setStyleSheet(u"background: transparent;")
        self.frame_top_right.setFrameShape(QFrame.NoFrame)
        self.frame_top_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_top_right)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_top_btns = QFrame(self.frame_top_right)
        self.frame_top_btns.setObjectName(u"frame_top_btns")
        self.frame_top_btns.setMaximumSize(QSize(16777215, 42))
        self.frame_top_btns.setStyleSheet(u"background-color: rgba(27, 29, 35, 200)")
        self.frame_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_top_btns)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_label_top_btns = QFrame(self.frame_top_btns)
        self.frame_label_top_btns.setObjectName(u"frame_label_top_btns")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_label_top_btns.sizePolicy().hasHeightForWidth())
        self.frame_label_top_btns.setSizePolicy(sizePolicy1)
        self.frame_label_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_label_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_label_top_btns)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(5, 0, 10, 0)
        self.frame_icon_top_bar = QFrame(self.frame_label_top_btns)
        self.frame_icon_top_bar.setObjectName(u"frame_icon_top_bar")
        self.frame_icon_top_bar.setMaximumSize(QSize(30, 30))
        self.frame_icon_top_bar.setStyleSheet(u"background: transparent;\n"
"\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"")
        self.frame_icon_top_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_icon_top_bar.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_10.addWidget(self.frame_icon_top_bar)

        self.label_title_bar_top = QLabel(self.frame_label_top_btns)
        self.label_title_bar_top.setObjectName(u"label_title_bar_top")
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_title_bar_top.setFont(font1)
        self.label_title_bar_top.setStyleSheet(u"background: transparent;\n"
"")

        self.horizontalLayout_10.addWidget(self.label_title_bar_top)


        self.horizontalLayout_4.addWidget(self.frame_label_top_btns)

        self.frame_btns_right = QFrame(self.frame_top_btns)
        self.frame_btns_right.setObjectName(u"frame_btns_right")
        sizePolicy1.setHeightForWidth(self.frame_btns_right.sizePolicy().hasHeightForWidth())
        self.frame_btns_right.setSizePolicy(sizePolicy1)
        self.frame_btns_right.setMaximumSize(QSize(120, 16777215))
        self.frame_btns_right.setFrameShape(QFrame.NoFrame)
        self.frame_btns_right.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_btns_right)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btn_minimize = QPushButton(self.frame_btns_right)
        self.btn_minimize.setObjectName(u"btn_minimize")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_minimize.sizePolicy().hasHeightForWidth())
        self.btn_minimize.setSizePolicy(sizePolicy2)
        self.btn_minimize.setMinimumSize(QSize(40, 0))
        self.btn_minimize.setMaximumSize(QSize(40, 16777215))
        self.btn_minimize.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/16x16/icons/16x16/cil-window-minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_minimize.setIcon(icon)

        self.horizontalLayout_5.addWidget(self.btn_minimize)

        self.btn_maximize_restore = QPushButton(self.frame_btns_right)
        self.btn_maximize_restore.setObjectName(u"btn_maximize_restore")
        sizePolicy2.setHeightForWidth(self.btn_maximize_restore.sizePolicy().hasHeightForWidth())
        self.btn_maximize_restore.setSizePolicy(sizePolicy2)
        self.btn_maximize_restore.setMinimumSize(QSize(40, 0))
        self.btn_maximize_restore.setMaximumSize(QSize(40, 16777215))
        self.btn_maximize_restore.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/16x16/icons/16x16/cil-window-maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_maximize_restore.setIcon(icon1)

        self.horizontalLayout_5.addWidget(self.btn_maximize_restore)

        self.btn_close = QPushButton(self.frame_btns_right)
        self.btn_close.setObjectName(u"btn_close")
        sizePolicy2.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy2)
        self.btn_close.setMinimumSize(QSize(40, 0))
        self.btn_close.setMaximumSize(QSize(40, 16777215))
        self.btn_close.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 53, 53);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(255, 53, 53);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/16x16/icons/16x16/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon2)

        self.horizontalLayout_5.addWidget(self.btn_close)


        self.horizontalLayout_4.addWidget(self.frame_btns_right, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.frame_top_btns)

        self.frame_top_info = QFrame(self.frame_top_right)
        self.frame_top_info.setObjectName(u"frame_top_info")
        self.frame_top_info.setMaximumSize(QSize(16777215, 65))
        self.frame_top_info.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.frame_top_info.setFrameShape(QFrame.NoFrame)
        self.frame_top_info.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_top_info)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(10, 0, 10, 0)
        self.label_top_info_2 = QLabel(self.frame_top_info)
        self.label_top_info_2.setObjectName(u"label_top_info_2")
        self.label_top_info_2.setMaximumSize(QSize(16777215, 15))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        self.label_top_info_2.setFont(font2)
        self.label_top_info_2.setStyleSheet(u"color: rgb(98, 103, 111); ")

        self.horizontalLayout_8.addWidget(self.label_top_info_2)


        self.verticalLayout_2.addWidget(self.frame_top_info)


        self.horizontalLayout_3.addWidget(self.frame_top_right)


        self.verticalLayout.addWidget(self.frame_top)

        self.frame_center = QFrame(self.frame_main)
        self.frame_center.setObjectName(u"frame_center")
        sizePolicy.setHeightForWidth(self.frame_center.sizePolicy().hasHeightForWidth())
        self.frame_center.setSizePolicy(sizePolicy)
        self.frame_center.setStyleSheet(u"background-color: rgb(40, 44, 52);")
        self.frame_center.setFrameShape(QFrame.NoFrame)
        self.frame_center.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_center)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.frame_center)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_left_menu.sizePolicy().hasHeightForWidth())
        self.frame_left_menu.setSizePolicy(sizePolicy3)
        self.frame_left_menu.setMinimumSize(QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setLayoutDirection(Qt.LeftToRight)
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(27, 29, 35);")
        self.frame_left_menu.setFrameShape(QFrame.NoFrame)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_5.setSpacing(1)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_menus = QFrame(self.frame_left_menu)
        self.frame_menus.setObjectName(u"frame_menus")
        self.frame_menus.setFrameShape(QFrame.NoFrame)
        self.frame_menus.setFrameShadow(QFrame.Raised)
        self.layout_menus = QVBoxLayout(self.frame_menus)
        self.layout_menus.setSpacing(0)
        self.layout_menus.setObjectName(u"layout_menus")
        self.layout_menus.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_5.addWidget(self.frame_menus, 0, Qt.AlignTop)

        self.frame_extra_menus = QFrame(self.frame_left_menu)
        self.frame_extra_menus.setObjectName(u"frame_extra_menus")
        sizePolicy3.setHeightForWidth(self.frame_extra_menus.sizePolicy().hasHeightForWidth())
        self.frame_extra_menus.setSizePolicy(sizePolicy3)
        self.frame_extra_menus.setFrameShape(QFrame.NoFrame)
        self.frame_extra_menus.setFrameShadow(QFrame.Raised)
        self.layout_menu_bottom = QVBoxLayout(self.frame_extra_menus)
        self.layout_menu_bottom.setSpacing(10)
        self.layout_menu_bottom.setObjectName(u"layout_menu_bottom")
        self.layout_menu_bottom.setContentsMargins(0, 0, 0, 25)

        self.verticalLayout_5.addWidget(self.frame_extra_menus, 0, Qt.AlignBottom)


        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_content_right = QFrame(self.frame_center)
        self.frame_content_right.setObjectName(u"frame_content_right")
        self.frame_content_right.setStyleSheet(u"background-color: rgb(44, 49, 60);")
        self.frame_content_right.setFrameShape(QFrame.NoFrame)
        self.frame_content_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_content_right)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_content = QFrame(self.frame_content_right)
        self.frame_content.setObjectName(u"frame_content")
        self.frame_content.setFrameShape(QFrame.NoFrame)
        self.frame_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_content)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(5, 5, 5, 5)
        self.stackedWidget = QStackedWidget(self.frame_content)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy4)
        self.stackedWidget.setMinimumSize(QSize(0, 100))
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.FrenchCoursePage = QWidget()
        self.FrenchCoursePage.setObjectName(u"FrenchCoursePage")
        self.Level_Basic1 = QPushButton(self.FrenchCoursePage)
        self.Level_Basic1.setObjectName(u"Level_Basic1")
        self.Level_Basic1.setGeometry(QRect(10, 10, 131, 121))
        font3 = QFont()
        font3.setPointSize(30)
        self.Level_Basic1.setFont(font3)
        self.Level_Basic1.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 10px;	\n"
"	 background: #3399ff;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #2b82d9;\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.Level_Basic1.setFlat(False)
        self.Level_Basic2 = QPushButton(self.FrenchCoursePage)
        self.Level_Basic2.setObjectName(u"Level_Basic2")
        self.Level_Basic2.setGeometry(QRect(150, 10, 131, 121))
        self.Level_Basic2.setFont(font3)
        self.Level_Basic2.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 10px;	\n"
"	 background: #3399ff;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #2b82d9;\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.Level_Basic2.setFlat(False)
        self.stackedWidget.addWidget(self.FrenchCoursePage)
        self.SpanishCoursePage = QWidget()
        self.SpanishCoursePage.setObjectName(u"SpanishCoursePage")
        self.gridLayout_8 = QGridLayout(self.SpanishCoursePage)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.frame_6 = QFrame(self.SpanishCoursePage)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.Level_Basic1_Spanish = QPushButton(self.frame_6)
        self.Level_Basic1_Spanish.setObjectName(u"Level_Basic1_Spanish")
        self.Level_Basic1_Spanish.setGeometry(QRect(0, 0, 131, 121))
        self.Level_Basic1_Spanish.setFont(font3)
        self.Level_Basic1_Spanish.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 10px;	\n"
"	 background: #3399ff;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #2b82d9;\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.Level_Basic1_Spanish.setFlat(False)
        self.Level_Basic2_Spanish = QPushButton(self.frame_6)
        self.Level_Basic2_Spanish.setObjectName(u"Level_Basic2_Spanish")
        self.Level_Basic2_Spanish.setGeometry(QRect(140, 0, 131, 121))
        self.Level_Basic2_Spanish.setFont(font3)
        self.Level_Basic2_Spanish.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 10px;	\n"
"	 background: #3399ff;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #2b82d9;\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.Level_Basic2_Spanish.setFlat(False)

        self.gridLayout_8.addWidget(self.frame_6, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.SpanishCoursePage)
        self.ItalianCoursePage = QWidget()
        self.ItalianCoursePage.setObjectName(u"ItalianCoursePage")
        self.gridLayout_13 = QGridLayout(self.ItalianCoursePage)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.frame_11 = QFrame(self.ItalianCoursePage)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.Level_Basic2_Italian = QPushButton(self.frame_11)
        self.Level_Basic2_Italian.setObjectName(u"Level_Basic2_Italian")
        self.Level_Basic2_Italian.setGeometry(QRect(140, 0, 131, 121))
        self.Level_Basic2_Italian.setFont(font3)
        self.Level_Basic2_Italian.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 10px;	\n"
"	 background: #3399ff;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #2b82d9;\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.Level_Basic2_Italian.setFlat(False)
        self.Level_Basic1_Italian = QPushButton(self.frame_11)
        self.Level_Basic1_Italian.setObjectName(u"Level_Basic1_Italian")
        self.Level_Basic1_Italian.setGeometry(QRect(0, 0, 131, 121))
        self.Level_Basic1_Italian.setFont(font3)
        self.Level_Basic1_Italian.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 10px;	\n"
"	 background: #3399ff;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #2b82d9;\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.Level_Basic1_Italian.setFlat(False)

        self.gridLayout_13.addWidget(self.frame_11, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.ItalianCoursePage)
        self.Basic1_French = QWidget()
        self.Basic1_French.setObjectName(u"Basic1_French")
        self.formLayout_3 = QFormLayout(self.Basic1_French)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.Basic1FrenchFrame_1 = QFrame(self.Basic1_French)
        self.Basic1FrenchFrame_1.setObjectName(u"Basic1FrenchFrame_1")
        self.Basic1FrenchFrame_1.setFrameShape(QFrame.StyledPanel)
        self.Basic1FrenchFrame_1.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.Basic1FrenchFrame_1)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_7 = QLabel(self.Basic1FrenchFrame_1)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font3)

        self.gridLayout_4.addWidget(self.label_7, 0, 0, 1, 1)

        self.Basic1French_StackedWidget = QStackedWidget(self.Basic1FrenchFrame_1)
        self.Basic1French_StackedWidget.setObjectName(u"Basic1French_StackedWidget")
        self.Basic1French_StackedWidget.setMaximumSize(QSize(1000, 450))
        self.Basic1French_Page1 = QWidget()
        self.Basic1French_Page1.setObjectName(u"Basic1French_Page1")
        self.formLayout_2 = QFormLayout(self.Basic1French_Page1)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_9 = QLabel(self.Basic1French_Page1)
        self.label_9.setObjectName(u"label_9")
        font4 = QFont()
        font4.setPointSize(15)
        self.label_9.setFont(font4)
        self.label_9.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.formLayout_2.setWidget(0, QFormLayout.SpanningRole, self.label_9)

        self.Basic1French_StackedWidget.addWidget(self.Basic1French_Page1)
        self.Basic1French_Page2 = QWidget()
        self.Basic1French_Page2.setObjectName(u"Basic1French_Page2")
        self.formLayout_4 = QFormLayout(self.Basic1French_Page2)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.label_8 = QLabel(self.Basic1French_Page2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font4)
        self.label_8.setStyleSheet(u"text-color= white;")

        self.formLayout_4.setWidget(0, QFormLayout.SpanningRole, self.label_8)

        self.Basic1French_StackedWidget.addWidget(self.Basic1French_Page2)
        self.Basic1French_Page3 = QWidget()
        self.Basic1French_Page3.setObjectName(u"Basic1French_Page3")
        self.formLayout_5 = QFormLayout(self.Basic1French_Page3)
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.label_10 = QLabel(self.Basic1French_Page3)
        self.label_10.setObjectName(u"label_10")

        self.formLayout_5.setWidget(0, QFormLayout.SpanningRole, self.label_10)

        self.Basic1French_StackedWidget.addWidget(self.Basic1French_Page3)

        self.gridLayout_4.addWidget(self.Basic1French_StackedWidget, 1, 0, 1, 1)

        self.frame_4 = QFrame(self.Basic1FrenchFrame_1)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.Basic1FrenchNavButtonLeft = QPushButton(self.frame_4)
        self.Basic1FrenchNavButtonLeft.setObjectName(u"Basic1FrenchNavButtonLeft")
        font5 = QFont()
        font5.setPointSize(24)
        font5.setBold(True)
        font5.setWeight(75)
        self.Basic1FrenchNavButtonLeft.setFont(font5)
        self.Basic1FrenchNavButtonLeft.setLayoutDirection(Qt.LeftToRight)
        self.Basic1FrenchNavButtonLeft.setStyleSheet(u"\n"
"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 10px;	\n"
"	background: #3399ff;\n"
"	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #2b82d9;\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")

        self.gridLayout_5.addWidget(self.Basic1FrenchNavButtonLeft, 0, 0, 1, 1)

        self.Basic1FrenchNavButtonRight = QPushButton(self.frame_4)
        self.Basic1FrenchNavButtonRight.setObjectName(u"Basic1FrenchNavButtonRight")
        self.Basic1FrenchNavButtonRight.setFont(font5)
        self.Basic1FrenchNavButtonRight.setStyleSheet(u"\n"
"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 10px;	\n"
"	background: #3399ff;\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #2b82d9;\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")

        self.gridLayout_5.addWidget(self.Basic1FrenchNavButtonRight, 0, 1, 1, 1)


        self.gridLayout_4.addWidget(self.frame_4, 2, 0, 1, 1)


        self.formLayout_3.setWidget(0, QFormLayout.SpanningRole, self.Basic1FrenchFrame_1)

        self.stackedWidget.addWidget(self.Basic1_French)
        self.Basic2_French = QWidget()
        self.Basic2_French.setObjectName(u"Basic2_French")
        self.formLayout_6 = QFormLayout(self.Basic2_French)
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.Basic2FrenchFrame_1 = QFrame(self.Basic2_French)
        self.Basic2FrenchFrame_1.setObjectName(u"Basic2FrenchFrame_1")
        self.Basic2FrenchFrame_1.setFrameShape(QFrame.StyledPanel)
        self.Basic2FrenchFrame_1.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.Basic2FrenchFrame_1)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_14 = QLabel(self.Basic2FrenchFrame_1)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font3)

        self.gridLayout_7.addWidget(self.label_14, 0, 0, 1, 1)

        self.frame_5 = QFrame(self.Basic2FrenchFrame_1)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_5)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.Basic2FrenchNavButtonLeft = QPushButton(self.frame_5)
        self.Basic2FrenchNavButtonLeft.setObjectName(u"Basic2FrenchNavButtonLeft")
        self.Basic2FrenchNavButtonLeft.setFont(font5)
        self.Basic2FrenchNavButtonLeft.setLayoutDirection(Qt.LeftToRight)
        self.Basic2FrenchNavButtonLeft.setStyleSheet(u"\n"
"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 10px;	\n"
"	background: #3399ff;\n"
"	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #2b82d9;\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")

        self.gridLayout_6.addWidget(self.Basic2FrenchNavButtonLeft, 0, 0, 1, 1)

        self.Basic2FrenchNavButtonRight = QPushButton(self.frame_5)
        self.Basic2FrenchNavButtonRight.setObjectName(u"Basic2FrenchNavButtonRight")
        self.Basic2FrenchNavButtonRight.setFont(font5)
        self.Basic2FrenchNavButtonRight.setStyleSheet(u"\n"
"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 10px;	\n"
"	background: #3399ff;\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #2b82d9;\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")

        self.gridLayout_6.addWidget(self.Basic2FrenchNavButtonRight, 0, 1, 1, 1)


        self.gridLayout_7.addWidget(self.frame_5, 2, 0, 1, 1)

        self.Basic2French_StackedWidget = QStackedWidget(self.Basic2FrenchFrame_1)
        self.Basic2French_StackedWidget.setObjectName(u"Basic2French_StackedWidget")
        self.Basic2French_StackedWidget.setMaximumSize(QSize(1000, 450))
        self.Basic2French_Page1 = QWidget()
        self.Basic2French_Page1.setObjectName(u"Basic2French_Page1")
        self.formLayout_7 = QFormLayout(self.Basic2French_Page1)
        self.formLayout_7.setObjectName(u"formLayout_7")
        self.label_11 = QLabel(self.Basic2French_Page1)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font4)
        self.label_11.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.formLayout_7.setWidget(0, QFormLayout.SpanningRole, self.label_11)

        self.Basic2French_StackedWidget.addWidget(self.Basic2French_Page1)
        self.Basic2French_Page2 = QWidget()
        self.Basic2French_Page2.setObjectName(u"Basic2French_Page2")
        self.formLayout_8 = QFormLayout(self.Basic2French_Page2)
        self.formLayout_8.setObjectName(u"formLayout_8")
        self.label_12 = QLabel(self.Basic2French_Page2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font4)
        self.label_12.setStyleSheet(u"text-color= white;")

        self.formLayout_8.setWidget(0, QFormLayout.SpanningRole, self.label_12)

        self.Basic2French_StackedWidget.addWidget(self.Basic2French_Page2)

        self.gridLayout_7.addWidget(self.Basic2French_StackedWidget, 1, 0, 1, 1)


        self.formLayout_6.setWidget(0, QFormLayout.FieldRole, self.Basic2FrenchFrame_1)

        self.stackedWidget.addWidget(self.Basic2_French)
        self.Basic1_Spanish = QWidget()
        self.Basic1_Spanish.setObjectName(u"Basic1_Spanish")
        self.formLayout_9 = QFormLayout(self.Basic1_Spanish)
        self.formLayout_9.setObjectName(u"formLayout_9")
        self.frame_7 = QFrame(self.Basic1_Spanish)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.frame_7)
        self.gridLayout_10.setObjectName(u"gridLayout_10")

        self.formLayout_9.setWidget(3, QFormLayout.LabelRole, self.frame_7)

        self.frame_8 = QFrame(self.Basic1_Spanish)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_8)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.Basic1SpanishNavButtonLeft = QPushButton(self.frame_8)
        self.Basic1SpanishNavButtonLeft.setObjectName(u"Basic1SpanishNavButtonLeft")
        self.Basic1SpanishNavButtonLeft.setFont(font5)
        self.Basic1SpanishNavButtonLeft.setLayoutDirection(Qt.LeftToRight)
        self.Basic1SpanishNavButtonLeft.setStyleSheet(u"\n"
"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 10px;	\n"
"	background: #3399ff;\n"
"	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #2b82d9;\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")

        self.gridLayout_9.addWidget(self.Basic1SpanishNavButtonLeft, 0, 0, 1, 1)

        self.Basic1SpanishNavButtonRight = QPushButton(self.frame_8)
        self.Basic1SpanishNavButtonRight.setObjectName(u"Basic1SpanishNavButtonRight")
        self.Basic1SpanishNavButtonRight.setFont(font5)
        self.Basic1SpanishNavButtonRight.setStyleSheet(u"\n"
"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 10px;	\n"
"	background: #3399ff;\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #2b82d9;\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")

        self.gridLayout_9.addWidget(self.Basic1SpanishNavButtonRight, 0, 1, 1, 1)


        self.formLayout_9.setWidget(3, QFormLayout.FieldRole, self.frame_8)

        self.Basic1Spanish_StackedWidget = QStackedWidget(self.Basic1_Spanish)
        self.Basic1Spanish_StackedWidget.setObjectName(u"Basic1Spanish_StackedWidget")
        self.Basic1Spanish_StackedWidget.setMaximumSize(QSize(1000, 450))
        self.Basic1Spanish_Page1 = QWidget()
        self.Basic1Spanish_Page1.setObjectName(u"Basic1Spanish_Page1")
        self.formLayout_10 = QFormLayout(self.Basic1Spanish_Page1)
        self.formLayout_10.setObjectName(u"formLayout_10")
        self.label_15 = QLabel(self.Basic1Spanish_Page1)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font4)
        self.label_15.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.formLayout_10.setWidget(0, QFormLayout.SpanningRole, self.label_15)

        self.Basic1Spanish_StackedWidget.addWidget(self.Basic1Spanish_Page1)
        self.Basic1Spanish_Page2 = QWidget()
        self.Basic1Spanish_Page2.setObjectName(u"Basic1Spanish_Page2")
        self.formLayout_11 = QFormLayout(self.Basic1Spanish_Page2)
        self.formLayout_11.setObjectName(u"formLayout_11")
        self.label_16 = QLabel(self.Basic1Spanish_Page2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font4)
        self.label_16.setStyleSheet(u"text-color= white;")

        self.formLayout_11.setWidget(0, QFormLayout.SpanningRole, self.label_16)

        self.Basic1Spanish_StackedWidget.addWidget(self.Basic1Spanish_Page2)
        self.Basic1Spanish_Page3 = QWidget()
        self.Basic1Spanish_Page3.setObjectName(u"Basic1Spanish_Page3")
        self.formLayout_12 = QFormLayout(self.Basic1Spanish_Page3)
        self.formLayout_12.setObjectName(u"formLayout_12")
        self.label_17 = QLabel(self.Basic1Spanish_Page3)
        self.label_17.setObjectName(u"label_17")

        self.formLayout_12.setWidget(0, QFormLayout.SpanningRole, self.label_17)

        self.Basic1Spanish_StackedWidget.addWidget(self.Basic1Spanish_Page3)

        self.formLayout_9.setWidget(1, QFormLayout.FieldRole, self.Basic1Spanish_StackedWidget)

        self.label_13 = QLabel(self.Basic1_Spanish)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font3)

        self.formLayout_9.setWidget(0, QFormLayout.FieldRole, self.label_13)

        self.stackedWidget.addWidget(self.Basic1_Spanish)
        self.Basic2_Spanish = QWidget()
        self.Basic2_Spanish.setObjectName(u"Basic2_Spanish")
        self.formLayout_13 = QFormLayout(self.Basic2_Spanish)
        self.formLayout_13.setObjectName(u"formLayout_13")
        self.frame_9 = QFrame(self.Basic2_Spanish)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.gridLayout_12 = QGridLayout(self.frame_9)
        self.gridLayout_12.setObjectName(u"gridLayout_12")

        self.formLayout_13.setWidget(2, QFormLayout.LabelRole, self.frame_9)

        self.frame_10 = QFrame(self.Basic2_Spanish)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.gridLayout_11 = QGridLayout(self.frame_10)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.Basic2SpanishNavButtonLeft = QPushButton(self.frame_10)
        self.Basic2SpanishNavButtonLeft.setObjectName(u"Basic2SpanishNavButtonLeft")
        self.Basic2SpanishNavButtonLeft.setFont(font5)
        self.Basic2SpanishNavButtonLeft.setLayoutDirection(Qt.LeftToRight)
        self.Basic2SpanishNavButtonLeft.setStyleSheet(u"\n"
"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 10px;	\n"
"	background: #3399ff;\n"
"	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #2b82d9;\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")

        self.gridLayout_11.addWidget(self.Basic2SpanishNavButtonLeft, 0, 0, 1, 1)

        self.Basic2SpanishNavButtonRight = QPushButton(self.frame_10)
        self.Basic2SpanishNavButtonRight.setObjectName(u"Basic2SpanishNavButtonRight")
        self.Basic2SpanishNavButtonRight.setFont(font5)
        self.Basic2SpanishNavButtonRight.setStyleSheet(u"\n"
"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 10px;	\n"
"	background: #3399ff;\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #2b82d9;\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")

        self.gridLayout_11.addWidget(self.Basic2SpanishNavButtonRight, 0, 1, 1, 1)


        self.formLayout_13.setWidget(2, QFormLayout.FieldRole, self.frame_10)

        self.Basic2Spanish_StackedWidget = QStackedWidget(self.Basic2_Spanish)
        self.Basic2Spanish_StackedWidget.setObjectName(u"Basic2Spanish_StackedWidget")
        self.Basic2Spanish_StackedWidget.setMaximumSize(QSize(1000, 450))
        self.Basic2Spanish_Page1 = QWidget()
        self.Basic2Spanish_Page1.setObjectName(u"Basic2Spanish_Page1")
        self.formLayout_14 = QFormLayout(self.Basic2Spanish_Page1)
        self.formLayout_14.setObjectName(u"formLayout_14")
        self.label_18 = QLabel(self.Basic2Spanish_Page1)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font4)
        self.label_18.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.formLayout_14.setWidget(0, QFormLayout.SpanningRole, self.label_18)

        self.Basic2Spanish_StackedWidget.addWidget(self.Basic2Spanish_Page1)
        self.Basic2Spanish_Page2 = QWidget()
        self.Basic2Spanish_Page2.setObjectName(u"Basic2Spanish_Page2")
        self.formLayout_15 = QFormLayout(self.Basic2Spanish_Page2)
        self.formLayout_15.setObjectName(u"formLayout_15")
        self.label_19 = QLabel(self.Basic2Spanish_Page2)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font4)
        self.label_19.setStyleSheet(u"text-color= white;")

        self.formLayout_15.setWidget(0, QFormLayout.SpanningRole, self.label_19)

        self.Basic2Spanish_StackedWidget.addWidget(self.Basic2Spanish_Page2)

        self.formLayout_13.setWidget(1, QFormLayout.FieldRole, self.Basic2Spanish_StackedWidget)

        self.label_20 = QLabel(self.Basic2_Spanish)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font3)

        self.formLayout_13.setWidget(0, QFormLayout.FieldRole, self.label_20)

        self.stackedWidget.addWidget(self.Basic2_Spanish)
        self.Basic1_Italian = QWidget()
        self.Basic1_Italian.setObjectName(u"Basic1_Italian")
        self.formLayout_19 = QFormLayout(self.Basic1_Italian)
        self.formLayout_19.setObjectName(u"formLayout_19")
        self.frame_12 = QFrame(self.Basic1_Italian)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.gridLayout_14 = QGridLayout(self.frame_12)
        self.gridLayout_14.setObjectName(u"gridLayout_14")

        self.formLayout_19.setWidget(2, QFormLayout.LabelRole, self.frame_12)

        self.frame_13 = QFrame(self.Basic1_Italian)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.gridLayout_15 = QGridLayout(self.frame_13)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.Basic1ItalianNavButtonLeft = QPushButton(self.frame_13)
        self.Basic1ItalianNavButtonLeft.setObjectName(u"Basic1ItalianNavButtonLeft")
        self.Basic1ItalianNavButtonLeft.setFont(font5)
        self.Basic1ItalianNavButtonLeft.setLayoutDirection(Qt.LeftToRight)
        self.Basic1ItalianNavButtonLeft.setStyleSheet(u"\n"
"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 10px;	\n"
"	background: #3399ff;\n"
"	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #2b82d9;\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")

        self.gridLayout_15.addWidget(self.Basic1ItalianNavButtonLeft, 0, 0, 1, 1)

        self.Basic1ItalianNavButtonRight = QPushButton(self.frame_13)
        self.Basic1ItalianNavButtonRight.setObjectName(u"Basic1ItalianNavButtonRight")
        self.Basic1ItalianNavButtonRight.setFont(font5)
        self.Basic1ItalianNavButtonRight.setStyleSheet(u"\n"
"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 10px;	\n"
"	background: #3399ff;\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #2b82d9;\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")

        self.gridLayout_15.addWidget(self.Basic1ItalianNavButtonRight, 0, 1, 1, 1)


        self.formLayout_19.setWidget(2, QFormLayout.FieldRole, self.frame_13)

        self.Basic1Italian_StackedWidget = QStackedWidget(self.Basic1_Italian)
        self.Basic1Italian_StackedWidget.setObjectName(u"Basic1Italian_StackedWidget")
        self.Basic1Italian_StackedWidget.setMaximumSize(QSize(1000, 450))
        self.Basic1Italian_Page1 = QWidget()
        self.Basic1Italian_Page1.setObjectName(u"Basic1Italian_Page1")
        self.formLayout_16 = QFormLayout(self.Basic1Italian_Page1)
        self.formLayout_16.setObjectName(u"formLayout_16")
        self.label_22 = QLabel(self.Basic1Italian_Page1)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font4)
        self.label_22.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.formLayout_16.setWidget(0, QFormLayout.SpanningRole, self.label_22)

        self.Basic1Italian_StackedWidget.addWidget(self.Basic1Italian_Page1)
        self.Basic1Italian_Page2 = QWidget()
        self.Basic1Italian_Page2.setObjectName(u"Basic1Italian_Page2")
        self.formLayout_17 = QFormLayout(self.Basic1Italian_Page2)
        self.formLayout_17.setObjectName(u"formLayout_17")
        self.label_23 = QLabel(self.Basic1Italian_Page2)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font4)
        self.label_23.setStyleSheet(u"text-color= white;")

        self.formLayout_17.setWidget(0, QFormLayout.SpanningRole, self.label_23)

        self.Basic1Italian_StackedWidget.addWidget(self.Basic1Italian_Page2)
        self.Basic1Italian_Page3 = QWidget()
        self.Basic1Italian_Page3.setObjectName(u"Basic1Italian_Page3")
        self.formLayout_18 = QFormLayout(self.Basic1Italian_Page3)
        self.formLayout_18.setObjectName(u"formLayout_18")
        self.label_24 = QLabel(self.Basic1Italian_Page3)
        self.label_24.setObjectName(u"label_24")

        self.formLayout_18.setWidget(0, QFormLayout.SpanningRole, self.label_24)

        self.Basic1Italian_StackedWidget.addWidget(self.Basic1Italian_Page3)

        self.formLayout_19.setWidget(1, QFormLayout.FieldRole, self.Basic1Italian_StackedWidget)

        self.label_21 = QLabel(self.Basic1_Italian)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font3)

        self.formLayout_19.setWidget(0, QFormLayout.FieldRole, self.label_21)

        self.stackedWidget.addWidget(self.Basic1_Italian)
        self.Basic2_Italian = QWidget()
        self.Basic2_Italian.setObjectName(u"Basic2_Italian")
        self.formLayout_20 = QFormLayout(self.Basic2_Italian)
        self.formLayout_20.setObjectName(u"formLayout_20")
        self.frame_14 = QFrame(self.Basic2_Italian)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.gridLayout_17 = QGridLayout(self.frame_14)
        self.gridLayout_17.setObjectName(u"gridLayout_17")

        self.formLayout_20.setWidget(3, QFormLayout.LabelRole, self.frame_14)

        self.frame_15 = QFrame(self.Basic2_Italian)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.gridLayout_16 = QGridLayout(self.frame_15)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.Basic2ItalianNavButtonLeft = QPushButton(self.frame_15)
        self.Basic2ItalianNavButtonLeft.setObjectName(u"Basic2ItalianNavButtonLeft")
        self.Basic2ItalianNavButtonLeft.setFont(font5)
        self.Basic2ItalianNavButtonLeft.setLayoutDirection(Qt.LeftToRight)
        self.Basic2ItalianNavButtonLeft.setStyleSheet(u"\n"
"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 10px;	\n"
"	background: #3399ff;\n"
"	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #2b82d9;\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")

        self.gridLayout_16.addWidget(self.Basic2ItalianNavButtonLeft, 0, 0, 1, 1)

        self.Basic2ItalianNavButtonRight = QPushButton(self.frame_15)
        self.Basic2ItalianNavButtonRight.setObjectName(u"Basic2ItalianNavButtonRight")
        self.Basic2ItalianNavButtonRight.setFont(font5)
        self.Basic2ItalianNavButtonRight.setStyleSheet(u"\n"
"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 10px;	\n"
"	background: #3399ff;\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #2b82d9;\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")

        self.gridLayout_16.addWidget(self.Basic2ItalianNavButtonRight, 0, 1, 1, 1)


        self.formLayout_20.setWidget(3, QFormLayout.FieldRole, self.frame_15)

        self.Basic2Italian_StackedWidget = QStackedWidget(self.Basic2_Italian)
        self.Basic2Italian_StackedWidget.setObjectName(u"Basic2Italian_StackedWidget")
        self.Basic2Italian_StackedWidget.setMaximumSize(QSize(1000, 450))
        self.Basic2Italian_Page1 = QWidget()
        self.Basic2Italian_Page1.setObjectName(u"Basic2Italian_Page1")
        self.formLayout_21 = QFormLayout(self.Basic2Italian_Page1)
        self.formLayout_21.setObjectName(u"formLayout_21")
        self.label_25 = QLabel(self.Basic2Italian_Page1)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font4)
        self.label_25.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.formLayout_21.setWidget(0, QFormLayout.SpanningRole, self.label_25)

        self.Basic2Italian_StackedWidget.addWidget(self.Basic2Italian_Page1)
        self.Basic2Italian_Page2 = QWidget()
        self.Basic2Italian_Page2.setObjectName(u"Basic2Italian_Page2")
        self.formLayout_22 = QFormLayout(self.Basic2Italian_Page2)
        self.formLayout_22.setObjectName(u"formLayout_22")
        self.label_26 = QLabel(self.Basic2Italian_Page2)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font4)
        self.label_26.setStyleSheet(u"text-color= white;")

        self.formLayout_22.setWidget(0, QFormLayout.SpanningRole, self.label_26)

        self.Basic2Italian_StackedWidget.addWidget(self.Basic2Italian_Page2)

        self.formLayout_20.setWidget(1, QFormLayout.FieldRole, self.Basic2Italian_StackedWidget)

        self.label_27 = QLabel(self.Basic2_Italian)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font3)

        self.formLayout_20.setWidget(0, QFormLayout.FieldRole, self.label_27)

        self.stackedWidget.addWidget(self.Basic2_Italian)
        self.page_quizes = QWidget()
        self.page_quizes.setObjectName(u"page_quizes")
        self.formLayout_23 = QFormLayout(self.page_quizes)
        self.formLayout_23.setObjectName(u"formLayout_23")
        self.label_28 = QLabel(self.page_quizes)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMaximumSize(QSize(16777215, 100))
        font6 = QFont()
        font6.setFamily(u"Miriam")
        font6.setPointSize(35)
        font6.setBold(True)
        font6.setWeight(75)
        self.label_28.setFont(font6)

        self.formLayout_23.setWidget(0, QFormLayout.SpanningRole, self.label_28)

        self.QuizButton_French = QPushButton(self.page_quizes)
        self.QuizButton_French.setObjectName(u"QuizButton_French")
        font7 = QFont()
        font7.setPointSize(40)
        font7.setBold(True)
        font7.setWeight(75)
        self.QuizButton_French.setFont(font7)
        self.QuizButton_French.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	 background: #3399ff;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #2b82d9;\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")

        self.formLayout_23.setWidget(1, QFormLayout.FieldRole, self.QuizButton_French)

        self.QuizButton_Italian = QPushButton(self.page_quizes)
        self.QuizButton_Italian.setObjectName(u"QuizButton_Italian")
        self.QuizButton_Italian.setFont(font7)
        self.QuizButton_Italian.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	 background: #3399ff;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #2b82d9;\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")

        self.formLayout_23.setWidget(2, QFormLayout.FieldRole, self.QuizButton_Italian)

        self.QuizButton_Spanish = QPushButton(self.page_quizes)
        self.QuizButton_Spanish.setObjectName(u"QuizButton_Spanish")
        self.QuizButton_Spanish.setFont(font7)
        self.QuizButton_Spanish.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	 background: #3399ff;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #2b82d9;\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")

        self.formLayout_23.setWidget(3, QFormLayout.FieldRole, self.QuizButton_Spanish)

        self.stackedWidget.addWidget(self.page_quizes)
        self.QuizOutput_Page = QWidget()
        self.QuizOutput_Page.setObjectName(u"QuizOutput_Page")
        self.gridLayout_24 = QGridLayout(self.QuizOutput_Page)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.frame_20 = QFrame(self.QuizOutput_Page)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.QuizOutputPage_OutputLabel = QLabel(self.frame_20)
        self.QuizOutputPage_OutputLabel.setObjectName(u"QuizOutputPage_OutputLabel")
        self.QuizOutputPage_OutputLabel.setGeometry(QRect(10, 0, 541, 71))
        font8 = QFont()
        font8.setFamily(u"Corbel")
        font8.setPointSize(28)
        font8.setBold(True)
        font8.setWeight(75)
        self.QuizOutputPage_OutputLabel.setFont(font8)
        self.QuizOutputPage_CorrectAnswer = QLabel(self.frame_20)
        self.QuizOutputPage_CorrectAnswer.setObjectName(u"QuizOutputPage_CorrectAnswer")
        self.QuizOutputPage_CorrectAnswer.setGeometry(QRect(10, 150, 821, 231))
        self.QuizOutputPage_CorrectAnswer.setFont(font8)
        self.QuizOutputPage_CorrectAnswer.setStyleSheet(u"color: rgb(67, 255, 67);")
        self.QuizOutputPage_CorrectAnswer.setWordWrap(True)
        self.QuizOutputPage_NextButton = QPushButton(self.frame_20)
        self.QuizOutputPage_NextButton.setObjectName(u"QuizOutputPage_NextButton")
        self.QuizOutputPage_NextButton.setGeometry(QRect(0, 520, 331, 61))
        font9 = QFont()
        font9.setPointSize(20)
        font9.setBold(True)
        font9.setWeight(75)
        self.QuizOutputPage_NextButton.setFont(font9)
        self.QuizOutputPage_NextButton.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(1, 1, 1);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(1, 1, 1);\n"
"	color: #FFFFFF;\n"
"	\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"")

        self.gridLayout_24.addWidget(self.frame_20, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.QuizOutput_Page)
        self.SubjectFrench_QuizPage = QWidget()
        self.SubjectFrench_QuizPage.setObjectName(u"SubjectFrench_QuizPage")
        self.gridLayout_18 = QGridLayout(self.SubjectFrench_QuizPage)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.frame_17 = QFrame(self.SubjectFrench_QuizPage)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.formLayout_26 = QFormLayout(self.frame_17)
        self.formLayout_26.setObjectName(u"formLayout_26")
        self.FrenchQuiz_QuestionText = QLabel(self.frame_17)
        self.FrenchQuiz_QuestionText.setObjectName(u"FrenchQuiz_QuestionText")
        font10 = QFont()
        font10.setPointSize(17)
        font10.setBold(True)
        font10.setWeight(75)
        self.FrenchQuiz_QuestionText.setFont(font10)
        self.FrenchQuiz_QuestionText.setScaledContents(False)
        self.FrenchQuiz_QuestionText.setWordWrap(True)

        self.formLayout_26.setWidget(0, QFormLayout.SpanningRole, self.FrenchQuiz_QuestionText)

        self.FrenchQuizButton_Submit = QPushButton(self.frame_17)
        self.FrenchQuizButton_Submit.setObjectName(u"FrenchQuizButton_Submit")
        self.FrenchQuizButton_Submit.setFont(font7)
        self.FrenchQuizButton_Submit.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	 background: #3399ff;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #2b82d9;\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")

        self.formLayout_26.setWidget(4, QFormLayout.SpanningRole, self.FrenchQuizButton_Submit)

        self.FrenchFrame_RadioButtons = QFrame(self.frame_17)
        self.FrenchFrame_RadioButtons.setObjectName(u"FrenchFrame_RadioButtons")
        self.FrenchFrame_RadioButtons.setFrameShape(QFrame.StyledPanel)
        self.FrenchFrame_RadioButtons.setFrameShadow(QFrame.Raised)
        self.gridLayout_19 = QGridLayout(self.FrenchFrame_RadioButtons)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.FrenchQuizRadioButton_1 = QRadioButton(self.FrenchFrame_RadioButtons)
        self.FrenchQuizRadioButton_1.setObjectName(u"FrenchQuizRadioButton_1")
        font11 = QFont()
        font11.setPointSize(11)
        font11.setBold(True)
        font11.setWeight(75)
        self.FrenchQuizRadioButton_1.setFont(font11)
        self.FrenchQuizRadioButton_1.setStyleSheet(u"QRadioButton::indicator:checked {\n"
"    background-color:      green;\n"
"  \n"
"}")
        self.FrenchQuizRadioButton_1.setChecked(True)

        self.gridLayout_19.addWidget(self.FrenchQuizRadioButton_1, 0, 0, 1, 1)

        self.FrenchQuizRadioButton_2 = QRadioButton(self.FrenchFrame_RadioButtons)
        self.FrenchQuizRadioButton_2.setObjectName(u"FrenchQuizRadioButton_2")
        self.FrenchQuizRadioButton_2.setFont(font11)
        self.FrenchQuizRadioButton_2.setStyleSheet(u"QRadioButton::indicator:checked {\n"
"    background-color:      green;\n"
"  \n"
"}")
        self.FrenchQuizRadioButton_2.setCheckable(True)
        self.FrenchQuizRadioButton_2.setChecked(False)

        self.gridLayout_19.addWidget(self.FrenchQuizRadioButton_2, 0, 1, 1, 1)

        self.FrenchQuizRadioButton_3 = QRadioButton(self.FrenchFrame_RadioButtons)
        self.FrenchQuizRadioButton_3.setObjectName(u"FrenchQuizRadioButton_3")
        self.FrenchQuizRadioButton_3.setFont(font11)
        self.FrenchQuizRadioButton_3.setStyleSheet(u"QRadioButton::indicator:checked {\n"
"    background-color:      green;\n"
"  \n"
"}")

        self.gridLayout_19.addWidget(self.FrenchQuizRadioButton_3, 0, 2, 1, 1)


        self.formLayout_26.setWidget(2, QFormLayout.SpanningRole, self.FrenchFrame_RadioButtons)

        self.FrenchQuizButton_Skip = QPushButton(self.frame_17)
        self.FrenchQuizButton_Skip.setObjectName(u"FrenchQuizButton_Skip")
        font12 = QFont()
        font12.setPointSize(25)
        font12.setBold(True)
        font12.setWeight(75)
        self.FrenchQuizButton_Skip.setFont(font12)
        self.FrenchQuizButton_Skip.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	 background: #3399ff;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #2b82d9;\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")

        self.formLayout_26.setWidget(5, QFormLayout.SpanningRole, self.FrenchQuizButton_Skip)

        self.verticalSpacer = QSpacerItem(10, 87, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.formLayout_26.setItem(1, QFormLayout.SpanningRole, self.verticalSpacer)

        self.verticalSpacer_2 = QSpacerItem(10, 30, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.formLayout_26.setItem(3, QFormLayout.SpanningRole, self.verticalSpacer_2)


        self.gridLayout_18.addWidget(self.frame_17, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.SubjectFrench_QuizPage)
        self.SubjectSpanish_QuizPage = QWidget()
        self.SubjectSpanish_QuizPage.setObjectName(u"SubjectSpanish_QuizPage")
        self.gridLayout_20 = QGridLayout(self.SubjectSpanish_QuizPage)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.frame_18 = QFrame(self.SubjectSpanish_QuizPage)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.formLayout_27 = QFormLayout(self.frame_18)
        self.formLayout_27.setObjectName(u"formLayout_27")
        self.SpanishQuiz_QuestionText = QLabel(self.frame_18)
        self.SpanishQuiz_QuestionText.setObjectName(u"SpanishQuiz_QuestionText")
        self.SpanishQuiz_QuestionText.setFont(font10)
        self.SpanishQuiz_QuestionText.setScaledContents(False)
        self.SpanishQuiz_QuestionText.setWordWrap(True)

        self.formLayout_27.setWidget(0, QFormLayout.SpanningRole, self.SpanishQuiz_QuestionText)

        self.verticalSpacer_3 = QSpacerItem(859, 87, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.formLayout_27.setItem(1, QFormLayout.SpanningRole, self.verticalSpacer_3)

        self.SpanishFrame_RadioButtons = QFrame(self.frame_18)
        self.SpanishFrame_RadioButtons.setObjectName(u"SpanishFrame_RadioButtons")
        self.SpanishFrame_RadioButtons.setFrameShape(QFrame.StyledPanel)
        self.SpanishFrame_RadioButtons.setFrameShadow(QFrame.Raised)
        self.gridLayout_21 = QGridLayout(self.SpanishFrame_RadioButtons)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.SpanishQuizRadioButton_1 = QRadioButton(self.SpanishFrame_RadioButtons)
        self.SpanishQuizRadioButton_1.setObjectName(u"SpanishQuizRadioButton_1")
        self.SpanishQuizRadioButton_1.setFont(font11)
        self.SpanishQuizRadioButton_1.setStyleSheet(u"QRadioButton::indicator:checked {\n"
"    background-color:      green;\n"
"  \n"
"}")

        self.gridLayout_21.addWidget(self.SpanishQuizRadioButton_1, 0, 0, 1, 1)

        self.SpanishQuizRadioButton_2 = QRadioButton(self.SpanishFrame_RadioButtons)
        self.SpanishQuizRadioButton_2.setObjectName(u"SpanishQuizRadioButton_2")
        self.SpanishQuizRadioButton_2.setFont(font11)
        self.SpanishQuizRadioButton_2.setStyleSheet(u"QRadioButton::indicator:checked {\n"
"    background-color:      green;\n"
"  \n"
"}")

        self.gridLayout_21.addWidget(self.SpanishQuizRadioButton_2, 0, 1, 1, 1)

        self.SpanishQuizRadioButton_3 = QRadioButton(self.SpanishFrame_RadioButtons)
        self.SpanishQuizRadioButton_3.setObjectName(u"SpanishQuizRadioButton_3")
        self.SpanishQuizRadioButton_3.setFont(font11)
        self.SpanishQuizRadioButton_3.setStyleSheet(u"QRadioButton::indicator:checked {\n"
"    background-color:      green;\n"
"  \n"
"}")

        self.gridLayout_21.addWidget(self.SpanishQuizRadioButton_3, 0, 2, 1, 1)


        self.formLayout_27.setWidget(2, QFormLayout.SpanningRole, self.SpanishFrame_RadioButtons)

        self.SpanishQuizButton_Submit = QPushButton(self.frame_18)
        self.SpanishQuizButton_Submit.setObjectName(u"SpanishQuizButton_Submit")
        self.SpanishQuizButton_Submit.setFont(font7)
        self.SpanishQuizButton_Submit.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	 background: #3399ff;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #2b82d9;\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")

        self.formLayout_27.setWidget(4, QFormLayout.SpanningRole, self.SpanishQuizButton_Submit)

        self.SpanishQuizButton_Skip = QPushButton(self.frame_18)
        self.SpanishQuizButton_Skip.setObjectName(u"SpanishQuizButton_Skip")
        self.SpanishQuizButton_Skip.setFont(font12)
        self.SpanishQuizButton_Skip.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	 background: #3399ff;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #2b82d9;\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")

        self.formLayout_27.setWidget(5, QFormLayout.SpanningRole, self.SpanishQuizButton_Skip)

        self.verticalSpacer_4 = QSpacerItem(859, 30, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.formLayout_27.setItem(3, QFormLayout.SpanningRole, self.verticalSpacer_4)


        self.gridLayout_20.addWidget(self.frame_18, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.SubjectSpanish_QuizPage)
        self.SubjectItalian_QuizPage = QWidget()
        self.SubjectItalian_QuizPage.setObjectName(u"SubjectItalian_QuizPage")
        self.gridLayout_22 = QGridLayout(self.SubjectItalian_QuizPage)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.frame_19 = QFrame(self.SubjectItalian_QuizPage)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.formLayout_28 = QFormLayout(self.frame_19)
        self.formLayout_28.setObjectName(u"formLayout_28")
        self.verticalSpacer_6 = QSpacerItem(859, 30, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.formLayout_28.setItem(4, QFormLayout.LabelRole, self.verticalSpacer_6)

        self.ItalianFrame_RadioButtons = QFrame(self.frame_19)
        self.ItalianFrame_RadioButtons.setObjectName(u"ItalianFrame_RadioButtons")
        self.ItalianFrame_RadioButtons.setFrameShape(QFrame.StyledPanel)
        self.ItalianFrame_RadioButtons.setFrameShadow(QFrame.Raised)
        self.gridLayout_23 = QGridLayout(self.ItalianFrame_RadioButtons)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.ItalianQuizRadioButton_1 = QRadioButton(self.ItalianFrame_RadioButtons)
        self.ItalianQuizRadioButton_1.setObjectName(u"ItalianQuizRadioButton_1")
        self.ItalianQuizRadioButton_1.setFont(font11)
        self.ItalianQuizRadioButton_1.setStyleSheet(u"QRadioButton::indicator:checked {\n"
"    background-color:      green;\n"
"  \n"
"}")

        self.gridLayout_23.addWidget(self.ItalianQuizRadioButton_1, 0, 0, 1, 1)

        self.ItalianQuizRadioButton_2 = QRadioButton(self.ItalianFrame_RadioButtons)
        self.ItalianQuizRadioButton_2.setObjectName(u"ItalianQuizRadioButton_2")
        self.ItalianQuizRadioButton_2.setFont(font11)
        self.ItalianQuizRadioButton_2.setStyleSheet(u"QRadioButton::indicator:checked {\n"
"    background-color:      green;\n"
"  \n"
"}")

        self.gridLayout_23.addWidget(self.ItalianQuizRadioButton_2, 0, 1, 1, 1)

        self.ItalianQuizRadioButton_3 = QRadioButton(self.ItalianFrame_RadioButtons)
        self.ItalianQuizRadioButton_3.setObjectName(u"ItalianQuizRadioButton_3")
        self.ItalianQuizRadioButton_3.setFont(font11)
        self.ItalianQuizRadioButton_3.setStyleSheet(u"QRadioButton::indicator:checked {\n"
"    background-color:      green;\n"
"  \n"
"}")

        self.gridLayout_23.addWidget(self.ItalianQuizRadioButton_3, 0, 2, 1, 1)


        self.formLayout_28.setWidget(3, QFormLayout.SpanningRole, self.ItalianFrame_RadioButtons)

        self.verticalSpacer_5 = QSpacerItem(859, 87, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.formLayout_28.setItem(2, QFormLayout.LabelRole, self.verticalSpacer_5)

        self.ItalianQuizButton_Submit = QPushButton(self.frame_19)
        self.ItalianQuizButton_Submit.setObjectName(u"ItalianQuizButton_Submit")
        self.ItalianQuizButton_Submit.setFont(font7)
        self.ItalianQuizButton_Submit.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	 background: #3399ff;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #2b82d9;\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")

        self.formLayout_28.setWidget(5, QFormLayout.SpanningRole, self.ItalianQuizButton_Submit)

        self.ItalianQuizButton_Skip = QPushButton(self.frame_19)
        self.ItalianQuizButton_Skip.setObjectName(u"ItalianQuizButton_Skip")
        self.ItalianQuizButton_Skip.setFont(font12)
        self.ItalianQuizButton_Skip.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	 background: #3399ff;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #2b82d9;\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")

        self.formLayout_28.setWidget(6, QFormLayout.SpanningRole, self.ItalianQuizButton_Skip)

        self.ItalianQuiz_QuestionText = QLabel(self.frame_19)
        self.ItalianQuiz_QuestionText.setObjectName(u"ItalianQuiz_QuestionText")
        self.ItalianQuiz_QuestionText.setFont(font10)
        self.ItalianQuiz_QuestionText.setScaledContents(False)
        self.ItalianQuiz_QuestionText.setWordWrap(True)

        self.formLayout_28.setWidget(0, QFormLayout.SpanningRole, self.ItalianQuiz_QuestionText)


        self.gridLayout_22.addWidget(self.frame_19, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.SubjectItalian_QuizPage)
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.formLayout = QFormLayout(self.page_home)
        self.formLayout.setObjectName(u"formLayout")
        self.label_6 = QLabel(self.page_home)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setEnabled(True)
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy5)
        self.label_6.setFont(font6)
        self.label_6.setStyleSheet(u"")
        self.label_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_6)

        self.formLayout_24 = QFormLayout()
        self.formLayout_24.setObjectName(u"formLayout_24")
        self.SubjectButton_French = QPushButton(self.page_home)
        self.SubjectButton_French.setObjectName(u"SubjectButton_French")
        self.SubjectButton_French.setFont(font7)
        self.SubjectButton_French.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	 background: #3399ff;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #2b82d9;\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")

        self.formLayout_24.setWidget(0, QFormLayout.SpanningRole, self.SubjectButton_French)

        self.SubjectButton_Italian = QPushButton(self.page_home)
        self.SubjectButton_Italian.setObjectName(u"SubjectButton_Italian")
        self.SubjectButton_Italian.setFont(font7)
        self.SubjectButton_Italian.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	 background: #3399ff;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #2b82d9;\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")

        self.formLayout_24.setWidget(1, QFormLayout.SpanningRole, self.SubjectButton_Italian)

        self.SubjectButton_Spanish = QPushButton(self.page_home)
        self.SubjectButton_Spanish.setObjectName(u"SubjectButton_Spanish")
        self.SubjectButton_Spanish.setFont(font7)
        self.SubjectButton_Spanish.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	 background: #3399ff;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #2b82d9;\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")

        self.formLayout_24.setWidget(2, QFormLayout.SpanningRole, self.SubjectButton_Spanish)


        self.formLayout.setLayout(1, QFormLayout.SpanningRole, self.formLayout_24)

        self.stackedWidget.addWidget(self.page_home)
        self.btn_user_stats = QWidget()
        self.btn_user_stats.setObjectName(u"btn_user_stats")
        self.label = QLabel(self.btn_user_stats)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 110, 271, 41))
        font13 = QFont()
        font13.setPointSize(21)
        self.label.setFont(font13)
        self.label_2 = QLabel(self.btn_user_stats)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 150, 271, 41))
        self.label_2.setFont(font13)
        self.CoursesEnrolled_Text = QLabel(self.btn_user_stats)
        self.CoursesEnrolled_Text.setObjectName(u"CoursesEnrolled_Text")
        self.CoursesEnrolled_Text.setGeometry(QRect(230, 110, 71, 41))
        self.CoursesEnrolled_Text.setFont(font13)
        self.QuizesDone_Text = QLabel(self.btn_user_stats)
        self.QuizesDone_Text.setObjectName(u"QuizesDone_Text")
        self.QuizesDone_Text.setGeometry(QRect(200, 150, 71, 41))
        self.QuizesDone_Text.setFont(font13)
        self.label_5 = QLabel(self.btn_user_stats)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(0, 0, 301, 51))
        font14 = QFont()
        font14.setFamily(u"Rod")
        font14.setPointSize(32)
        font14.setBold(True)
        font14.setItalic(False)
        font14.setUnderline(False)
        font14.setWeight(75)
        self.label_5.setFont(font14)
        self.label_3 = QLabel(self.btn_user_stats)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 190, 271, 41))
        self.label_3.setFont(font13)
        self.QuizesPassed_Txt = QLabel(self.btn_user_stats)
        self.QuizesPassed_Txt.setObjectName(u"QuizesPassed_Txt")
        self.QuizesPassed_Txt.setGeometry(QRect(200, 190, 71, 41))
        self.QuizesPassed_Txt.setFont(font13)
        self.QuizesFails_Txt = QLabel(self.btn_user_stats)
        self.QuizesFails_Txt.setObjectName(u"QuizesFails_Txt")
        self.QuizesFails_Txt.setGeometry(QRect(180, 230, 71, 41))
        self.QuizesFails_Txt.setFont(font13)
        self.label_4 = QLabel(self.btn_user_stats)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(0, 230, 271, 41))
        self.label_4.setFont(font13)
        self.stackedWidget.addWidget(self.btn_user_stats)
        self.label_4.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.CoursesEnrolled_Text.raise_()
        self.QuizesDone_Text.raise_()
        self.label_5.raise_()
        self.label_3.raise_()
        self.QuizesPassed_Txt.raise_()
        self.QuizesFails_Txt.raise_()
        self.page_widgets_deprecated = QWidget()
        self.page_widgets_deprecated.setObjectName(u"page_widgets_deprecated")
        self.page_widgets_deprecated.setEnabled(True)
        self.verticalLayout_6 = QVBoxLayout(self.page_widgets_deprecated)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame = QFrame(self.page_widgets_deprecated)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"border-radius: 5px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frame_div_content_1 = QFrame(self.frame)
        self.frame_div_content_1.setObjectName(u"frame_div_content_1")
        self.frame_div_content_1.setMinimumSize(QSize(0, 110))
        self.frame_div_content_1.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_1.setStyleSheet(u"background-color: rgb(41, 45, 56);\n"
"border-radius: 5px;\n"
"")
        self.frame_div_content_1.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_div_content_1)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_title_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_title_wid_1.setObjectName(u"frame_title_wid_1")
        self.frame_title_wid_1.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_1.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.frame_title_wid_1.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_title_wid_1)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.labelBoxBlenderInstalation = QLabel(self.frame_title_wid_1)
        self.labelBoxBlenderInstalation.setObjectName(u"labelBoxBlenderInstalation")
        self.labelBoxBlenderInstalation.setFont(font1)
        self.labelBoxBlenderInstalation.setStyleSheet(u"")

        self.verticalLayout_8.addWidget(self.labelBoxBlenderInstalation)


        self.verticalLayout_7.addWidget(self.frame_title_wid_1)

        self.frame_content_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_content_wid_1.setObjectName(u"frame_content_wid_1")
        self.frame_content_wid_1.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_content_wid_1)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)
        self.lineEdit = QLineEdit(self.frame_content_wid_1)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 30))
        self.lineEdit.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)

        self.pushButton = QPushButton(self.frame_content_wid_1)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(150, 30))
        font15 = QFont()
        font15.setFamily(u"Segoe UI")
        font15.setPointSize(9)
        self.pushButton.setFont(font15)
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/16x16/icons/16x16/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon3)

        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)

        self.labelVersion_3 = QLabel(self.frame_content_wid_1)
        self.labelVersion_3.setObjectName(u"labelVersion_3")
        self.labelVersion_3.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.labelVersion_3.setLineWidth(1)
        self.labelVersion_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.labelVersion_3, 1, 0, 1, 2)


        self.horizontalLayout_9.addLayout(self.gridLayout)


        self.verticalLayout_7.addWidget(self.frame_content_wid_1)


        self.verticalLayout_15.addWidget(self.frame_div_content_1)


        self.verticalLayout_6.addWidget(self.frame)

        self.frame_2 = QFrame(self.page_widgets_deprecated)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 150))
        self.frame_2.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_2)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.checkBox = QCheckBox(self.frame_2)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setAutoFillBackground(False)
        self.checkBox.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.checkBox, 0, 0, 1, 1)

        self.radioButton = QRadioButton(self.frame_2)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.radioButton, 0, 1, 1, 1)

        self.verticalSlider = QSlider(self.frame_2)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setStyleSheet(u"")
        self.verticalSlider.setOrientation(Qt.Vertical)

        self.gridLayout_2.addWidget(self.verticalSlider, 0, 2, 3, 1)

        self.verticalScrollBar = QScrollBar(self.frame_2)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setStyleSheet(u" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }")
        self.verticalScrollBar.setOrientation(Qt.Vertical)

        self.gridLayout_2.addWidget(self.verticalScrollBar, 0, 4, 3, 1)

        self.scrollArea = QScrollArea(self.frame_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"QScrollArea {\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 218, 218))
        self.horizontalLayout_11 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.textEdit = QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(200, 200))
        self.textEdit.setStyleSheet(u"QTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"}\n"
"QTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.horizontalLayout_11.addWidget(self.textEdit)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_2.addWidget(self.scrollArea, 0, 5, 3, 1)

        self.comboBox = QComboBox(self.frame_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setFont(font15)
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}")
        self.comboBox.setIconSize(QSize(16, 16))
        self.comboBox.setFrame(True)

        self.gridLayout_2.addWidget(self.comboBox, 1, 0, 1, 2)

        self.horizontalScrollBar = QScrollBar(self.frame_2)
        self.horizontalScrollBar.setObjectName(u"horizontalScrollBar")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.horizontalScrollBar.sizePolicy().hasHeightForWidth())
        self.horizontalScrollBar.setSizePolicy(sizePolicy6)
        self.horizontalScrollBar.setStyleSheet(u"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"")
        self.horizontalScrollBar.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalScrollBar, 1, 3, 1, 1)

        self.commandLinkButton = QCommandLinkButton(self.frame_2)
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        self.commandLinkButton.setStyleSheet(u"QCommandLinkButton {	\n"
"	color: rgb(85, 170, 255);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(210, 210, 210);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(210, 210, 210);\n"
"	background-color: rgb(52, 58, 71);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/16x16/icons/16x16/cil-link.png", QSize(), QIcon.Normal, QIcon.Off)
        self.commandLinkButton.setIcon(icon4)

        self.gridLayout_2.addWidget(self.commandLinkButton, 1, 6, 1, 1)

        self.horizontalSlider = QSlider(self.frame_2)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setStyleSheet(u"")
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalSlider, 2, 0, 1, 2)


        self.verticalLayout_11.addLayout(self.gridLayout_2)


        self.verticalLayout_6.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.page_widgets_deprecated)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 150))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.frame_3)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tableWidget.rowCount() < 16):
            self.tableWidget.setRowCount(16)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font2);
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget.setItem(0, 3, __qtablewidgetitem23)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        brush15 = QBrush(QColor(39, 44, 54, 255))
        brush15.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush15)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush15)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush15)
        brush16 = QBrush(QColor(210, 210, 210, 128))
        brush16.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush16)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush15)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush15)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush15)
        brush17 = QBrush(QColor(210, 210, 210, 128))
        brush17.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush17)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush15)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush15)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush15)
        brush18 = QBrush(QColor(210, 210, 210, 128))
        brush18.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush18)
#endif
        self.tableWidget.setPalette(palette1)
        self.tableWidget.setStyleSheet(u"QTableWidget {	\n"
"	background-color: rgb(39, 44, 54);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: rgb(39, 44, 54);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
""
                        "QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"")
        self.tableWidget.setFrameShape(QFrame.NoFrame)
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setStretchLastSection(True)

        self.horizontalLayout_12.addWidget(self.tableWidget)


        self.verticalLayout_6.addWidget(self.frame_3)

        self.stackedWidget.addWidget(self.page_widgets_deprecated)
        self.page_widgets = QWidget()
        self.page_widgets.setObjectName(u"page_widgets")
        self.gridLayout_3 = QGridLayout(self.page_widgets)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame_16 = QFrame(self.page_widgets)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.formLayout_25 = QFormLayout(self.frame_16)
        self.formLayout_25.setObjectName(u"formLayout_25")
        self.textEdit_2 = QTextEdit(self.frame_16)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setMinimumSize(QSize(200, 200))
        self.textEdit_2.setStyleSheet(u"QTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"}\n"
"QTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.textEdit_2.setReadOnly(True)

        self.formLayout_25.setWidget(0, QFormLayout.FieldRole, self.textEdit_2)


        self.gridLayout_3.addWidget(self.frame_16, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_widgets)

        self.verticalLayout_9.addWidget(self.stackedWidget)


        self.verticalLayout_4.addWidget(self.frame_content)

        self.frame_grip = QFrame(self.frame_content_right)
        self.frame_grip.setObjectName(u"frame_grip")
        self.frame_grip.setMinimumSize(QSize(0, 25))
        self.frame_grip.setMaximumSize(QSize(16777215, 25))
        self.frame_grip.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.frame_grip.setFrameShape(QFrame.NoFrame)
        self.frame_grip.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_grip)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 2, 0)
        self.frame_label_bottom = QFrame(self.frame_grip)
        self.frame_label_bottom.setObjectName(u"frame_label_bottom")
        self.frame_label_bottom.setFrameShape(QFrame.NoFrame)
        self.frame_label_bottom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_label_bottom)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(10, 0, 10, 0)
        self.label_credits = QLabel(self.frame_label_bottom)
        self.label_credits.setObjectName(u"label_credits")
        self.label_credits.setFont(font2)
        self.label_credits.setStyleSheet(u"color: rgb(98, 103, 111);")

        self.horizontalLayout_7.addWidget(self.label_credits)

        self.label_version = QLabel(self.frame_label_bottom)
        self.label_version.setObjectName(u"label_version")
        self.label_version.setMaximumSize(QSize(100, 16777215))
        self.label_version.setFont(font2)
        self.label_version.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.label_version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_version)


        self.horizontalLayout_6.addWidget(self.frame_label_bottom)

        self.frame_size_grip = QFrame(self.frame_grip)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMaximumSize(QSize(20, 20))
        self.frame_size_grip.setStyleSheet(u"QSizeGrip {\n"
"	background-image: url(:/16x16/icons/16x16/cil-size-grip.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}")
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.frame_size_grip)


        self.verticalLayout_4.addWidget(self.frame_grip)


        self.horizontalLayout_2.addWidget(self.frame_content_right)


        self.verticalLayout.addWidget(self.frame_center)


        self.horizontalLayout.addWidget(self.frame_main)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.btn_minimize, self.btn_maximize_restore)
        QWidget.setTabOrder(self.btn_maximize_restore, self.btn_close)
        QWidget.setTabOrder(self.btn_close, self.btn_toggle_menu)
        QWidget.setTabOrder(self.btn_toggle_menu, self.checkBox)
        QWidget.setTabOrder(self.checkBox, self.comboBox)
        QWidget.setTabOrder(self.comboBox, self.radioButton)
        QWidget.setTabOrder(self.radioButton, self.horizontalSlider)
        QWidget.setTabOrder(self.horizontalSlider, self.verticalSlider)
        QWidget.setTabOrder(self.verticalSlider, self.scrollArea)
        QWidget.setTabOrder(self.scrollArea, self.tableWidget)
        QWidget.setTabOrder(self.tableWidget, self.commandLinkButton)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(15)
        self.Basic1French_StackedWidget.setCurrentIndex(0)
        self.Basic2French_StackedWidget.setCurrentIndex(0)
        self.Basic1Spanish_StackedWidget.setCurrentIndex(0)
        self.Basic2Spanish_StackedWidget.setCurrentIndex(0)
        self.Basic1Italian_StackedWidget.setCurrentIndex(0)
        self.Basic2Italian_StackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_toggle_menu.setText("")
        self.label_title_bar_top.setText(QCoreApplication.translate("MainWindow", u"Main Course Window", None))
#if QT_CONFIG(tooltip)
        self.btn_minimize.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_minimize.setText("")
#if QT_CONFIG(tooltip)
        self.btn_maximize_restore.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_maximize_restore.setText("")
#if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.btn_close.setText("")
        self.label_top_info_2.setText(QCoreApplication.translate("MainWindow", u"|HOME|", None))
        self.Level_Basic1.setText(QCoreApplication.translate("MainWindow", u"Basic 1", None))
        self.Level_Basic2.setText(QCoreApplication.translate("MainWindow", u"Basic 2", None))
        self.Level_Basic1_Spanish.setText(QCoreApplication.translate("MainWindow", u"Basic 1", None))
        self.Level_Basic2_Spanish.setText(QCoreApplication.translate("MainWindow", u"Basic 2", None))
        self.Level_Basic2_Italian.setText(QCoreApplication.translate("MainWindow", u"Basic 2", None))
        self.Level_Basic1_Italian.setText(QCoreApplication.translate("MainWindow", u"Basic 1", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Basic 1:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:22pt; font-weight:600; color:#ffffff;\">Common words and their meaning:</span></p><p><span style=\" color:#ffffff;\">* Je = I</span></p><p><span style=\" color:#ffffff;\">* Suis = Am</span></p><p><span style=\" color:#ffffff;\">* gar\u00e7on = boy</span></p><p><span style=\" color:#ffffff;\">* fille = girl</span></p><p><span style=\" color:#ffffff;\">* Homme = man</span></p><p><span style=\" color:#ffffff;\">* Femme = Woman</span></p><p><span style=\" color:#ffffff;\">* Fran\u00e7ais = French</span></p><p><span style=\" color:#ffffff;\">* Oui = Yes</span></p><p><span style=\" color:#ffffff;\">* Non = No</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:22pt; font-weight:600; color:#ffffff;\">Common animals and places names:</span></p><p><span style=\" color:#ffffff;\">* Chat = cat</span></p><p><span style=\" color:#ffffff;\">* Chien = dog</span></p><p><span style=\" color:#ffffff;\">* Rate = rat</span></p><p><span style=\" color:#ffffff;\">* Vache = cow</span></p><p><span style=\" color:#ffffff;\">* parc = park</span></p><p><span style=\" color:#ffffff;\">* </span><a name=\"tw-target-text\"/><span style=\" font-family:'Google Sans','arial','sans-serif'; font-size:16pt; color:#ffffff;\">\u00e9</span><span style=\" font-family:'Google Sans','arial','sans-serif'; font-size:16pt; color:#ffffff;\">cole = school</span></p><p><a name=\"tw-target-text\"/><span style=\" font-family:'Google Sans','arial','sans-serif'; font-size:16pt; color:#ffffff;\">*</span><span style=\" font-family:'Google Sans','arial','sans-serif'; font-size:16pt; color:#ffffff;\"> maison = house</span></p><p><a name=\"tw-target-text\"/><span style=\""
                        " font-family:'Google Sans','arial','sans-serif'; font-size:16pt; color:#ffffff;\">*</span><span style=\" font-family:'Google Sans','arial','sans-serif'; font-size:16pt; color:#ffffff;\"> domicile = home</span></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:22pt; font-weight:600; color:#ffffff;\">Common greetings:</span></p><p><span style=\" font-size:16pt; color:#ffffff;\">* Bonjour = Hello, good morning.</span></p><p><span style=\" font-size:16pt; color:#ffffff;\">* Au revoir = Goodbye.</span></p><p><span style=\" font-size:16pt; color:#ffffff;\">* Merci = Thank you.</span></p><p><span style=\" font-size:16pt; color:#ffffff;\">* Bonsoir = Good Morning.</span></p><p><span style=\" font-size:16pt; color:#ffffff;\">* Bonne nuit = Good Night.</span></p><p><span style=\" font-size:16pt; color:#ffffff;\">* De rien = You're welcome. (Informal)</span></p><p><span style=\" font-size:16pt; color:#ffffff;\">* Je vous en prie = You're welcome. (Formal)</span></p><p><span style=\" font-size:16pt; color:#ffffff;\">* Comment ca va = How are you?</span></p></body></html>", None))
        self.Basic1FrenchNavButtonLeft.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.Basic1FrenchNavButtonRight.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Basic 2:", None))
        self.Basic2FrenchNavButtonLeft.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.Basic2FrenchNavButtonRight.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:22pt; font-weight:600; color:#ffffff;\">Basic words and their meaning:</span></p><p><span style=\" color:#ffffff;\">* un = a/an (singular masculine)</span></p><p><span style=\" color:#ffffff;\">* une = a/an (singular feminine)</span></p><p><span style=\" color:#ffffff;\">* les = the (plural masculine/feminine)</span></p><p><span style=\" color:#ffffff;\">* le (l') = the (singular masculine)</span></p><p><span style=\" color:#ffffff;\">* la(l') = the (singular feminine)</span></p><p><span style=\" color:#ffffff;\">* sont = are</span></p><p><span style=\" color:#ffffff;\">* et = and</span></p><p><span style=\" color:#ffffff;\">* est = is</span></p><p><span style=\" color:#ffffff;\">* ceci = this</span></p><p><span style=\" color:#ffffff;\">* c'est = that<br/></span></p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:22pt; font-weight:600; color:#ffffff;\">Basic sentences and their meaning:</span></p><p><span style=\" color:#ffffff;\">* Le chat et le chien. = A cat and a dog.</span></p><p><span style=\" color:#ffffff;\">* Je suis un gar</span><a name=\"tw-target-text\"/><span style=\" font-family:'Google Sans','arial','sans-serif'; font-size:16pt; color:#ffffff;\">\u00e7</span><span style=\" font-family:'Google Sans','arial','sans-serif'; font-size:16pt; color:#ffffff;\">on.</span><span style=\" color:#ffffff;\"> = I am a boy.</span></p><p><span style=\" color:#ffffff;\">* Je suis une fille. = I am a girl.</span></p><p><span style=\" color:#ffffff;\">* Je suis un homme. = I am a man.</span></p><p><span style=\" color:#ffffff;\">* Je suis une femme. = I am a woman.</span></p><p><span style=\" color:#ffffff;\">* Ceci est un chat. = This is a cat.</span></p><p><span style=\" color:#ffffff;\">* C'est un chien. = That is a dog.</span></p></body></html>", None))
        self.Basic1SpanishNavButtonLeft.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.Basic1SpanishNavButtonRight.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:22pt; font-weight:600; color:#ffffff;\">Common words and their meaning:</span></p><p><span style=\" color:#ffffff;\">* Yo = I</span></p><p><span style=\" color:#ffffff;\">* Soy = Am</span></p><p><span style=\" color:#ffffff;\">* Chico = Boy</span></p><p><span style=\" color:#ffffff;\">* </span><a name=\"tw-target-text\"/><span style=\" font-family:'Google Sans','arial','sans-serif'; font-size:16pt; color:#ffffff;\">n</span><span style=\" font-family:'Google Sans','arial','sans-serif'; font-size:16pt; color:#ffffff;\">i\u00f1a = girl</span></p><p><span style=\" color:#ffffff;\">* Hombre = man</span></p><p><span style=\" color:#ffffff;\">* mujer = Woman</span></p><p><span style=\" color:#ffffff;\">* </span><a name=\"tw-target-text-masculine\"/><span style=\" font-family:'Google Sans','arial','sans-serif'; font-size:16pt; color:#ffffff;\">E</span><span style=\" font-family:'Google Sans','arial','sans-serif'; font-size:16pt; color:#ffffff;\">spa\u00f1ol</span><span st"
                        "yle=\" color:#ffffff;\"> = Spanish</span></p><p><span style=\" color:#ffffff;\">* Si = Yes</span></p><p><span style=\" color:#ffffff;\">* No = No</span></p></body></html>", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:22pt; font-weight:600; color:#ffffff;\">Common animals and places names:</span></p><p><span style=\" color:#ffffff;\">* gata = cat</span></p><p><span style=\" color:#ffffff;\">* pero = dog</span></p><p><span style=\" color:#ffffff;\">* rato = rat</span></p><p><span style=\" color:#ffffff;\">* vaca = cow</span></p><p><span style=\" color:#ffffff;\">* parque = park</span></p><p><span style=\" color:#ffffff;\">* </span><span style=\" font-family:'Google Sans','arial','sans-serif'; font-size:16pt; color:#ffffff;\">colegio = school</span></p><p><a name=\"tw-target-text\"/><span style=\" font-family:'Google Sans','arial','sans-serif'; font-size:16pt; color:#ffffff;\">*</span><span style=\" font-family:'Google Sans','arial','sans-serif'; font-size:16pt; color:#ffffff;\"> casa = house</span></p><p><a name=\"tw-target-text\"/><span style=\" font-family:'Google Sans','arial','sans-serif'; font-size:16pt; color:#ffffff;\">*</span><span style=\" font-family:'Google Sans','ari"
                        "al','sans-serif'; font-size:16pt; color:#ffffff;\"> hogar = home</span></p></body></html>", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:22pt; font-weight:600; color:#ffffff;\">Common greetings:</span></p><p><span style=\" font-size:16pt; color:#ffffff;\">* Hola = Hello</span></p><p><span style=\" font-size:16pt; color:#ffffff;\">* Adios = Goodbye.</span></p><p><span style=\" font-size:16pt; color:#ffffff;\">* Garcias = Thank you.</span></p><p><span style=\" font-size:16pt; color:#ffffff;\">* Buenos dias = Good Morning.</span></p><p><span style=\" font-size:16pt; color:#ffffff;\">* Buenos noches = Good Night.</span></p><p><span style=\" font-size:16pt; color:#ffffff;\">* De nada = You're welcome.</span></p><p><span style=\" font-size:16pt; color:#ffffff;\">* </span><span style=\" font-family:'Google Sans','arial','sans-serif'; font-size:16pt; color:#ffffff;\">C\u00f3mo est\u00e1s</span><span style=\" font-size:16pt; color:#ffffff;\"> = How are you?</span><span style=\" color:#ffffff;\"><br/><br/></span></p></body></html>", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Basic 1:", None))
        self.Basic2SpanishNavButtonLeft.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.Basic2SpanishNavButtonRight.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:22pt; font-weight:600; color:#ffffff;\">Basic words and their meaning:</span></p><p><span style=\" color:#ffffff;\">* una = a/an (singular masculine)</span></p><p><span style=\" color:#ffffff;\">* uno = a/an (singular feminine)</span></p><p><span style=\" color:#ffffff;\">* la = the (feminine)</span></p><p><span style=\" color:#ffffff;\">* el = the (masculine)</span></p><p><span style=\" color:#ffffff;\">* son = are</span></p><p><span style=\" color:#ffffff;\">* y = and</span></p><p><span style=\" color:#ffffff;\">* es = is</span></p><p><span style=\" color:#ffffff;\">* esto = this</span></p><p><span style=\" color:#ffffff;\">* ese = that<br/></span></p></body></html>", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:22pt; font-weight:600; color:#ffffff;\">Basic sentences and their meaning:</span></p><p><span style=\" color:#ffffff;\">* Un gato y un perro. = A cat and a dog.</span></p><p><span style=\" color:#ffffff;\">* Soy un chico</span><span style=\" font-family:'Google Sans','arial','sans-serif'; font-size:16pt; color:#ffffff;\">.</span><span style=\" color:#ffffff;\"> = I am a boy.</span></p><p><span style=\" color:#ffffff;\">* Soy una nina. = I am a girl.</span></p><p><span style=\" color:#ffffff;\">* Soy un hombre. = I am a man.</span></p><p><span style=\" color:#ffffff;\">* Soy una mujer. = I am a woman.</span></p><p><span style=\" color:#ffffff;\">* Este es un gato. = This is a cat.</span></p><p><span style=\" color:#ffffff;\">* Eso es un perro. = That is a dog.</span></p></body></html>", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Basic 2:", None))
        self.Basic1ItalianNavButtonLeft.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.Basic1ItalianNavButtonRight.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:22pt; font-weight:600; color:#ffffff;\">Common words and their meaning:</span></p><p><span style=\" color:#ffffff;\">* io = I</span></p><p><span style=\" color:#ffffff;\">* sono = Am</span></p><p><span style=\" color:#ffffff;\">* ragazzo = boy</span></p><p><span style=\" color:#ffffff;\">* ragazza = girl</span></p><p><span style=\" color:#ffffff;\">* uomo = man</span></p><p><span style=\" color:#ffffff;\">* donna = Woman</span></p><p><span style=\" color:#ffffff;\">* italiano = French</span></p><p><span style=\" color:#ffffff;\">* si = Yes</span></p><p><span style=\" color:#ffffff;\">* No = No</span></p></body></html>", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:22pt; font-weight:600; color:#ffffff;\">Common animals and places names:</span></p><p><span style=\" color:#ffffff;\">* gatto = cat</span></p><p><span style=\" color:#ffffff;\">* cane = dog</span></p><p><span style=\" color:#ffffff;\">* ratto = rat</span></p><p><span style=\" color:#ffffff;\">* mucca = cow</span></p><p><span style=\" color:#ffffff;\">* parco = park</span></p><p><span style=\" color:#ffffff;\">* scuola</span><span style=\" font-family:'Google Sans','arial','sans-serif'; font-size:16pt; color:#ffffff;\"> = school</span></p><p><a name=\"tw-target-text\"/><span style=\" font-family:'Google Sans','arial','sans-serif'; font-size:16pt; color:#ffffff;\">*</span><span style=\" font-family:'Google Sans','arial','sans-serif'; font-size:16pt; color:#ffffff;\"> casa = house</span></p><p><a name=\"tw-target-text\"/><span style=\" font-family:'Google Sans','arial','sans-serif'; font-size:16pt; color:#ffffff;\">*</span><span style=\" font-family:'Google Sans','ar"
                        "ial','sans-serif'; font-size:16pt; color:#ffffff;\"> casa = home</span></p></body></html>", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:22pt; font-weight:600; color:#ffffff;\">Common greetings:</span></p><p><span style=\" font-size:16pt; color:#ffffff;\">* Ciao = Hello, good morning.</span></p><p><span style=\" font-size:16pt; color:#ffffff;\">* addio = Goodbye.</span></p><p><span style=\" font-size:16pt; color:#ffffff;\">* grazie = Thank you.</span></p><p><span style=\" font-size:16pt; color:#ffffff;\">* Buongiorno = Good Morning.</span></p><p><span style=\" font-size:16pt; color:#ffffff;\">* Buona notte = Good Night.</span></p><p><span style=\" font-size:16pt; color:#ffffff;\">* Prego = You're welcome.</span></p><p><span style=\" font-size:16pt; color:#ffffff;\">* Come stai = How are you?</span></p></body></html>", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Basic 1:", None))
        self.Basic2ItalianNavButtonLeft.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.Basic2ItalianNavButtonRight.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:22pt; font-weight:600; color:#ffffff;\">Basic words and their meaning:</span></p><p><span style=\" color:#ffffff;\">* un = a/an (singular masculine)</span></p><p><span style=\" color:#ffffff;\">* una = a/an (singular feminine)</span></p><p><span style=\" color:#ffffff;\">* il = the (singular masculine)</span></p><p><span style=\" color:#ffffff;\">* la = the (singular feminine)</span></p><p><span style=\" color:#ffffff;\">* siamo = are</span></p><p><span style=\" color:#ffffff;\">* e = and</span></p><p><span style=\" color:#ffffff;\">* </span><a name=\"tw-target-text\"/><span style=\" font-family:'Google Sans','arial','sans-serif'; font-size:16pt; color:#ffffff;\">\u00e8</span><span style=\" color:#ffffff;\"> = is</span></p><p><span style=\" color:#ffffff;\">* questo = this</span></p><p><span style=\" color:#ffffff;\">* quello = that<br/></span></p></body></html>", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:22pt; font-weight:600; color:#ffffff;\">Basic sentences and their meaning:</span></p><p><span style=\" color:#ffffff;\">* Un gatto e un cane. = A cat and a dog.</span></p><p><span style=\" color:#ffffff;\">* Sono un ragazzo</span><span style=\" font-family:'Google Sans','arial','sans-serif'; font-size:16pt; color:#ffffff;\">.</span><span style=\" color:#ffffff;\"> = I am a boy.</span></p><p><span style=\" color:#ffffff;\">* Sono una ragazzina. = I am a girl.</span></p><p><span style=\" color:#ffffff;\">* Sono un uomo. = I am a man.</span></p><p><span style=\" color:#ffffff;\">* lo sono una donna. = I am a woman.</span></p><p><span style=\" color:#ffffff;\">* </span><span style=\" font-family:'Google Sans','arial','sans-serif'; font-size:16pt; color:#ffffff;\">Questo \u00e8 un gatto</span><span style=\" color:#ffffff;\">. = This is a cat.</span></p><p><span style=\" color:#ffffff;\">* </span><a name=\"tw-target-text\"/><span style=\" font-family:'Google Sans','aria"
                        "l','sans-serif'; font-size:16pt; color:#ffffff;\">Q</span><span style=\" font-family:'Google Sans','arial','sans-serif'; font-size:16pt; color:#ffffff;\">uesto \u00e8 un cane</span><span style=\" color:#ffffff;\">. = That is a dog.</span></p></body></html>", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Basic 2:", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Quizes", None))
        self.QuizButton_French.setText(QCoreApplication.translate("MainWindow", u"FRENCH", None))
        self.QuizButton_Italian.setText(QCoreApplication.translate("MainWindow", u"ITALIAN", None))
        self.QuizButton_Spanish.setText(QCoreApplication.translate("MainWindow", u"SPANISH", None))
        self.QuizOutputPage_OutputLabel.setText(QCoreApplication.translate("MainWindow", u"Correct/Wrong Answer!", None))
        self.QuizOutputPage_CorrectAnswer.setText(QCoreApplication.translate("MainWindow", u"Correct answer was: asxasdxwadx", None))
        self.QuizOutputPage_NextButton.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.FrenchQuiz_QuestionText.setText(QCoreApplication.translate("MainWindow", u"Lorem Ipsum", None))
        self.FrenchQuizButton_Submit.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.FrenchQuizRadioButton_1.setText(QCoreApplication.translate("MainWindow", u"Test1", None))
        self.FrenchQuizRadioButton_2.setText(QCoreApplication.translate("MainWindow", u"Test1", None))
        self.FrenchQuizRadioButton_3.setText(QCoreApplication.translate("MainWindow", u"Test1", None))
        self.FrenchQuizButton_Skip.setText(QCoreApplication.translate("MainWindow", u"Skip", None))
        self.SpanishQuiz_QuestionText.setText(QCoreApplication.translate("MainWindow", u"Lorem Ipsum", None))
        self.SpanishQuizRadioButton_1.setText(QCoreApplication.translate("MainWindow", u"Test1", None))
        self.SpanishQuizRadioButton_2.setText(QCoreApplication.translate("MainWindow", u"Test1", None))
        self.SpanishQuizRadioButton_3.setText(QCoreApplication.translate("MainWindow", u"Test1", None))
        self.SpanishQuizButton_Submit.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.SpanishQuizButton_Skip.setText(QCoreApplication.translate("MainWindow", u"Skip", None))
        self.ItalianQuizRadioButton_1.setText(QCoreApplication.translate("MainWindow", u"Test1", None))
        self.ItalianQuizRadioButton_2.setText(QCoreApplication.translate("MainWindow", u"Test1", None))
        self.ItalianQuizRadioButton_3.setText(QCoreApplication.translate("MainWindow", u"Test1", None))
        self.ItalianQuizButton_Submit.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.ItalianQuizButton_Skip.setText(QCoreApplication.translate("MainWindow", u"Skip", None))
        self.ItalianQuiz_QuestionText.setText(QCoreApplication.translate("MainWindow", u"Lorem Ipsum", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Courses:", None))
        self.SubjectButton_French.setText(QCoreApplication.translate("MainWindow", u"FRENCH", None))
        self.SubjectButton_Italian.setText(QCoreApplication.translate("MainWindow", u"ITALIAN", None))
        self.SubjectButton_Spanish.setText(QCoreApplication.translate("MainWindow", u"SPANISH", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Courses Enrolled:- ", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Quizes Played:- ", None))
        self.CoursesEnrolled_Text.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.QuizesDone_Text.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Your Stats;", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Quizes Passed:-", None))
        self.QuizesPassed_Txt.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.QuizesFails_Txt.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Quizes Fails:-", None))
        self.labelBoxBlenderInstalation.setText(QCoreApplication.translate("MainWindow", u"BLENDER INSTALLATION", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Your Password", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Open Blender", None))
        self.labelVersion_3.setText(QCoreApplication.translate("MainWindow", u"Ex: C:Program FilesBlender FoundationBlender 2.82 blender.exe", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Test 1", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Test 2", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Test 3", None))

        self.commandLinkButton.setText(QCoreApplication.translate("MainWindow", u"CommandLinkButton", None))
        self.commandLinkButton.setDescription(QCoreApplication.translate("MainWindow", u"Open External Link", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem9 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem10 = self.tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem11 = self.tableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem12 = self.tableWidget.verticalHeaderItem(8)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem13 = self.tableWidget.verticalHeaderItem(9)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem14 = self.tableWidget.verticalHeaderItem(10)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem15 = self.tableWidget.verticalHeaderItem(11)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem16 = self.tableWidget.verticalHeaderItem(12)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem17 = self.tableWidget.verticalHeaderItem(13)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem18 = self.tableWidget.verticalHeaderItem(14)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem19 = self.tableWidget.verticalHeaderItem(15)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem20 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Test", None));
        ___qtablewidgetitem21 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Text", None));
        ___qtablewidgetitem22 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Cell", None));
        ___qtablewidgetitem23 = self.tableWidget.item(0, 3)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Line", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.textEdit_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt; font-weight:600; text-decoration: underline; color:#00aaff;\">Changelog</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">* Version 1.0 Released</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-l"
                        "eft:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_credits.setText(QCoreApplication.translate("MainWindow", u"Nomz#2168", None))
        self.label_version.setText(QCoreApplication.translate("MainWindow", u"v1.0.0", None))
    # retranslateUi

