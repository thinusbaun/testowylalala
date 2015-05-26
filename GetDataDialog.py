# -*- coding: utf-8 -*-
__author__ = 'michal'

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from CameraDevice import CameraDevice
from CameraWidget import CameraWidget

class GetDataDialog(QDialog):
    def __init__(self, parent = None):
        super(GetDataDialog, self).__init__(parent)
        self.cameraDevice = CameraDevice()
        self.cameraWidget = CameraWidget(self.cameraDevice, self)
        self.mainLayout = QHBoxLayout(self)
        self.mainLayout.addWidget(self.cameraWidget)
        self.setLayout(self.mainLayout)


