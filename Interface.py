# -*- coding: utf-8 -*-
import pygame
from PyQt5 import QtCore, QtGui, QtWidgets

from Mediado import Mediado


class Interface(Mediado):
    def __init__(self, janela, mediador):
        super().__init__(mediador)
        self.janela = janela
        self.centralwidget = QtWidgets.QWidget(self.janela)
        self.botaoVerde = QtWidgets.QPushButton(self.centralwidget)
        self.botaoVermelho = QtWidgets.QPushButton(self.centralwidget)
        self.botaoAzul = QtWidgets.QPushButton(self.centralwidget)
        self.botaoAmarelo = QtWidgets.QPushButton(self.centralwidget)
        self.logo = QtWidgets.QPushButton(self.centralwidget)
        self.botaoOnOff = QtWidgets.QPushButton(self.centralwidget)
        self.bg_logo = QtWidgets.QPushButton(self.centralwidget)
        self.pontuacao = QtWidgets.QLCDNumber(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self.janela)
        self.statusbar = QtWidgets.QStatusBar(self.janela)

        self.configuraUi()
        self.funcoesBotoes()

        self.ligarAmarelo()
        QtCore.QTimer.singleShot(20000, lambda: int(9))
        self.ligarAzul()
        self.ligarVerde()
        self.ligarVermelho()

    def configuraUi(self):
        self.janela.setObjectName("Genius")
        self.janela.resize(451, 498)
        self.janela.setStyleSheet("background-color:#1d1d1d;")
        self.centralwidget.setObjectName("centralwidget")
        self.botaoVerde.setGeometry(QtCore.QRect(20, 20, 200, 200))
        self.botaoVerde.setStyleSheet("#botaoVerde{\n"
                                      "background-color:transparent;\n"
                                      "border-image: url(\"src/images/bt_verde.png\");\n"
                                      "}\n"
                                      "\n"
                                      "#botaoVerde:pressed{\n"
                                      "background-color:transparent;\n"
                                      "border-image: url(\"src/images/bt_verdeAct.png\");\n"
                                      "}")
        self.botaoVerde.setObjectName("botaoVerde")
        self.botaoVermelho.setGeometry(QtCore.QRect(230, 20, 200, 200))
        self.botaoVermelho.setStyleSheet("#botaoVermelho{\n"
                                         "background-color:transparent;\n"
                                         "border-image: url(\"src/images/bt_vermelho.png\");\n"
                                         "}\n"
                                         "\n"
                                         "#botaoVermelho:pressed{\n"
                                         "background-color:transparent;\n"
                                         "border-image: url(\"src/images/bt_vermelhoAct.png\");\n"
                                         "}")
        self.botaoVermelho.setObjectName("botaoVermelho")
        self.botaoAzul.setGeometry(QtCore.QRect(230, 230, 200, 200))
        self.botaoAzul.setStyleSheet("#botaoAzul{\n"
                                     "background-color:transparent;\n"
                                     "border-image: url(\"src/images/bt_azul.png\");\n"
                                     "}\n"
                                     "\n"
                                     "#botaoAzul:pressed{\n"
                                     "background-color:transparent;\n"
                                     "border-image: url(\"src/images/bt_azulAct.png\");\n"
                                     "}")
        self.botaoAzul.setObjectName("botaoAzul")
        self.botaoAmarelo.setGeometry(QtCore.QRect(20, 230, 200, 200))
        self.botaoAmarelo.setStyleSheet("#botaoAmarelo{\n"
                                        "background-color:transparent;\n"
                                        "border-image: url(\"src/images/bt_amarelo.png\");\n"
                                        "}\n"
                                        "\n"
                                        "#botaoAmarelo:pressed{\n"
                                        "background-color:transparent;\n"
                                        "border-image: url(\"src/images/bt_amareloAct.png\");\n"
                                        "}")
        self.botaoAmarelo.setObjectName("botaoAmarelo")
        self.logo.setGeometry(QtCore.QRect(150, 160, 151, 41))
        self.logo.setStyleSheet("#logo{\n"
                                "background-color:transparent;\n"
                                "border-image: url(\"src/images/logo.png\");\n"
                                "}\n"
                                "")
        self.logo.setObjectName("logo")
        self.botaoOnOff.setGeometry(QtCore.QRect(200, 280, 51, 51))
        self.botaoOnOff.setStyleSheet("#botaoOnOff{\n"
                                      "background-color:transparent;\n"
                                      "border-image: url(\"src/images/bt_off.png\");\n"
                                      "}\n"
                                      "")
        self.botaoOnOff.setObjectName("botaoOnOff")
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
        self.botaoAzul.raise_()
        self.bg_logo.raise_()
        self.botaoVermelho.raise_()
        self.botaoAmarelo.raise_()
        self.logo.raise_()
        self.botaoOnOff.raise_()
        self.botaoVerde.raise_()
        self.pontuacao.raise_()
        self.janela.setCentralWidget(self.centralwidget)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 451, 21))
        self.menubar.setObjectName("menubar")
        self.janela.setMenuBar(self.menubar)
        self.statusbar.setObjectName("statusbar")
        self.janela.setStatusBar(self.statusbar)
        _translate = QtCore.QCoreApplication.translate
        self.janela.setWindowTitle(_translate("Genius", "MainWindow"))
        QtCore.QMetaObject.connectSlotsByName(self.janela)

    def funcoesBotoes(self):
        self.botaoOnOff.clicked.connect(self.mediador.ligarDesligar)
        self.botaoAmarelo.clicked.connect(self.ligarAmarelo)
        self.botaoAzul.clicked.connect(self.ligarAzul)
        self.botaoVerde.clicked.connect(self.ligarVerde)
        self.botaoVermelho.clicked.connect(self.ligarVermelho)

    def pausa(self, i):
        i += 1
        if i < 999:
            QtCore.QTimer.singleShot(2000, lambda: self.pausa(i))

    def iniciarJogo(self):
        self.pausa(1)
        self.ligarAmarelo()
        self.pausa(1)
        self.botaoOnOff.setStyleSheet("#botaoOnOff{\n"
                                      "background-color:transparent;\n"
                                      "border-image: url(\"src/images/bt_on.png\");\n"
                                      "}\n"
                                      "")

    def desligarJogo(self):
        self.botaoOnOff.setStyleSheet("#botaoOnOff{\n"
                                      "background-color:transparent;\n"
                                      "border-image: url(\"src/images/bt_off.png\");\n"
                                      "}\n"
                                      "")

    def novaSequencia(self, sequencia):
        import time

        self.ligarVermelho()

        for cor in sequencia:
            if cor == "amarelo":
                self.ligarAmarelo()
                time.sleep(1)

            elif cor == "azul":
                self.ligarAzul()
                time.sleep(1)

            elif cor == "verde":
                self.ligarAzul()
                time.sleep(1)

            elif cor == "vermelho":
                self.ligarVermelho()
                time.sleep(1)

            self.pausa(1)
            self.ligarAmarelo()
            self.pausa(1)

    def desabilitarBotoes(self):
        self.botaoAmarelo.setEnabled(False)
        self.botaoAzul.setEnabled(False)
        self.botaoVerde.setEnabled(False)
        self.botaoVermelho.setEnabled(False)

    def habilitarBotoes(self):
        self.botaoAmarelo.setEnabled(True)
        self.botaoAzul.setEnabled(True)
        self.botaoVerde.setEnabled(True)
        self.botaoVermelho.setEnabled(True)

    def ligarAmarelo(self):
        # pygame.mixer.init()
        # pygame.mixer.music.load('src/sounds/amarelo.mp3')
        # pygame.mixer.music.play(0)
        self.botaoAmarelo.setDown(True)
        QtCore.QTimer.singleShot(400, lambda: self.botaoAmarelo.setDown(False))
        self.botaoAmarelo.setCheckable(True)
        self.botaoAmarelo.setChecked(True)

    def ligarAzul(self):
        # pygame.mixer.init()
        # pygame.mixer.music.load('src/sounds/azul.mp3')
        # pygame.mixer.music.play(0)
        self.botaoAzul.setDown(True)
        QtCore.QTimer.singleShot(400, lambda: self.botaoAzul.setDown(False))
        self.botaoAzul.setCheckable(True)
        self.botaoAzul.setChecked(True)

    def ligarVerde(self):
        # pygame.mixer.init()
        # pygame.mixer.music.load('src/sounds/verde.mp3')
        # pygame.mixer.music.play(0)
        self.botaoVerde.setDown(True)
        QtCore.QTimer.singleShot(400, lambda: self.botaoVerde.setDown(False))
        self.botaoVerde.setCheckable(True)
        self.botaoVerde.setChecked(True)

    def ligarVermelho(self):
        # pygame.mixer.init()
        # pygame.mixer.music.load('src/sounds/vermelho.mp3')
        # pygame.mixer.music.play(0)
        self.botaoVermelho.setDown(True)
        QtCore.QTimer.singleShot(400, lambda: self.botaoVermelho.setDown(False))
        self.botaoVermelho.setCheckable(True)
        self.botaoVermelho.setChecked(True)
