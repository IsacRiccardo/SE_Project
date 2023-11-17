#!/usr/bin/python
# -*- coding: utf-8 -*-
from PySide6.QtCore import QUrl
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtWidgets import QWidget, QPushButton

from IHome import IHome
from UI.Home import Ui_Home


class Home(IHome, QWidget, Ui_Home):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
