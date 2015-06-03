# -*- coding: utf-8 -*-
__author__ = 'michal'

import os
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from CameraDevice import CameraDevice
from CameraWidget import CameraWidget


class GetDataDialog(QDialog):
    def __init__(self, userName, parent=None):
        super(GetDataDialog, self).__init__(parent)
        self.userName = userName
        self.picturesLeft = 5


        self.cameraDevice = CameraDevice()
        self.cameraWidget = CameraWidget(self.cameraDevice, self)
        self.mainLayout = QVBoxLayout(self)
        self.mainLayout.addWidget(self.cameraWidget)
        self.setLayout(self.mainLayout)

        self.getPictureButton = QPushButton("Zrób zdjęcie", self)
        self.getPictureButton.clicked.connect(self.pictureButtonClicked)
        self.picturesLeftLabel = QLabel("Pozostało zdjęć: {}".format(self.picturesLeft), self)

        self.secondLayout = QHBoxLayout(self)
        self.secondLayout.addWidget(self.getPictureButton)
        self.secondLayout.addWidget(self.picturesLeftLabel)
        self.mainLayout.addLayout(self.secondLayout)
        self.checkUserName()

    @pyqtSlot()
    def pictureButtonClicked(self):
        if self.picturesLeft == 0:
            self.close()

        frame = self.cameraWidget.getFaceRectangle()
        if frame is not None:
            frame.save("./dane/{}/{}.bmp".format(self.userName, self.picturesLeft))
            self.picturesLeft -= 1
            self.picturesLeftLabel.setText("Pozostało zdjęć: {}".format(self.picturesLeft))
            if self.picturesLeft == 0:
                self.getPictureButton.setText("Zamknij")

    def checkUserName(self):
        self.picturesLeft = 0 if os.path.exists("./dane/{}".format(self.userName)) else 5
        if self.picturesLeft == 0:
            self.getPictureButton.setDisabled(True)
        if self.picturesLeft == 5:
            os.makedirs("./dane/{}".format(self.userName))
