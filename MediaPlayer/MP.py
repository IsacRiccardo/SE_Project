import os

from PySide6.QtCore import QUrl
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput


class MediaPlayer():
    def __init__(self):
        super().__init__()
        self.mediaDir = os.path.abspath("Resources/Songs")
        self.currentSongPlaying = 0
        self.volume = 0.2
        self.media = []
        self.audio = QAudioOutput()
        self.audio.setVolume(self.volume)
        self.player = QMediaPlayer()
        self.player.setAudioOutput(self.audio)
        self.getMedia()
        print(self.media)
        try:
            self.player.setSource(QUrl.fromLocalFile(self.media[self.currentSongPlaying]))
        except Exception:
            print("Error setting source")

    def getMedia(self):
        for source in os.listdir(self.mediaDir):
            self.media.append(os.path.abspath(os.path.join(self.mediaDir, source)))

    def changeVolume(self, volume):
        self.volume = volume / 100
        self.audio.setVolume(self.volume)

    def getMediaPlayerStatus(self):
        return self.player.playbackState()
