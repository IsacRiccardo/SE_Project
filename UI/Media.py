# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Media.ui'
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
from PySide6.QtWidgets import (QApplication, QDial, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QSlider, QSpacerItem, QVBoxLayout, QWidget)
from UI import resources_rc

class Ui_Media(object):
    def setupUi(self, Media):
        if not Media.objectName():
            Media.setObjectName(u"Media")
        Media.resize(857, 642)
        font = QFont()
        font.setFamilies([u"Tahoma"])
        font.setPointSize(12)
        Media.setFont(font)
        self.gridLayout = QGridLayout(Media)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(Media)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"border:2px solid black;\n"
"border-radius: 15px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 40, -1, -1)
        self.horizontalSpacer_4 = QSpacerItem(250, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.CurrentSongLabel = QLabel(self.frame)
        self.CurrentSongLabel.setObjectName(u"CurrentSongLabel")
        self.CurrentSongLabel.setMaximumSize(QSize(110, 16777215))
        font1 = QFont()
        font1.setFamilies([u"Tahoma"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.CurrentSongLabel.setFont(font1)
        self.CurrentSongLabel.setStyleSheet(u"border:none;")

        self.horizontalLayout_2.addWidget(self.CurrentSongLabel)

        self.CurrentSong = QLabel(self.frame)
        self.CurrentSong.setObjectName(u"CurrentSong")
        self.CurrentSong.setFont(font1)
        self.CurrentSong.setStyleSheet(u"border:none;")

        self.horizontalLayout_2.addWidget(self.CurrentSong)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(225, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.ImageLabel = QLabel(self.frame)
        self.ImageLabel.setObjectName(u"ImageLabel")
        self.ImageLabel.setStyleSheet(u"border:none;")

        self.horizontalLayout_3.addWidget(self.ImageLabel)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, -1, 5, -1)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.VolumeLabel = QLabel(self.frame)
        self.VolumeLabel.setObjectName(u"VolumeLabel")
        self.VolumeLabel.setMaximumSize(QSize(16777215, 25))
        self.VolumeLabel.setFont(font1)
        self.VolumeLabel.setStyleSheet(u"border:none;")
        self.VolumeLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.VolumeLabel)

        self.VolumeDial = QDial(self.frame)
        self.VolumeDial.setObjectName(u"VolumeDial")
        self.VolumeDial.setMaximumSize(QSize(16777215, 150))
        self.VolumeDial.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.VolumeDial.setMaximum(100)
        self.VolumeDial.setInvertedControls(False)
        self.VolumeDial.setWrapping(False)
        self.VolumeDial.setNotchTarget(5.000000000000000)
        self.VolumeDial.setNotchesVisible(True)

        self.verticalLayout.addWidget(self.VolumeDial)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.MusicSlider = QSlider(self.frame)
        self.MusicSlider.setObjectName(u"MusicSlider")
        self.MusicSlider.setStyleSheet(u"border:none;")
        self.MusicSlider.setOrientation(Qt.Horizontal)

        self.verticalLayout_2.addWidget(self.MusicSlider)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.PreviousButton = QPushButton(self.frame)
        self.PreviousButton.setObjectName(u"PreviousButton")
        self.PreviousButton.setMinimumSize(QSize(70, 50))
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

        self.PlayPauseButton = QPushButton(self.frame)
        self.PlayPauseButton.setObjectName(u"PlayPauseButton")
        self.PlayPauseButton.setMinimumSize(QSize(70, 60))
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
        icon1.addFile(u":/Icons/Icons/play-icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/Icons/Icons/play-icon.svg", QSize(), QIcon.Disabled, QIcon.Off)
        icon1.addFile(u":/Icons/Icons/play-icon.svg", QSize(), QIcon.Active, QIcon.Off)
        icon1.addFile(u":/Icons/Icons/pause-icon.svg", QSize(), QIcon.Active, QIcon.On)
        icon1.addFile(u":/Icons/Icons/play-icon.svg", QSize(), QIcon.Selected, QIcon.Off)
        icon1.addFile(u":/Icons/Icons/pause-icon.svg", QSize(), QIcon.Selected, QIcon.On)
        self.PlayPauseButton.setIcon(icon1)
        self.PlayPauseButton.setIconSize(QSize(25, 25))
        self.PlayPauseButton.setCheckable(True)

        self.horizontalLayout.addWidget(self.PlayPauseButton)

        self.NextButton = QPushButton(self.frame)
        self.NextButton.setObjectName(u"NextButton")
        self.NextButton.setMinimumSize(QSize(70, 50))
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

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)


        self.gridLayout.addWidget(self.frame, 0, 1, 1, 1)


        self.retranslateUi(Media)

        QMetaObject.connectSlotsByName(Media)
    # setupUi

    def retranslateUi(self, Media):
        Media.setWindowTitle(QCoreApplication.translate("Media", u"Media", None))
        self.CurrentSongLabel.setText(QCoreApplication.translate("Media", u"Current song: ", None))
        self.CurrentSong.setText(QCoreApplication.translate("Media", u"No music playing", None))
        self.ImageLabel.setText(QCoreApplication.translate("Media", u"TextLabel", None))
        self.VolumeLabel.setText(QCoreApplication.translate("Media", u"Volume", None))
        self.PreviousButton.setText("")
        self.PlayPauseButton.setText("")
        self.NextButton.setText("")
    # retranslateUi

