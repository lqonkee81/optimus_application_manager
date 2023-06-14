import sys

from PySide6.QtWidgets import \
    QApplication, \
    QWidget, \
    QMainWindow, \
    QCheckBox, \
    QGridLayout, \
    QPushButton


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)

        self.layout = QGridLayout()
        centralWidget.setLayout(self.layout)

        self.checkBox = QCheckBox("Kek")

        self.button = QPushButton(text="Show", parent=self)
        self.button.clicked.connect(self.btn_clicked)

        # self.layout.addWidget(self.button, 0, 0)
        self.layout.addWidget(self.checkBox, 0, 1)

    def btn_clicked(self):
        print(self.checkBox.isChecked())


if __name__ == "__main__":
    app = QApplication(sys.argv)

    mw = App()
    mw.show()

    sys.exit(app.exec())
