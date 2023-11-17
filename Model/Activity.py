#!/usr/bin/python
#-*- coding: utf-8 -*-
from PySide6.QtWidgets import QMainWindow

from Model.ActivityFactory import ActivityFactory


class Activity(QMainWindow, ActivityFactory):
    def __init__(self):
        super().__init__()
        self.Create(self)

    def Display(self, ):
        self.show()

