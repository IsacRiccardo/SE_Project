#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from PySide6 import QtCore
from PySide6.QtMultimedia import QMediaPlayer
from PySide6.QtWidgets import QWidget

from IHome import IHome
from UI.Home import Ui_Home


class Home(IHome, QWidget, Ui_Home):
    def __init__(self, media):
        super().__init__()
        self.setupUi(self)
        self.CurrentSong.setText("No song playing")
        self.media = media

        self.PlayPauseButton.clicked.connect(self.play)
        self.NextButton.clicked.connect(self.next)

    @QtCore.Slot()
    def play(self):
        if self.media.player.mediaStatus() == QMediaPlayer.MediaStatus.InvalidMedia:
            print("Invalid media")
        else:
            if self.media.player.playbackState() == QMediaPlayer.PlaybackState.PlayingState:
                self.media.player.pause()
            else:
                self.media.player.play()
            self.CurrentSong.setText(os.path.basename(str(self.media.player.source().url())))

    def next(self):
        pass

    def previous(self):
        pass
