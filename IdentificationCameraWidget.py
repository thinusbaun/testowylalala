__author__ = 'michal'

import numpy
import cv2
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from CameraWidget import CameraWidget

class IdentificationCameraWidget(CameraWidget):
    def __init__(self, device, recognizer, parent = None):
        super(IdentificationCameraWidget, self).__init__(device, parent)
        self.recognizer = recognizer

    def paintRectangles(self, faces):
        painter = QPainter(self)
        frame = QImage(self._frame.tostring(), self._frame.width, self._frame.height, QImage.Format_RGB888).rgbSwapped()
        painter.drawImage(QPoint(0, 0), frame)
        painter.setPen(Qt.red)
        for (x, y, w, h) in faces:
            face = numpy.asarray(self._frame[y:y+w,x:x+h])
            grayface = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
            grayresizedface = cv2.resize(grayface, (100, 100))
            [p_class, p_confidence] = self.recognizer.recognizePerson(grayresizedface)
            if p_class != -1:
                text = self.recognizer.labels[p_class] + "\n" + str(p_confidence)
            else:
                text = "Nie rozpoznano"
            painter.drawText(x,y,w,h, Qt.AlignLeft, text)
            painter.drawRect(x, y, w, h)
