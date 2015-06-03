__author__ = 'michal'

import numpy
import cv2
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

        self._faceCascade = cv2.CascadeClassifier("./classifier.xml")

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
        tmp = numpy.asarray(self._frame[:,:])
        gray = cv2.cvtColor(tmp, cv2.COLOR_BGR2GRAY)
        faces = self._faceCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30),
                                                   flags = cv.CV_HAAR_SCALE_IMAGE)
        self.paintRectangles(faces)

    def paintRectangles(self, faces):
        painter = QPainter(self)
        frame = QImage(self._frame.tostring(), self._frame.width, self._frame.height, QImage.Format_RGB888).rgbSwapped()
        painter.drawImage(QPoint(0, 0), frame)
        painter.setPen(Qt.green)
        for (x, y, w, h) in faces:
            painter.drawRect(x, y, w, h)

    def getFaceRectangle(self):
        if self._frame is None:
            return
        tmp = numpy.asarray(self._frame[:,:])
        gray = cv2.cvtColor(tmp, cv2.COLOR_BGR2GRAY)
        faces = self._faceCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30),
                                                   flags = cv.CV_HAAR_SCALE_IMAGE)
        if len(faces) == 1:
            frame = QImage(self._frame.tostring(), self._frame.width, self._frame.height, QImage.Format_RGB888).rgbSwapped()
            for (x,y,w,h) in faces:
                return frame.copy(x,y,w,h)
        else:
            return



