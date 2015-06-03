# -*- coding: utf-8 -*-
__author__ = 'michal'

import os
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from CameraDevice import CameraDevice
from CameraWidget import CameraWidget


class IdentificationDialog(QDialog):
    def __init__(self, userName, parent=None):
        super(IdentificationDialog, self).__init__(parent)
        self.userName = userName
        self.picturesLeft = 5

        self.cameraDevice = CameraDevice()
        self.cameraWidget = CameraWidget(self.cameraDevice, self)
        self.mainLayout = QVBoxLayout(self)
        self.mainLayout.addWidget(self.cameraWidget)
        self.setLayout(self.mainLayout)

        self.closeButton = QPushButton("Zamknij", self)
        self.closeButton.clicked.connect(self.closeButtonClicked)

        self.secondLayout = QHBoxLayout(self)
        self.secondLayout.addWidget(self.closeButton)
        self.mainLayout.addLayout(self.secondLayout)
        self.checkUserName()

    @pyqtSlot()
    def closeButtonClicked(self):
        self.close()
