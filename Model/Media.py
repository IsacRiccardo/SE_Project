#!/usr/bin/python
# -*- coding: utf-8 -*-
import os

from PySide6 import QtCore
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtMultimedia import QMediaPlayer
from PySide6.QtWidgets import QWidget

from IMEDIA import IMEDIA
from UI.Media import Ui_Media


class Media(IMEDIA, QWidget, Ui_Media):
    def __init__(self, media):
        super().__init__()
        self.setupUi(self)
        self.mediaPlayer = media
        self.VolumeDial.setValue(self.mediaPlayer.volume * 100)
        self.VolumeDial.setRange(0, 100)

        with open(os.path.abspath("Resources/music_image.jpg"), "rb") as f:
            self.contentBytes = f.read()

        self.musicImage = QImage()
        self.musicImage.loadFromData(self.contentBytes)
        self.musicImage = self.musicImage.scaled(400, 400)
        self.pixmap = QPixmap.fromImage(self.musicImage)
        self.ImageLabel.setPixmap(self.pixmap)

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

    def verifyMPstatus(self):
        if self.mediaPlayer.getMediaPlayerStatus() == QMediaPlayer.PlaybackState.PlayingState:
            self.CurrentSong.setText(os.path.basename(str(self.mediaPlayer.player.source().url())))
            self.PlayPauseButton.setChecked(True)
        else:
            self.PlayPauseButton.setChecked(False)