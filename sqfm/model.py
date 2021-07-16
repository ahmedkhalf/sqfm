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
            self.file_browser.current_pwd = QDir(item.filePath())
            self.get_files()

    def go_back(self):
        if self.file_browser.current_pwd.cdUp():
            self.get_files()

    def toggle_hidden(self):
        self.file_browser.show_hidden = not self.file_browser.show_hidden
        self.get_files()

    def rowCount(self, ind: QModelIndex):
        return len(self.file_browser.files)

    def columnCount(self, ind: QModelIndex):
        return 1

    def data(self, ind: QModelIndex, role: Qt.ItemDataRole):
        if role == Qt.DisplayRole:
            return self.file_browser.files[ind.row()].fileName()
        return None

    def headerData(self, section: int, orientation: Qt.Orientation, role: Qt.ItemDataRole):
        if orientation == Qt.Horizontal:
            if section == 0:
                if role == Qt.DisplayRole:
                    return "Name"
        return None

    def sort(self, column: int, order: Qt.SortOrder):
        if order == Qt.AscendingOrder:
            self.file_browser.sort_reversed = False
        elif order == Qt.DescendingOrder:
            self.file_browser.sort_reversed = True

        self.get_files()


class FileBrowser:
    def __init__(self) -> None:
        self.current_pwd: QDir = QDir.home()

        self.files: List[QFileInfo] = []
        self.show_hidden = False

        self.sort_item = QDir.Name
        self.sort_reversed = False

    def list_files(self):
        filter = QDir.AllEntries | QDir.NoDotAndDotDot
        if self.show_hidden:
            filter |= QDir.Hidden

        sort = self.sort_item | QDir.DirsFirst | QDir.IgnoreCase | QDir.LocaleAware
        if self.sort_reversed:
            sort |= QDir.Reversed
        self.files = self.current_pwd.entryInfoList(filters=filter, sort=sort)  # type: ignore

    def refresh(self):
        pass
