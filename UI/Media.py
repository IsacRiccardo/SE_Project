# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Media.ui'
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
from PySide6.QtWidgets import (QApplication, QDial, QGridLayout, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSlider,
    QSpacerItem, QVBoxLayout, QWidget)
from UI import resources_rc

class Ui_Media(object):
    def setupUi(self, Media):
        if not Media.objectName():
            Media.setObjectName(u"Media")
        Media.resize(646, 507)
        font = QFont()
        font.setFamilies([u"Tahoma"])
        font.setPointSize(12)
        Media.setFont(font)
        self.gridLayout = QGridLayout(Media)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.ImageLabe = QLabel(Media)
        self.ImageLabe.setObjectName(u"ImageLabe")

        self.horizontalLayout_3.addWidget(self.ImageLabe)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.VolumeDial = QDial(Media)
        self.VolumeDial.setObjectName(u"VolumeDial")
        self.VolumeDial.setMaximumSize(QSize(16777215, 150))

        self.horizontalLayout_3.addWidget(self.VolumeDial)


        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 3, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, -1, 5, -1)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.CurrentSongLabel = QLabel(Media)
        self.CurrentSongLabel.setObjectName(u"CurrentSongLabel")
        self.CurrentSongLabel.setMaximumSize(QSize(100, 50))
        self.CurrentSongLabel.setFont(font)

        self.horizontalLayout_2.addWidget(self.CurrentSongLabel)

        self.CurrentSong = QLabel(Media)
        self.CurrentSong.setObjectName(u"CurrentSong")
        self.CurrentSong.setMaximumSize(QSize(16777215, 50))

        self.horizontalLayout_2.addWidget(self.CurrentSong)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.MusicSlider = QSlider(Media)
        self.MusicSlider.setObjectName(u"MusicSlider")
        self.MusicSlider.setOrientation(Qt.Horizontal)

        self.verticalLayout_2.addWidget(self.MusicSlider)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.PreviousButton = QPushButton(Media)
        self.PreviousButton.setObjectName(u"PreviousButton")
        self.PreviousButton.setMinimumSize(QSize(70, 40))
        self.PreviousButton.setFont(font)
        self.PreviousButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.PreviousButton.setStyleSheet(u"QPushButton{border-radius : 10px; border : 2px solid black; padding:10px;\n"
"background-color: rgb(255, 255, 255);}\n"
"\n"
"QPushButton::pressed{\n"
"	background-color: #a6e9ff;\n"
"	border-radius: 10px;\n"
"	border: 2px solid black;\n"
"	padding:10px;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/Icons/Icons/step-backward-icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.PreviousButton.setIcon(icon)

        self.horizontalLayout.addWidget(self.PreviousButton)

        self.PlayPauseButton = QPushButton(Media)
        self.PlayPauseButton.setObjectName(u"PlayPauseButton")
        self.PlayPauseButton.setMinimumSize(QSize(70, 40))
        self.PlayPauseButton.setFont(font)
        self.PlayPauseButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.PlayPauseButton.setStyleSheet(u"QPushButton{border-radius : 10px; border : 2px solid black; padding:10px;\n"
"background-color: rgb(255, 255, 255);}\n"
"\n"
"QPushButton::pressed{\n"
"	background-color: #a6e9ff;\n"
"	border-radius: 10px;\n"
"	border: 2px solid black;\n"
"	padding:10px;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/Icons/Icons/play-pause-icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.PlayPauseButton.setIcon(icon1)
        self.PlayPauseButton.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.PlayPauseButton)

        self.NextButton = QPushButton(Media)
        self.NextButton.setObjectName(u"NextButton")
        self.NextButton.setMinimumSize(QSize(70, 40))
        self.NextButton.setFont(font)
        self.NextButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.NextButton.setStyleSheet(u"QPushButton{border-radius : 10px; border : 2px solid black; padding:10px;\n"
"background-color: rgb(255, 255, 255);}\n"
"\n"
"QPushButton::pressed{\n"
"	background-color: #a6e9ff;\n"
"	border-radius: 10px;\n"
"	border: 2px solid black;\n"
"	padding:10px;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/Icons/Icons/step-forward-icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.NextButton.setIcon(icon2)

        self.horizontalLayout.addWidget(self.NextButton)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.gridLayout.addLayout(self.verticalLayout_2, 3, 3, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 50, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer, 2, 3, 1, 1)


        self.retranslateUi(Media)

        QMetaObject.connectSlotsByName(Media)
    # setupUi

    def retranslateUi(self, Media):
        Media.setWindowTitle(QCoreApplication.translate("Media", u"Media", None))
        self.ImageLabe.setText(QCoreApplication.translate("Media", u"TextLabel", None))
        self.CurrentSongLabel.setText(QCoreApplication.translate("Media", u"Current song: ", None))
        self.CurrentSong.setText(QCoreApplication.translate("Media", u"TextLabel", None))
        self.PreviousButton.setText("")
        self.PlayPauseButton.setText("")
        self.NextButton.setText("")
    # retranslateUi

