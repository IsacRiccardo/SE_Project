# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Home.ui'
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
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QSlider, QSpacerItem, QVBoxLayout,
    QWidget)
from UI import resources_rc

class Ui_Home(object):
    def setupUi(self, Home):
        if not Home.objectName():
            Home.setObjectName(u"Home")
        Home.resize(790, 702)
        font = QFont()
        font.setFamilies([u"Tahoma"])
        font.setPointSize(12)
        Home.setFont(font)
        self.verticalLayout = QVBoxLayout(Home)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, -1, 5, -1)
        self.CurrentSongLabel = QLabel(Home)
        self.CurrentSongLabel.setObjectName(u"CurrentSongLabel")
        self.CurrentSongLabel.setFont(font)

        self.verticalLayout_2.addWidget(self.CurrentSongLabel)

        self.MusicSlider = QSlider(Home)
        self.MusicSlider.setObjectName(u"MusicSlider")
        self.MusicSlider.setOrientation(Qt.Horizontal)

        self.verticalLayout_2.addWidget(self.MusicSlider)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.PreviousButton = QPushButton(Home)
        self.PreviousButton.setObjectName(u"PreviousButton")
        self.PreviousButton.setMinimumSize(QSize(70, 40))
        self.PreviousButton.setFont(font)
        self.PreviousButton.setStyleSheet(u"border-radius : 10px; border : 2px solid black; padding:10px;\n"
"background-color: rgb(255, 255, 255);")
        icon = QIcon()
        icon.addFile(u":/Icons/Icons/step-backward-icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.PreviousButton.setIcon(icon)

        self.horizontalLayout.addWidget(self.PreviousButton)

        self.PlayPauseButton = QPushButton(Home)
        self.PlayPauseButton.setObjectName(u"PlayPauseButton")
        self.PlayPauseButton.setMinimumSize(QSize(70, 40))
        self.PlayPauseButton.setFont(font)
        self.PlayPauseButton.setStyleSheet(u"border-radius : 10px; border : 2px solid black; padding:10px;\n"
"background-color: rgb(255, 255, 255);")
        icon1 = QIcon()
        icon1.addFile(u":/Icons/Icons/play-pause-icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.PlayPauseButton.setIcon(icon1)
        self.PlayPauseButton.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.PlayPauseButton)

        self.NextButton = QPushButton(Home)
        self.NextButton.setObjectName(u"NextButton")
        self.NextButton.setMinimumSize(QSize(70, 40))
        self.NextButton.setFont(font)
        self.NextButton.setStyleSheet(u"border-radius : 10px; border : 2px solid black; padding:10px;\n"
"background-color: rgb(255, 255, 255);")
        icon2 = QIcon()
        icon2.addFile(u":/Icons/Icons/step-forward-icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.NextButton.setIcon(icon2)

        self.horizontalLayout.addWidget(self.NextButton)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.GPSLayout = QHBoxLayout()
        self.GPSLayout.setObjectName(u"GPSLayout")
        self.webEngineView = QWebEngineView(Home)
        self.webEngineView.setObjectName(u"webEngineView")
        self.webEngineView.setMinimumSize(QSize(0, 400))
        self.webEngineView.setUrl(QUrl(u"https://www.google.com/maps/@45.7266998,21.220925,14z?ucbcb=1&entry=ttu"))

        self.GPSLayout.addWidget(self.webEngineView)


        self.verticalLayout.addLayout(self.GPSLayout)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.VCLayout = QHBoxLayout()
        self.VCLayout.setObjectName(u"VCLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.VCLayout.addItem(self.horizontalSpacer)

        self.VCButton = QPushButton(Home)
        self.VCButton.setObjectName(u"VCButton")
        self.VCButton.setFont(font)
        self.VCButton.setStyleSheet(u"border-radius : 10px; border : 2px solid black; padding:10px;\n"
"background-color: rgb(255, 255, 255);")
        icon3 = QIcon()
        icon3.addFile(u":/Icons/Icons/microphone-icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.VCButton.setIcon(icon3)
        self.VCButton.setIconSize(QSize(30, 30))

        self.VCLayout.addWidget(self.VCButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.VCLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.VCLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.retranslateUi(Home)

        QMetaObject.connectSlotsByName(Home)
    # setupUi

    def retranslateUi(self, Home):
        Home.setWindowTitle(QCoreApplication.translate("Home", u"Form", None))
        self.CurrentSongLabel.setText(QCoreApplication.translate("Home", u"Current song: ", None))
        self.PreviousButton.setText("")
        self.PlayPauseButton.setText("")
        self.NextButton.setText("")
        self.VCButton.setText("")
    # retranslateUi

