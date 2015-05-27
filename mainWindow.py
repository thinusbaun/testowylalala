# -*- coding: utf-8 -*-
__author__ = 'michal'

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from GetDataDialog import GetDataDialog


class MainWindow(QMainWindow):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)
        self.mainWidget = QWidget()
        self.setCentralWidget(self.mainWidget)

        self.mainLayout = QVBoxLayout(self)
        self.getDataButton = QPushButton("Zbierz dane", self)
        self.identificationButton = QPushButton("Identyfikacja", self)
        self.getDataButton.clicked.connect(self.getData)

        self.mainLayout.addWidget(self.getDataButton)
        self.mainLayout.addWidget(self.identificationButton)
        self.mainWidget.setLayout(self.mainLayout)

    @pyqtSlot()
    def getData(self):
        userNameInputDialog, ok = QInputDialog.getText(self,"GetUserName","Nazwa użytkownika:", QLineEdit.Normal,
                                                   QDir.home().dirName())
        if ok:
            dialog = GetDataDialog(userNameInputDialog, self)
            dialog.exec_()
        self.close()
