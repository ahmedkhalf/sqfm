from PyQt5.QtWidgets import QMainWindow

from .views import SimpleTableView
from .model import FileManagerModel


class FileManagerApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        model = FileManagerModel()
        table = SimpleTableView(model)

        self.setCentralWidget(table)

        self.setWindowTitle("File Manager")
        self.resize(640, 480)
        self.show()
