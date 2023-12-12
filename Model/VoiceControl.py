#!/usr/bin/python
#-*- coding: utf-8 -*-
from PySide6.QtMultimedia import QMediaPlayer
from PySide6.QtWidgets import QWidget

from IVoiceControl import IVoiceControl
from UI.VoiceControl import Ui_VC


class VoiceControl(IVoiceControl, QWidget, Ui_VC):
    def __init__(self, media):
        super().__init__()
        self.setupUi(self)
        self.mediaplayer = media
        self.UsernameLabel.setText("HI USER")
        self.Suggestion_1.setText("How's the weather?")
        self.Suggestion_2.setText("Where is the nearest gas station?")
        self.Suggestion_3.setText("Call Marco")

    def pauseToSpeak(self):
        # Pause music in order to speak
        if self.mediaplayer.getMediaPlayerStatus() == QMediaPlayer.PlaybackState.PlayingState:
            self.mediaplayer.pauseMediaPLayer()
