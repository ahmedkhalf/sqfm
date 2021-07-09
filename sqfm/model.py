import typing
from pathlib import Path

from PyQt5.QtCore import QAbstractTableModel, QModelIndex, QObject, Qt


class FileManagerModel(QAbstractTableModel):
    def __init__(self, parent: typing.Optional[QObject] = None) -> None:
        super().__init__(parent=parent)

        self.current_pwd = Path.home()
        self.show_hidden = False
        self.files = []

        self.get_files()

    def get_files(self):
        self.layoutAboutToBeChanged.emit()
        if self.show_hidden:
            self.files = list(self.current_pwd.glob("*"))
        else:
            self.files = []
            for file in self.current_pwd.glob("*"):
                if file.name[0] != ".":
                    self.files.append(file)
        self.layoutChanged.emit()

    def open_item(self, ind: int):
        if self.files[ind].is_dir():
            self.current_pwd = self.files[ind]
            self.get_files()

    def go_back(self):
        self.current_pwd = self.current_pwd.parent
        self.get_files()

    def rowCount(self, ind: QModelIndex):
        return len(self.files)

    def columnCount(self, ind: QModelIndex):
        return 1

    def data(self, ind: QModelIndex, role: Qt.ItemDataRole):
        if role == Qt.DisplayRole:
            return self.files[ind.row()].name
        return None
