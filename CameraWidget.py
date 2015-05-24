__author__ = 'michal'

import cv
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class CameraWidget(QWidget):

    newFrame = pyqtSignal(cv.iplimage)

    def __init__(self, cameraDevice, parent=None):
        super(CameraWidget, self).__init__(parent)

        self._frame = None

        self._cameraDevice = cameraDevice
        self._cameraDevice.newFrameAvailable.connect(self._onNewFrame)

        width, height = cameraDevice.frameSize
        self.setMinimumHeight(height)
        self.setMinimumWidth(width)

    @pyqtSlot(cv.iplimage)
    def _onNewFrame(self, frame):
        self._frame = cv.CloneImage(frame)
        self.newFrame.emit(self._frame)
        self.update()

    def changeEvent(self, event):
        if event.type() == QEvent.EnabledChange:
            if self.isEnabled():
                self._cameraDevice.newFrame.connect(self._onNewFrame)
            else:
                self._cameraDevice.newFrame.disconnect(self._onNewFrame)

    def paintEvent(self, event):
        if self._frame is None:
            return
        painter = QPainter(self)
        frame = QImage(self._frame.tostring(), self._frame.width, self._frame.height, QImage.Format_RGB888).rgbSwapped()
        painter.drawImage(QPoint(0, 0), frame)



