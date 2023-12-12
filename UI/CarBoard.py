# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CarBoard.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QMainWindow,
    QPushButton, QSizePolicy, QStackedWidget, QTabWidget,
    QVBoxLayout, QWidget)
from UI import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1280, 720))
        MainWindow.setMaximumSize(QSize(1000000, 1000000))
        font = QFont()
        font.setFamilies([u"Tahoma"])
        font.setPointSize(12)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/Icons/Icons/dashboard-report-icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"")
        MainWindow.setIconSize(QSize(50, 50))
        MainWindow.setAnimated(True)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QTabWidget.Rounded)
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnLeftLayout = QVBoxLayout()
        self.btnLeftLayout.setObjectName(u"btnLeftLayout")
        self.btnLeftLayout.setContentsMargins(50, 0, 50, 0)
        self.GPSButton = QPushButton(self.centralwidget)
        self.GPSButton.setObjectName(u"GPSButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.GPSButton.sizePolicy().hasHeightForWidth())
        self.GPSButton.setSizePolicy(sizePolicy1)
        self.GPSButton.setMinimumSize(QSize(130, 90))
        self.GPSButton.setFont(font)
        self.GPSButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.GPSButton.setStyleSheet(u"QPushButton{\n"
"	background-color: white;\n"
"	border-radius:10px;\n"
"	border: 2px solid black\n"
"}\n"
"\n"
"QPushButton::checked{\n"
"	background-color: #a6e9ff;\n"
"	border-radius: 10px;\n"
"	border: 2px solid black\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/Icons/Icons/maps-pin-black-icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.GPSButton.setIcon(icon1)
        self.GPSButton.setIconSize(QSize(48, 48))
        self.GPSButton.setCheckable(True)

        self.btnLeftLayout.addWidget(self.GPSButton)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.btnLeftLayout.addWidget(self.line)

        self.HomeButton = QPushButton(self.centralwidget)
        self.HomeButton.setObjectName(u"HomeButton")
        sizePolicy1.setHeightForWidth(self.HomeButton.sizePolicy().hasHeightForWidth())
        self.HomeButton.setSizePolicy(sizePolicy1)
        self.HomeButton.setMinimumSize(QSize(130, 90))
        self.HomeButton.setFont(font)
        self.HomeButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.HomeButton.setStyleSheet(u"QPushButton{\n"
"	background-color: white;\n"
"	border-radius:10px;\n"
"	border: 2px solid black\n"
"}\n"
"\n"
"QPushButton::checked{\n"
"	background-color: #a6e9ff;\n"
"	border-radius: 10px;\n"
"	border: 2px solid black\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/Icons/Icons/home-icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.HomeButton.setIcon(icon2)
        self.HomeButton.setIconSize(QSize(48, 48))
        self.HomeButton.setCheckable(True)

        self.btnLeftLayout.addWidget(self.HomeButton)


        self.horizontalLayout.addLayout(self.btnLeftLayout)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")

        self.horizontalLayout.addWidget(self.stackedWidget)

        self.btnRightLayout = QVBoxLayout()
        self.btnRightLayout.setSpacing(7)
        self.btnRightLayout.setObjectName(u"btnRightLayout")
        self.btnRightLayout.setContentsMargins(50, -1, 50, -1)
        self.AVButton = QPushButton(self.centralwidget)
        self.AVButton.setObjectName(u"AVButton")
        sizePolicy1.setHeightForWidth(self.AVButton.sizePolicy().hasHeightForWidth())
        self.AVButton.setSizePolicy(sizePolicy1)
        self.AVButton.setMinimumSize(QSize(130, 90))
        self.AVButton.setFont(font)
        self.AVButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.AVButton.setStyleSheet(u"QPushButton{\n"
"	background-color: white;\n"
"	border-radius:10px;\n"
"	border: 2px solid black\n"
"}\n"
"\n"
"QPushButton::checked{\n"
"	background-color: #a6e9ff;\n"
"	border-radius: 10px;\n"
"	border: 2px solid black\n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/Icons/Icons/headphone-icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.AVButton.setIcon(icon3)
        self.AVButton.setIconSize(QSize(48, 48))
        self.AVButton.setCheckable(True)

        self.btnRightLayout.addWidget(self.AVButton)

        self.line_4 = QFrame(self.centralwidget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.btnRightLayout.addWidget(self.line_4)

        self.VCButton = QPushButton(self.centralwidget)
        self.VCButton.setObjectName(u"VCButton")
        sizePolicy1.setHeightForWidth(self.VCButton.sizePolicy().hasHeightForWidth())
        self.VCButton.setSizePolicy(sizePolicy1)
        self.VCButton.setMinimumSize(QSize(130, 90))
        self.VCButton.setFont(font)
        self.VCButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.VCButton.setStyleSheet(u"QPushButton{\n"
"	background-color: white;\n"
"	border-radius:10px;\n"
"	border: 2px solid black\n"
"}\n"
"\n"
"QPushButton::checked{\n"
"	background-color: #a6e9ff;\n"
"	border-radius: 10px;\n"
"	border: 2px solid black\n"
"}\n"
"")
        icon4 = QIcon()
        icon4.addFile(u":/Icons/Icons/speak-talk-voice-icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.VCButton.setIcon(icon4)
        self.VCButton.setIconSize(QSize(48, 48))
        self.VCButton.setCheckable(True)

        self.btnRightLayout.addWidget(self.VCButton)


        self.horizontalLayout.addLayout(self.btnRightLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Dash Board", None))
        self.GPSButton.setText("")
        self.HomeButton.setText("")
        self.AVButton.setText("")
        self.VCButton.setText("")
    # retranslateUi

