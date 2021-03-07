import sys
#Requires Installation of PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from newWindow import Ui_newWindow

#Class to initialize a new instance of QApplication module which is required to run PyQt5
class StartApp:
    def __init__(self):
        self.QApp = QApplication(sys.argv)

#Class to create a new Window
class NewWindow:
    def __init__(self,name,xlen,ylen):
        #Initialize new instance of window ui
        self.QWin = QMainWindow()
        #Set Window Title
        self.QWin.setWindowTitle(name)
        #Set Window Size
        self.QWin.resize(xlen,ylen)

    #Method to set Window icon image
    def setWindowIcon(self,image):
        self.QWin.setWindowIcon(QtGui.QIcon(image))

#Class to create a new Label
class NewLabel:
    def __init__(self, Window,posx,posy,xlen,ylen):
        #Window parameter to control which window it appears on
        self.label = QLabel(Window)
        #Set window x & y position and window size
        self.label.setGeometry(QtCore.QRect(posx,posy,xlen,ylen))
        #Set alignment of Label text to align center
        self.label.setAlignment(QtCore.Qt.AlignCenter)

    #Method to set Label Text
    def setText(self,text):
        self.label.setText(text)