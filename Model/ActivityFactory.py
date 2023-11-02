#!/usr/bin/python
#-*- coding: utf-8 -*-
from PySide6.QtWidgets import QMainWindow

from Model.CarBoard import Ui_MainWindow


class ActivityFactory(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def Create(self, ):
        pass


