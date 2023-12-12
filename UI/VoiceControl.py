# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VoiceControl.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
from UI import resources_rc

class Ui_VC(object):
    def setupUi(self, VC):
        if not VC.objectName():
            VC.setObjectName(u"VC")
        VC.resize(709, 600)
        VC.setMaximumSize(QSize(100000, 100000))
        self.verticalLayout = QVBoxLayout(VC)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.VCframe = QFrame(VC)
        self.VCframe.setObjectName(u"VCframe")
        self.VCframe.setStyleSheet(u"border:2px solid black;\n"
"border-radius: 10px;\n"
"background-color: qlineargradient(spread:pad, x1:0.5, y1:0.818182, x2:0.506, y2:0, stop:0 rgba(24, 0, 97, 255), stop:1 rgba(255, 255, 255, 255));")
        self.VCframe.setFrameShape(QFrame.StyledPanel)
        self.VCframe.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.VCframe)
        self.gridLayout.setObjectName(u"gridLayout")
        self.Suggestion_3 = QLabel(self.VCframe)
        self.Suggestion_3.setObjectName(u"Suggestion_3")
        self.Suggestion_3.setMinimumSize(QSize(0, 50))
        font = QFont()
        font.setFamilies([u"Tahoma"])
        font.setPointSize(12)
        font.setBold(True)
        self.Suggestion_3.setFont(font)
        self.Suggestion_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.Suggestion_3.setAlignment(Qt.AlignCenter)
        self.Suggestion_3.setMargin(10)

        self.gridLayout.addWidget(self.Suggestion_3, 6, 2, 1, 1)

        self.Suggestion_1 = QLabel(self.VCframe)
        self.Suggestion_1.setObjectName(u"Suggestion_1")
        self.Suggestion_1.setMinimumSize(QSize(0, 50))
        self.Suggestion_1.setFont(font)
        self.Suggestion_1.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.Suggestion_1.setAlignment(Qt.AlignCenter)
        self.Suggestion_1.setMargin(10)

        self.gridLayout.addWidget(self.Suggestion_1, 6, 0, 1, 1)

        self.UsernameLabel = QLabel(self.VCframe)
        self.UsernameLabel.setObjectName(u"UsernameLabel")
        self.UsernameLabel.setMinimumSize(QSize(0, 50))
        font1 = QFont()
        font1.setFamilies([u"Tahoma"])
        font1.setPointSize(15)
        font1.setBold(True)
        self.UsernameLabel.setFont(font1)
        self.UsernameLabel.setStyleSheet(u"background-color: transparent;\n"
"border:none;\n"
"")
        self.UsernameLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.UsernameLabel, 0, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_2, 8, 1, 1, 1)

        self.pushToTalkBtn = QPushButton(self.VCframe)
        self.pushToTalkBtn.setObjectName(u"pushToTalkBtn")
        self.pushToTalkBtn.setMinimumSize(QSize(0, 50))
        self.pushToTalkBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushToTalkBtn.setStyleSheet(u"background-color: transparent;\n"
"border: none;")
        icon = QIcon()
        icon.addFile(u":/Icons/Icons/microphone-icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/Icons/Icons/waveform-icon.svg", QSize(), QIcon.Active, QIcon.On)
        icon.addFile(u":/Icons/Icons/waveform-icon.svg", QSize(), QIcon.Selected, QIcon.On)
        self.pushToTalkBtn.setIcon(icon)
        self.pushToTalkBtn.setIconSize(QSize(60, 80))
        self.pushToTalkBtn.setCheckable(True)

        self.gridLayout.addWidget(self.pushToTalkBtn, 2, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 1, 1, 1, 1)

        self.Suggestion_2 = QLabel(self.VCframe)
        self.Suggestion_2.setObjectName(u"Suggestion_2")
        self.Suggestion_2.setMinimumSize(QSize(0, 50))
        self.Suggestion_2.setFont(font)
        self.Suggestion_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.Suggestion_2.setAlignment(Qt.AlignCenter)
        self.Suggestion_2.setMargin(10)

        self.gridLayout.addWidget(self.Suggestion_2, 6, 1, 1, 1)

        self.line = QFrame(self.VCframe)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 4, 0, 2, 3)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 3, 1, 1, 1)


        self.verticalLayout.addWidget(self.VCframe)


        self.retranslateUi(VC)

        QMetaObject.connectSlotsByName(VC)
    # setupUi

    def retranslateUi(self, VC):
        VC.setWindowTitle(QCoreApplication.translate("VC", u"Form", None))
        self.Suggestion_3.setText(QCoreApplication.translate("VC", u"TextLabel", None))
        self.Suggestion_1.setText(QCoreApplication.translate("VC", u"TextLabel", None))
        self.UsernameLabel.setText(QCoreApplication.translate("VC", u"TextLabel", None))
        self.pushToTalkBtn.setText("")
        self.Suggestion_2.setText(QCoreApplication.translate("VC", u"TextLabel", None))
    # retranslateUi

