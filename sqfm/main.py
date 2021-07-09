import sys

from PyQt5.QtWidgets import QApplication, QStyleFactory

from .app import FileManagerApp


def main():
    app = QApplication(sys.argv)

    if "Fusion" in QStyleFactory.keys():
        app.setStyle("Fusion")

        # styleSheet = ""
        # with open("style.css", "r") as f:
        #     styleSheet = f.read()
        # app.setStyleSheet(styleSheet)
    else:
        raise EnvironmentError("App requires fusion style")

    _ = FileManagerApp()
    sys.exit(app.exec_())
