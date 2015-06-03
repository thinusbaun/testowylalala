__author__ = 'michal'
import sys
from PyQt5.QtWidgets import *
import mainWindow

if __name__=="__main__":
    app = QApplication(sys.argv)
    w = mainWindow.MainWindow()
    w.show()
    sys.exit(app.exec_())
