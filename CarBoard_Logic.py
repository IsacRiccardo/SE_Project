import sys

from PySide6 import QtCore
from PySide6.QtWidgets import QMainWindow, QApplication, QDialog

from CarBoard import Ui_MainWindow


class CarBoardWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.showDialog)

    @QtCore.Slot()
    def showDialog(self):
        demoDialog = QDialog()
        demoDialog.exec()


def main():
    app = QApplication(sys.argv)
    window = CarBoardWindow()

    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
