from PySide6.QtWidgets import QMainWindow, \
    QPushButton, \
    QWidget, \
    QBoxLayout, \
    QScrollArea, \
    QMessageBox

from widgets import AppTable


class NvidiaManager(QMainWindow):
    # TODO: Разобраться с css виджета. Пока что получается говно
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Optimuis application manager")

        self.setFixedWidth(600)
        self.setFixedHeight(400)

        self.setup_ui()

    def setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.layout = QBoxLayout(QBoxLayout.Direction.LeftToRight)
        central_widget.setLayout(self.layout)

        scroll = QScrollArea(central_widget)
        scroll.setWidgetResizable(True)

        self.appTable = AppTable(central_widget)
        scroll.setWidget(self.appTable)
        self.layout.addWidget(scroll)

        self.btn = QPushButton("Apply")
        self.btn.clicked.connect(self.apply_btn_clicked)
        self.layout.addWidget(self.btn)

    def apply_btn_clicked(self):
        appsList = self.appTable.get_apps()

        for app in appsList:
            app.change_video_card()

        msg = QMessageBox()
        msg.setText("Done")
        msg.exec()

    def enable_discrete_card(self):
        pass

    def disable_discrete_card(self):
        pass
