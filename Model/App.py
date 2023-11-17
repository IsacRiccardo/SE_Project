import sys

from PySide6 import QtCore
from PySide6.QtWidgets import QApplication, QWidget, QDialog

from Model.Activity import Activity
from Model.Home import Home


class App:
    def __init__(self):
        super().__init__()
        self.activity_factory = None
        self.activity = None
        self.home_page = None

        # Create a new activity
        self.activity = Activity()

        # Create home widget and insert it at index 2 (first 2 indexes are occupied by default)
        self.home_page = Home()
        self.activity.stackedWidget.insertWidget(2, self.home_page)

        # Connect UI buttons to methods (Slots)
        self.activity.HomeButton.clicked.connect(self.showHome)
        self.activity.GPSButton.clicked.connect(self.showGPS)
        self.activity.VCButton.clicked.connect(self.showVC)
        self.activity.AVButton.clicked.connect(self.showMedia)

    @QtCore.Slot()
    def showHome(self):
        print("Home")
        # Display home page
        self.activity.stackedWidget.setCurrentIndex(2)

    @QtCore.Slot()
    def showGPS(self):
        print("GPS")

    @QtCore.Slot()
    def showVC(self):
        print("VC")

    @QtCore.Slot()
    def showMedia(self):
        print("Media")


def main():
    core_app = QApplication(sys.argv)
    app = App()

    # Display activity
    app.activity.Display()
    sys.exit(core_app.exec())


if __name__ == "__main__":
    main()
