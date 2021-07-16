from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QAbstractItemView, QTableView, QHeaderView

from .model import FileManagerModel


class SimpleTableView(QTableView):
    def __init__(self, model: FileManagerModel):
        super(QTableView, self).__init__()
        self.verticalHeader().hide()
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.setSelectionMode(QAbstractItemView.SingleSelection)
        # Smooth scroll
        self.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.setSortingEnabled(True)
        self.sortByColumn(0, Qt.AscendingOrder)

        self.data_model: FileManagerModel = model
        self.setModel(model)
        self.selectRow(0)
        self.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_K:
            ind = self.currentIndex()
            newInd = ind.siblingAtRow(ind.row() - 1)
            self.setCurrentIndex(newInd)
        elif event.key() == Qt.Key_J:
            ind = self.currentIndex()
            newInd = ind.siblingAtRow(ind.row() + 1)
            self.setCurrentIndex(newInd)
        elif event.key() == Qt.Key_L:
            self.data_model.open_item(self.currentIndex().row())
        elif event.key() == Qt.Key_H:
            self.data_model.go_back()
        elif event.key() == Qt.Key_Period:
            self.data_model.toggle_hidden()
        else:
            super().keyPressEvent(event)
