import sys
from subprocess import run
from PySide6.QtWidgets import QApplication

from mainWindow import NvidiaManager


def main():
    app = QApplication(sys.argv)

    mainWindow = NvidiaManager()
    mainWindow.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    run("clear")

    user = run(["whoami"], capture_output=True, text=True).stdout
    if user.strip() == "root":
        main()
    else:
        print("i need root privileges")
