from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtCore import Qt, QTimer, QTime, QDate
from VeronicaUi import Ui_MainWindow  # this file is in ui file
import sys
import os
import psutil
import main  # importing main file


# This class run our Veronica


class MainThread(QThread):

    def __init__(self):  #it restart function again and again

        super(MainThread, self).__init__()
        os.startfile('main.py')
    def run(self):
        self.Task_Gui()
        print("hello123")
    
    def Task_Gui(self):
        os.startfile('main.py')







class Gui_Start(QMainWindow):

    def __init__(self):
        super().__init__()
        self.Veronica_ui = Ui_MainWindow()
        self.Veronica_ui.setupUi(self)
        self.Veronica_ui.pushButton_2.clicked.connect(self.startFunc)
        self.Veronica_ui.pushButton.clicked.connect(self.close)
        if self.Veronica_ui.pushButton.clicked.connect(self.close):
            print("hello")


        # GUI move
    def startFunc(self):
        self.Veronica_ui.movies2 = QtGui.QMovie(".\\GUI/gif2.gif")
        self.Veronica_ui.gif2.setMovie(self.Veronica_ui.movies2)
        self.Veronica_ui.movies2.start()

        self.Veronica_ui.movies3 = QtGui.QMovie(".\\GUI/gif3.gif")
        self.Veronica_ui.gif3.setMovie(self.Veronica_ui.movies3)
        self.Veronica_ui.movies3.start()

        self.Veronica_ui.movies4 = QtGui.QMovie(".\\GUI/gif4.gif")
        self.Veronica_ui.gif4.setMovie(self.Veronica_ui.movies4)
        self.Veronica_ui.movies4.start()

        self.Veronica_ui.movies5 = QtGui.QMovie(".\\GUI/gif5.gif")
        self.Veronica_ui.gif5.setMovie(self.Veronica_ui.movies5)
        self.Veronica_ui.movies5.start()

        self.Veronica_ui.movies6 = QtGui.QMovie(".\\GUI/gif6.gif")
        self.Veronica_ui.gif6.setMovie(self.Veronica_ui.movies6)
        self.Veronica_ui.movies6.start()

        self.Veronica_ui.movies7 = QtGui.QMovie(".\\GUI/gif7.gif")
        self.Veronica_ui.gif7.setMovie(self.Veronica_ui.movies7)
        self.Veronica_ui.movies7.start()

        self.Veronica_ui.movies8 = QtGui.QMovie(".\\GUI/gif8.gif")
        self.Veronica_ui.gif8.setMovie(self.Veronica_ui.movies8)
        self.Veronica_ui.movies8.start()

        self.Veronica_ui.movies10 = QtGui.QMovie(".\\GUI/gif9.gif")
        self.Veronica_ui.gif9.setMovie(self.Veronica_ui.movies10)
        self.Veronica_ui.movies10.start()

        self.Veronica_ui.movies10 = QtGui.QMovie(".\\GUI/gif10.gif")
        self.Veronica_ui.gif10.setMovie(self.Veronica_ui.movies10)
        self.Veronica_ui.movies10.start()

    #     timer = QTimer(self)
    #     timer.timeout.connect(self.showtime)
    #
    #     timer.start(1000)
    #
    #     startFunctions.start()
    #
    # def showtime(self):
    #     current_time = QTime.currentTime()
    #     label_time = current_time.toString("hh:mm:ss")
    #     label = "Time: " + label_time
    #     self.Veronica_ui..setText(label)

startFunctions = MainThread()
Gui_App = QApplication(sys.argv)

Gui_Veronica = Gui_Start()

Gui_Veronica.show()



exit(Gui_App.exec())









