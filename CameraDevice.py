__author__ = 'michal'

from PyQt5.QtCore import *
import cv2

class CameraDevice(QObject):
    __DEFAULT_FPS = 15

    newFrameAvailable = pyqtSignal(cv2.cv.iplimage)

    @pyqtSlot()
    def _queryFrame(self):
        frame = cv2.cv.QueryFrame(self._cameraDevice)
        self.newFrameAvailable.emit(frame)

    def __init__(self, parent = None):
        super(CameraDevice, self).__init__(parent)

        self._cameraDevice = cv2.cv.CaptureFromCAM(0)

        self._timer = QTimer(self)
        self._timer.timeout.connect(self._queryFrame)
        self._timer.setInterval(1000/self.__DEFAULT_FPS)

        self.paused = False

    @property
    def frameSize(self):
        width = cv2.cv.GetCaptureProperty(self._cameraDevice, cv2.cv.CV_CAP_PROP_FRAME_WIDTH)
        height = cv2.cv.GetCaptureProperty(self._cameraDevice, cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)

        return int(width), int(height)

    @property
    def paused(self):
        return not self._timer.isActive()

    @paused.setter
    def paused(self, paused):
        if paused:
            self._timer.stop()
        else:
            self._timer.start()


    @property
    def fps(self):
        fps = int(cv2.cv.GetCaptureProperty(self._cameraDevice, cv2.cv.CV_CAP_PROP_FPS))
        if not fps > 0:
            fps = self.__DEFAULT_FPS
        return fps
