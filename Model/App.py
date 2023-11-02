import sys

from PySide6.QtWidgets import QApplication
from ActivityFactory import ActivityFactory


def main():
    app = QApplication(sys.argv)
    factory = ActivityFactory()

    factory.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
