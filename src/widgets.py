import glob
import os

from PySide6.QtWidgets import \
    QCheckBox, \
    QVBoxLayout, \
    QWidget, \
    QLabel, \
    QBoxLayout

from PySide6.QtCore import Qt


class App(QWidget):
    def __init__(self, parrent, path: str):
        super().__init__(parent=parrent)

        self.path = path

        self.checkBox = QCheckBox(self)
        self.checkBox.setMaximumSize(18, 18)

        self.__parse_desktop_file()

        self.label = QLabel(self.name)
        self.label.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.grid = QBoxLayout(QBoxLayout.Direction.LeftToRight)
        self.setLayout(self.grid)

        self.grid.addWidget(self.checkBox)
        self.grid.addWidget(self.label)

        self.setStyleSheet("""
            background-color: #cacfcc;
            border: 2px solid #000000
        """)

    def __parse_desktop_file(self):
        self.name = None
        self.exec = None
        self.icon = None

        with open(self.path, 'r') as file:
            params = file.readlines()

        for i in params:
            if i.startswith("Name="):
                self.name = i[5:]
            if i.startswith("Exec="):
                self.exec = i.strip()
            if i.startswith("Icon="):
                self.icon = i.strip()

        if any([self.name is None, self.exec is None]):
            return

        if "env __NV_PRIME_RENDER_OFFLOAD=1 __VK_LAYER_NV_optimus=NVIDIA_only __GLX_VENDOR_LIBRARY_NAME=nvidia" in self.exec:
            self.checkBox.setChecked(True)
            self.isChecked = True

    def __str__(self) -> str:
        return f"VALUES:\n\t{self.name}\t{self.icon}\n\t{self.exec}"

    def is_checked(self):
        return self.checkBox.isChecked()

    def change_video_card(self):
        """
        Меняет видеокарту для запуска
        :return: None
        """
        with open(self.path, 'r') as file:
            cfgFile = file.readlines()

        execIndex = 0
        for i in range(len(cfgFile)):
            if cfgFile[i].startswith("Exec="):
                execIndex = i
                break

        if self.is_checked():
            if not "env __NV_PRIME_RENDER_OFFLOAD=1 __VK_LAYER_NV_optimus=NVIDIA_only __GLX_VENDOR_LIBRARY_NAME=nvidia" in \
                   cfgFile[execIndex]:
                cfgFile[execIndex] = cfgFile[execIndex].replace("Exec=", '')
                cfgFile[
                    execIndex] = "Exec=env __NV_PRIME_RENDER_OFFLOAD=1 __VK_LAYER_NV_optimus=NVIDIA_only __GLX_VENDOR_LIBRARY_NAME=nvidia" + \
                                 cfgFile[execIndex]
        else:
            if "env __NV_PRIME_RENDER_OFFLOAD=1 __VK_LAYER_NV_optimus=NVIDIA_only __GLX_VENDOR_LIBRARY_NAME=nvidia" in \
                    cfgFile[execIndex]:
                cfgFile[execIndex] = cfgFile[execIndex].replace(
                    "env __NV_PRIME_RENDER_OFFLOAD=1 __VK_LAYER_NV_optimus=NVIDIA_only __GLX_VENDOR_LIBRARY_NAME=nvidia",
                    "")

        s = ''
        for i in cfgFile:
            s += i

        with open(self.path, 'w') as file:
            file.write(s)


class AppTable(QWidget):
    def __init__(self, parrent):
        super().__init__(parent=parrent)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        HOME = os.listdir("/home")

        self.appsList = glob.glob(f"/home/{HOME[0]}/.local/share/applications" + "/*.desktop")
        self.appsList += glob.glob("/usr/share/applications" + "/*.desktop")


        self.apps = list()

        for app in self.appsList:
            try:
                self.apps.append(App(self, app))
            except:
                continue

        for app in self.apps:
            self.layout.addWidget(app)

    def get_apps(self):
        return self.apps
