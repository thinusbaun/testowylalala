# -*- coding: utf-8 -*-
__author__ = 'michal'

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from CameraDevice import CameraDevice
from IdentificationCameraWidget import IdentificationCameraWidget
from FacesRecognizer import FacesRecognizer


class IdentificationDialog(QDialog):
    def __init__(self, parent=None):
        super(IdentificationDialog, self).__init__(parent)
        self.recognizer = FacesRecognizer()
        self.recognizer.trainModel()
        print self.recognizer.labels

        self.cameraDevice = CameraDevice()
        self.cameraWidget = IdentificationCameraWidget(self.cameraDevice, self.recognizer, self)
        self.mainLayout = QVBoxLayout(self)
        self.mainLayout.addWidget(self.cameraWidget)
        self.setLayout(self.mainLayout)

        self.closeButton = QPushButton("Zamknij", self)
        self.closeButton.clicked.connect(self.closeButtonClicked)

        self.secondLayout = QHBoxLayout(self)
        self.secondLayout.addWidget(self.closeButton)
        self.mainLayout.addLayout(self.secondLayout)

    @pyqtSlot()
    def closeButtonClicked(self):
        self.close()
