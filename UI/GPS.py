# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GPS.ui'
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
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QSizePolicy,
    QWidget)

class Ui_GPS(object):
    def setupUi(self, GPS):
        if not GPS.objectName():
            GPS.setObjectName(u"GPS")
        GPS.resize(846, 620)
        self.gridLayout = QGridLayout(GPS)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(GPS)
        self.frame.setObjectName(u"frame")
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet(u"border:2px solid black;\n"
"border-radius: 15px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.webEngineView = QWebEngineView(self.frame)
        self.webEngineView.setObjectName(u"webEngineView")
        self.webEngineView.setUrl(QUrl(u"https://www.google.com/maps/@45.7266998,21.220925,14z?ucbcb=1&entry=ttu"))

        self.gridLayout_2.addWidget(self.webEngineView, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(GPS)

        QMetaObject.connectSlotsByName(GPS)
    # setupUi

    def retranslateUi(self, GPS):
        GPS.setWindowTitle(QCoreApplication.translate("GPS", u"GPS", None))
    # retranslateUi

