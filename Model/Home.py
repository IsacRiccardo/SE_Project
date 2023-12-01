#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from PySide6 import QtCore
from PySide6.QtCore import QTimer
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
        self.VCButton.clicked.connect(self.listenVoiceInput)
        self.timer = QTimer()
        self.timer.timeout.connect(self.processVoiceInput)
        self.timer.setInterval(2000)

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

    def verifyMPstatus(self):
        if self.media.getMediaPlayerStatus() == QMediaPlayer.PlaybackState.PlayingState:
            self.CurrentSong.setText(os.path.basename(str(self.media.player.source().url())))
            self.PlayPauseButton.setChecked(True)
        else:
            self.PlayPauseButton.setChecked(False)

    @QtCore.Slot()
    def listenVoiceInput(self):
        # Stop music player
        if self.media.getMediaPlayerStatus() == QMediaPlayer.PlaybackState.PlayingState:
            self.media.player.pause()
        # Start timer
        self.timer.start()

    @QtCore.Slot()
    def processVoiceInput(self):
        # Reset button status
        self.VCButton.setChecked(False)
        if self.media.getMediaPlayerStatus() == QMediaPlayer.PlaybackState.PausedState:
            self.media.player.play()
        # Stop timer
        self.timer.stop()
