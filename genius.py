# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_GeniusWindows.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Ui_Genius(object):
    def __init__(self, window):
        self.centralwidget = QtWidgets.QWidget(Genius)
        self.verde = QtWidgets.QPushButton(self.centralwidget)
        self.vermelho = QtWidgets.QPushButton(self.centralwidget)
        self.azul = QtWidgets.QPushButton(self.centralwidget)
        self.amarelo = QtWidgets.QPushButton(self.centralwidget)
        self.logo = QtWidgets.QPushButton(self.centralwidget)
        self.onoff = QtWidgets.QPushButton(self.centralwidget)
        self.bg_logo = QtWidgets.QPushButton(self.centralwidget)
        self.pontuacao = QtWidgets.QLCDNumber(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Genius)
        self.statusbar = QtWidgets.QStatusBar(Genius)

        self.window = Genius
        self.setupUi()

    def setupUi(self):
        self.window.setObjectName("Genius")
        self.window.resize(451, 498)
        self.window.setStyleSheet("background-color:#1d1d1d;")
        self.centralwidget.setObjectName("centralwidget")
        self.verde.setGeometry(QtCore.QRect(20, 20, 200, 200))
        self.verde.setStyleSheet("#verde{\n"
                                 "background-color:transparent;\n"
                                 "border-image: url(\"src/images/bt_verde.png\");\n"
                                 "}\n"
                                 "\n"
                                 "#verde:pressed{\n"
                                 "background-color:transparent;\n"
                                 "border-image: url(\"src/images/bt_verdeAct.png\");\n"
                                 "}")
        self.verde.setObjectName("verde")
        self.vermelho.setGeometry(QtCore.QRect(230, 20, 200, 200))
        self.vermelho.setStyleSheet("#vermelho{\n"
                                    "background-color:transparent;\n"
                                    "border-image: url(\"src/images/bt_vermelho.png\");\n"
                                    "}\n"
                                    "\n"
                                    "#vermelho:pressed{\n"
                                    "background-color:transparent;\n"
                                    "border-image: url(\"src/images/bt_vermelhoAct.png\");\n"
                                    "}")
        self.vermelho.setObjectName("vermelho")
        self.azul.setGeometry(QtCore.QRect(230, 230, 200, 200))
        self.azul.setStyleSheet("#azul{\n"
                                "background-color:transparent;\n"
                                "border-image: url(\"src/images/bt_azul.png\");\n"
                                "}\n"
                                "\n"
                                "#azul:pressed{\n"
                                "background-color:transparent;\n"
                                "border-image: url(\"src/images/bt_azulAct.png\");\n"
                                "}")
        self.azul.setObjectName("azul")
        self.amarelo.setGeometry(QtCore.QRect(20, 230, 200, 200))
        self.amarelo.setStyleSheet("#amarelo{\n"
                                   "background-color:transparent;\n"
                                   "border-image: url(\"src/images/bt_amarelo.png\");\n"
                                   "}\n"
                                   "\n"
                                   "#amarelo:pressed{\n"
                                   "background-color:transparent;\n"
                                   "border-image: url(\"src/images/bt_amareloAct.png\");\n"
                                   "}")
        self.amarelo.setObjectName("amarelo")
        self.logo.setGeometry(QtCore.QRect(150, 160, 151, 41))
        self.logo.setStyleSheet("#logo{\n"
                                "background-color:transparent;\n"
                                "border-image: url(\"src/images/logo.png\");\n"
                                "}\n"
                                "")
        self.logo.setObjectName("logo")
        self.onoff.setGeometry(QtCore.QRect(200, 280, 51, 51))
        self.onoff.setStyleSheet("#onoff{\n"
                                 "background-color:transparent;\n"
                                 "border-image: url(\"src/images/bt_off.png\");\n"
                                 "}\n"
                                 "")
        self.onoff.setObjectName("onoff")
        self.bg_logo.setGeometry(QtCore.QRect(120, 120, 211, 101))
        self.bg_logo.setStyleSheet("#bg_logo{\n"
                                   "background-color:transparent;\n"
                                   "border-image: url(\"src/images/bg_logo.png\");\n"
                                   "}\n"
                                   "")
        self.bg_logo.setObjectName("bg_logo")
        self.pontuacao.setGeometry(QtCore.QRect(200, 240, 51, 31))
        self.pontuacao.setMinimumSize(QtCore.QSize(41, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setKerning(True)
        self.pontuacao.setFont(font)
        self.pontuacao.setProperty("value", 0.0)
        self.pontuacao.setProperty("intValue", 0)
        self.pontuacao.setObjectName("pontuacao")
        self.azul.raise_()
        self.bg_logo.raise_()
        self.vermelho.raise_()
        self.amarelo.raise_()
        self.logo.raise_()
        self.onoff.raise_()
        self.verde.raise_()
        self.pontuacao.raise_()
        self.window.setCentralWidget(self.centralwidget)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 451, 21))
        self.menubar.setObjectName("menubar")
        self.window.setMenuBar(self.menubar)
        self.statusbar.setObjectName("statusbar")
        self.window.setStatusBar(self.statusbar)
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.window)

        self.functions()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.window.setWindowTitle(_translate("Genius", "MainWindow"))

    def functions(self):
        pass

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Genius = QtWidgets.QMainWindow()
    ui = Ui_Genius(Genius)
    Genius.show()
    sys.exit(app.exec_())
