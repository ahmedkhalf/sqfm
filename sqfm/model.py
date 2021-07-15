from pathlib import Path
from typing import List, Optional

from PyQt5.QtCore import QAbstractTableModel, QDir, QModelIndex, QObject, Qt, QFileInfo


class FileManagerModel(QAbstractTableModel):
    def __init__(self, parent: Optional[QObject] = None) -> None:
        super().__init__(parent=parent)

        self.file_browser = FileBrowser()
        self.get_files()

    def get_files(self):
        self.layoutAboutToBeChanged.emit()
        self.file_browser.list_files()
        self.layoutChanged.emit()

    def open_item(self, ind: int):
        item = self.file_browser.files[ind]
        if item.isDir():
            print("isDir")
            self.file_browser.current_pwd = QDir(item.filePath())
            self.get_files()

    def go_back(self):
        if self.file_browser.current_pwd.cdUp():
            self.get_files()

    def rowCount(self, ind: QModelIndex):
        return len(self.file_browser.files)

    def columnCount(self, ind: QModelIndex):
        return 1

    def data(self, ind: QModelIndex, role: Qt.ItemDataRole):
        if role == Qt.DisplayRole:
            return self.file_browser.files[ind.row()].fileName()
        return None


class FileBrowser:
    def __init__(self) -> None:
        self.current_pwd: QDir = QDir.home()

        self.files: List[QFileInfo] = []

    def list_files(self):
        self.files = self.current_pwd.entryInfoList()

    def refresh(self):
        pass
