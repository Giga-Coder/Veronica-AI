# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\VeronicaUi.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1316, 740)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bg = QtWidgets.QLabel(self.centralwidget)
        self.bg.setGeometry(QtCore.QRect(0, 0, 1391, 781))
        self.bg.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.bg.setText("")
        self.bg.setObjectName("bg")
        self.border = QtWidgets.QLabel(self.centralwidget)
        self.border.setGeometry(QtCore.QRect(0, 0, 1351, 741))
        self.border.setStyleSheet("color: rgb(90, 90, 90);\n"
"background-color: rgb(0, 0, 0);\n"
"border: 7px Solid White;")
        self.border.setText("")
        self.border.setObjectName("border")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1170, 640, 141, 61))
        self.pushButton.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border: 4px Solid white;\n"
"border-radius: 25px;\n"
"text-align: center;\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(990, 640, 141, 61))
        self.pushButton_2.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"background-color: rgb(255, 85, 0);\n"
"border: 4px Solid white;\n"
"border-radius: 25px;\n"
"text-align: center;\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.image = QtWidgets.QLabel(self.centralwidget)
        self.image.setGeometry(QtCore.QRect(450, 60, 451, 111))
        self.image.setStyleSheet("border: 2px solid white\n")
        self.image.setText("")
        self.image.setPixmap(QtGui.QPixmap(".\\GUI/image.png"))
        self.image.setObjectName("image")
        self.gif2 = QtWidgets.QLabel(self.centralwidget)
        self.gif2.setGeometry(QtCore.QRect(470, 170, 371, 311))
        self.gif2.setText("")
        self.gif2.setPixmap(QtGui.QPixmap(".\\GUI/gif2.gif"))
        self.gif2.setObjectName("gif2")
        self.gif3 = QtWidgets.QLabel(self.centralwidget)
        self.gif3.setGeometry(QtCore.QRect(1010, 60, 301, 211))
        self.gif3.setStyleSheet("border: 2px solid white;")
        self.gif3.setText("")
        self.gif3.setPixmap(QtGui.QPixmap(".\\GUI/gif3.gif"))
        self.gif3.setObjectName("gif3")
        self.gif4 = QtWidgets.QLabel(self.centralwidget)
        self.gif4.setGeometry(QtCore.QRect(1000, 300, 301, 191))
        self.gif4.setText("")
        self.gif4.setPixmap(QtGui.QPixmap(".\\GUI/gif4.gif"))
        self.gif4.setScaledContents(True)
        self.gif4.setObjectName("gif4")
        self.gif5 = QtWidgets.QLabel(self.centralwidget)
        self.gif5.setGeometry(QtCore.QRect(10, 50, 311, 241))
        self.gif5.setStyleSheet("border: 2px solid white;")
        self.gif5.setText("")
        self.gif5.setPixmap(QtGui.QPixmap(".\\GUI/gif5.gif"))
        self.gif5.setScaledContents(True)
        self.gif5.setObjectName("gif5")
        self.gif6 = QtWidgets.QLabel(self.centralwidget)
        self.gif6.setGeometry(QtCore.QRect(10, 293, 311, 211))
        self.gif6.setStyleSheet("border: 2px solid white;")
        self.gif6.setText("")
        self.gif6.setPixmap(QtGui.QPixmap(".\\GUI/gif6.gif"))
        self.gif6.setScaledContents(True)
        self.gif6.setObjectName("gif6")
        self.terminal = QtWidgets.QLabel(self.centralwidget)
        self.terminal.setGeometry(QtCore.QRect(10, 500, 521, 231))
        self.terminal.setStyleSheet("border: 5px solid white;")
        self.terminal.setObjectName("terminal")
        self.gif7 = QtWidgets.QLabel(self.centralwidget)
        self.gif7.setGeometry(QtCore.QRect(560, 490, 391, 171))
        self.gif7.setText("")
        self.gif7.setPixmap(QtGui.QPixmap(".\\GUI/gif7.gif"))
        self.gif7.setScaledContents(True)
        self.gif7.setObjectName("gif7")
        self.gif9 = QtWidgets.QLabel(self.centralwidget)
        self.gif9.setGeometry(QtCore.QRect(340, 270, 621, 161))
        self.gif9.setText("")
        self.gif9.setPixmap(QtGui.QPixmap(".\\GUI/gif9.gif"))
        self.gif9.setScaledContents(True)
        self.gif9.setObjectName("gif9")
        self.gif8 = QtWidgets.QLabel(self.centralwidget)
        self.gif8.setGeometry(QtCore.QRect(1100, 10, 211, 51))
        self.gif8.setText("")
        self.gif8.setPixmap(QtGui.QPixmap(".\\GUI/gif8.gif"))
        self.gif8.setScaledContents(True)
        self.gif8.setObjectName("gif8")
        self.gif10 = QtWidgets.QLabel(self.centralwidget)
        self.gif10.setGeometry(QtCore.QRect(20, 10, 151, 31))
        self.gif10.setText("")
        self.gif10.setPixmap(QtGui.QPixmap(".\\GUI/gif10.gif"))
        self.gif10.setObjectName("gif10")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(1080, 520, 55, 16))
        self.label.setObjectName("label")
        self.time = QtWidgets.QLabel(self.centralwidget)
        self.time.setGeometry(QtCore.QRect(980, 540, 331, 71))
        self.time.setStyleSheet("border: 2px solid white;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"font: 20pt \"Arial Black\";\n"
"color: white;\n"
"background-color: rgb(0, 0, 0);")
        self.time.setText("")
        self.time.setObjectName("time")
        self.bg.raise_()
        self.border.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.gif3.raise_()
        self.image.raise_()
        self.gif4.raise_()
        self.gif5.raise_()
        self.gif6.raise_()
        self.terminal.raise_()
        self.gif7.raise_()
        self.gif9.raise_()
        self.gif2.raise_()
        self.gif8.raise_()
        self.gif10.raise_()
        self.label.raise_()
        self.time.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "STOP"))
        self.pushButton_2.setText(_translate("MainWindow", "START"))
        self.terminal.setText(_translate("MainWindow", "TextLabel"))
        self.label.setText(_translate("MainWindow", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())