#!/usr/bin/python
# -*- coding: utf-8 -*-
from PySide6.QtWidgets import QWidget

from IGPS import IGPS
from UI.GPS import Ui_GPS


class GPS(IGPS, QWidget, Ui_GPS):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
