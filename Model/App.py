import sys

from PySide6 import QtCore
from PySide6.QtWidgets import QApplication, QWidget, QDialog, QButtonGroup

from Model.Activity import Activity
from Model.GPS import GPS
from Model.Home import Home

from MediaPlayer.MP import *
from Model.Media import Media
from Model.VoiceControl import VoiceControl


class App:
    def __init__(self):
        super().__init__()
        self.activity_factory = None
        self.activity = None
        self.home_page = None
        self.media = MediaPlayer()
        self.buttonGroup = QButtonGroup()

        # Create a new activity
        self.activity = Activity()

        # Create home widget and insert it at index 2 (first 2 indexes are occupied by default)
        self.home_page = Home(self.media)
        self.activity.stackedWidget.insertWidget(0, self.home_page)

        # Create GPS widget and insert it into the stacked widget
        self.gps_page = GPS()
        self.activity.stackedWidget.insertWidget(1, self.gps_page)

        # Create Media page and insert it into the stacked widget
        self.media_page = Media(self.media)
        self.activity.stackedWidget.insertWidget(2, self.media_page)

        # Create voice control page and insert it into the stacked widget
        self.vc_page = VoiceControl(self.media)
        self.activity.stackedWidget.insertWidget(3, self.vc_page)

        # Add buttons to button group
        self.buttonGroup.addButton(self.activity.HomeButton)
        self.buttonGroup.addButton(self.activity.GPSButton)
        self.buttonGroup.addButton(self.activity.VCButton)
        self.buttonGroup.addButton(self.activity.AVButton)
        self.activity.HomeButton.setChecked(True)

        # Connect UI buttons to methods (Slots)
        self.activity.HomeButton.clicked.connect(self.showHome)
        self.activity.GPSButton.clicked.connect(self.showGPS)
        self.activity.VCButton.clicked.connect(self.showVC)
        self.activity.AVButton.clicked.connect(self.showMedia)

    @QtCore.Slot()
    def showHome(self):
        print("Home")
        # Display home page
        self.activity.stackedWidget.setCurrentIndex(0)
        self.home_page.verifyMPstatus()

    @QtCore.Slot()
    def showGPS(self):
        print("GPS")
        # Display gps page
        self.activity.stackedWidget.setCurrentIndex(1)

    @QtCore.Slot()
    def showMedia(self):
        print("Media")
        # Display media page
        self.activity.stackedWidget.setCurrentIndex(2)
        self.media_page.verifyMPstatus()

    @QtCore.Slot()
    def showVC(self):
        print("VC")
        # Display vc page
        self.activity.stackedWidget.setCurrentIndex(3)
        self.vc_page.pauseToSpeak()


def main():
    core_app = QApplication(sys.argv)
    app = App()

    # Display activity
    app.activity.Display()
    sys.exit(core_app.exec())


if __name__ == "__main__":
    main()
