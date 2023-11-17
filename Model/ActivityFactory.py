#!/usr/bin/python
#-*- coding: utf-8 -*-
from UI.CarBoard import Ui_MainWindow


class ActivityFactory(Ui_MainWindow):

    def Create(self, activity):
        self.setupUi(activity)
