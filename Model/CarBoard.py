# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CarBoard.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QSize(1280, 720))
        font = QFont()
        font.setFamilies([u"Tahoma"])
        font.setPointSize(12)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnLeftLayout = QVBoxLayout()
        self.btnLeftLayout.setObjectName(u"btnLeftLayout")
        self.btnLeftLayout.setContentsMargins(50, 0, 50, 0)
        self.GPSButton = QPushButton(self.centralwidget)
        self.GPSButton.setObjectName(u"GPSButton")
        sizePolicy.setHeightForWidth(self.GPSButton.sizePolicy().hasHeightForWidth())
        self.GPSButton.setSizePolicy(sizePolicy)
        self.GPSButton.setMinimumSize(QSize(130, 90))
        self.GPSButton.setFont(font)
        self.GPSButton.setStyleSheet(u"QPushButton{\n"
"	color: white;\n"
"	background-color: black;\n"
"	border-radius:10px;\n"
"}\n"
"")
        self.GPSButton.setCheckable(True)

        self.btnLeftLayout.addWidget(self.GPSButton)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.btnLeftLayout.addWidget(self.line)

        self.HomeButton = QPushButton(self.centralwidget)
        self.HomeButton.setObjectName(u"HomeButton")
        sizePolicy.setHeightForWidth(self.HomeButton.sizePolicy().hasHeightForWidth())
        self.HomeButton.setSizePolicy(sizePolicy)
        self.HomeButton.setMinimumSize(QSize(130, 90))
        self.HomeButton.setFont(font)
        self.HomeButton.setStyleSheet(u"QPushButton{\n"
"	color: white;\n"
"	background-color: black;\n"
"	border-radius:10px;\n"
"}\n"
"")
        self.HomeButton.setCheckable(True)

        self.btnLeftLayout.addWidget(self.HomeButton)


        self.horizontalLayout.addLayout(self.btnLeftLayout)

        self.btnRightLayout = QVBoxLayout()
        self.btnRightLayout.setSpacing(7)
        self.btnRightLayout.setObjectName(u"btnRightLayout")
        self.btnRightLayout.setContentsMargins(50, -1, 50, -1)
        self.AVButton = QPushButton(self.centralwidget)
        self.AVButton.setObjectName(u"AVButton")
        sizePolicy.setHeightForWidth(self.AVButton.sizePolicy().hasHeightForWidth())
        self.AVButton.setSizePolicy(sizePolicy)
        self.AVButton.setMinimumSize(QSize(130, 90))
        self.AVButton.setFont(font)
        self.AVButton.setStyleSheet(u"QPushButton{\n"
"	color: white;\n"
"	background-color: black;\n"
"	border-radius: 10px;\n"
"}\n"
"")
        self.AVButton.setCheckable(True)

        self.btnRightLayout.addWidget(self.AVButton)

        self.line_4 = QFrame(self.centralwidget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.btnRightLayout.addWidget(self.line_4)

        self.VCButton = QPushButton(self.centralwidget)
        self.VCButton.setObjectName(u"VCButton")
        sizePolicy.setHeightForWidth(self.VCButton.sizePolicy().hasHeightForWidth())
        self.VCButton.setSizePolicy(sizePolicy)
        self.VCButton.setMinimumSize(QSize(130, 90))
        self.VCButton.setFont(font)
        self.VCButton.setStyleSheet(u"QPushButton{\n"
"	color: white;\n"
"	background-color: black;\n"
"	border-radius:10px;\n"
"}\n"
"")
        self.VCButton.setCheckable(True)

        self.btnRightLayout.addWidget(self.VCButton)


        self.horizontalLayout.addLayout(self.btnRightLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.GPSButton.setText(QCoreApplication.translate("MainWindow", u"GPS", None))
        self.HomeButton.setText(QCoreApplication.translate("MainWindow", u"HOME", None))
        self.AVButton.setText(QCoreApplication.translate("MainWindow", u"Audio/Video", None))
        self.VCButton.setText(QCoreApplication.translate("MainWindow", u"Voice Control", None))
    # retranslateUi

