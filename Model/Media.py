#!/usr/bin/python
# -*- coding: utf-8 -*-
import os

from PySide6 import QtCore
from PySide6.QtMultimedia import QMediaPlayer
from PySide6.QtWidgets import QWidget

from IMEDIA import IMEDIA
from UI.Media import Ui_Media


class Media(IMEDIA, QWidget, Ui_Media):
    def __init__(self, media):
        super().__init__()
        self.setupUi(self)
        self.mediaPlayer = media
        self.VolumeDial.setValue(self.mediaPlayer.volume*100)
        self.CurrentSong.setText(os.path.basename(str(self.mediaPlayer.player.source().url())))
        self.VolumeDial.setRange(0, 100)

        self.PlayPauseButton.clicked.connect(self.play)
        self.VolumeDial.valueChanged.connect(self.changeVolume)

    @QtCore.Slot()
    def play(self):
        if self.mediaPlayer.player.mediaStatus() == QMediaPlayer.MediaStatus.InvalidMedia:
            print("Invalid media")
        else:
            if self.mediaPlayer.player.playbackState() == QMediaPlayer.PlaybackState.PlayingState:
                self.mediaPlayer.player.pause()
            else:
                self.mediaPlayer.player.play()
            self.CurrentSong.setText(os.path.basename(str(self.mediaPlayer.player.source().url())))

    @QtCore.Slot()
    def changeVolume(self):
        self.mediaPlayer.changeVolume(self.VolumeDial.value())