import pygame
from ControleSom import ControleSom
from ControleTop import ControleTop
from PyQt5 import QtCore, QtGui, QtWidgets, QtTest


class Interface:
    def __init__(self, janela, mediador):
        self.mediador = mediador
        self.janela = janela
        self.som = ControleSom()
        self.ranking = ControleTop()
        self.centralwidget = QtWidgets.QWidget(self.janela)
        self.inserirNome = QtWidgets.QLineEdit(self.janela)
        self.botaoOK = QtWidgets.QPushButton('OK', self.janela)
        self.textoNome = QtWidgets.QStatusBar(self.janela)
        self.botaoVerde = QtWidgets.QPushButton(self.centralwidget)
        self.botaoVermelho = QtWidgets.QPushButton(self.centralwidget)
        self.botaoAzul = QtWidgets.QPushButton(self.centralwidget)
        self.botaoAmarelo = QtWidgets.QPushButton(self.centralwidget)
        self.botaoSom = QtWidgets.QPushButton(self.centralwidget)
        self.botaoConf = QtWidgets.QPushButton(self.centralwidget)
        self.botaoTop = QtWidgets.QPushButton(self.centralwidget)
        self.logo = QtWidgets.QPushButton(self.centralwidget)
        self.botaoOnOff = QtWidgets.QPushButton(self.centralwidget)
        self.bg_logo = QtWidgets.QPushButton(self.centralwidget)
        self.pontuacao = QtWidgets.QLCDNumber(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self.janela)
        self.statusbar = QtWidgets.QStatusBar(self.janela)

        self.configuraUi()
        self.funcoesBotoes()
        self.efeitoInicializacao()

    def configuraUi(self):
        self.__configuraJanela()
        self.__configuraJanelaTop10()
        self.__configuraBotaoVermelho()
        self.__configuraBotaoAmarelo()
        self.__configuraBotaoVerde()
        self.__configuraBotaoAzul()
        self.__configuraBotaoOnOff()
        self.__configuraBotaoSom()
        self.__configuraBotaoTop()
        self.__configuraBotaoConf()
        self.__configuraFundoLogo()
        self.__configuraLogo()
        self.__configuraDisplay()
        self.__configuraCaixaInserirNome()
        self.__configuraBotaoOK()
        self.__configuraTextoInfo()
        self.__configuraCamadasWidgets()


        self.janela.setCentralWidget(self.centralwidget)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 451, 21))
        self.menubar.setObjectName("menubar")
        self.janela.setMenuBar(self.menubar)
        self.statusbar.setObjectName("statusbar")
        self.janela.setStatusBar(self.statusbar)
        _translate = QtCore.QCoreApplication.translate
        self.janela.setWindowTitle(_translate("Genius", "Genius"))
        QtCore.QMetaObject.connectSlotsByName(self.janela)

    def __configuraJanelaTop10(self):
        self.ranking.abrirArquivo()
        self.ranking.ordenarTop10()
        top10 = self.ranking.getTop10
        self.ranking = ControleTop()
        texto = "Classificação\tPontuação\tNome\n\n"

        for i in range(10):
            jogador = top10[i]
            texto = str(texto) +(str(i+1) + "°\t\t" + str(jogador[1]) + '\t\t'  + str(jogador[0]) + '\n')

        self.janelaTop10 = QtWidgets.QLabel(texto)
        self.janelaTop10.setWindowTitle("Top 10")
        self.janelaTop10.setObjectName("Top 10")
        self.janelaTop10.resize(451,250)
        self.janelaTop10.move(902, 83)
        self.janelaTop10.setStyleSheet("background-color:#1d1d1d; color:green; font:bold 15px; subcontrol-position: right center")

    def __configuraJanela(self):
        self.janela.setObjectName("Genius")
        self.janela.resize(451, 500)
        self.janela.setStyleSheet("background-color:#1d1d1d;")
        self.centralwidget.setObjectName("centralwidget")

    def __configuraBotaoVermelho(self):
        self.botaoVermelho.setObjectName("botaoVermelho")
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

    def __configuraBotaoAmarelo(self):
        self.botaoAmarelo.setObjectName("botaoAmarelo")
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

    def __configuraBotaoVerde(self):
        self.botaoVerde.setObjectName("botaoVerde")
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

    def __configuraBotaoAzul(self):
        self.botaoAzul.setObjectName("botaoAzul")
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

    def __configuraBotaoOnOff(self):
        self.botaoOnOff.setObjectName("botaoOnOff")
        self.botaoOnOff.setGeometry(QtCore.QRect(200, 280, 51, 51))
        self.botaoOnOff.setStyleSheet("#botaoOnOff{\n"
                                      "background-color:transparent;\n"
                                      "border-image: url(\"src/images/bt_off.png\");\n"
                                      "}\n"
                                      "")

    def __configuraBotaoSom(self):
        self.botaoSom.setObjectName("botaoSom")
        self.botaoSom.setGeometry(QtCore.QRect(145, 235, 40, 40))
        self.botaoSom.setStyleSheet("#botaoSom{\n"
                                    "background-color:transparent;\n"
                                    "border-image: url(\"src/images/sound_on.png\");\n"
                                    "}\n"
                                    "")

    def __configuraBotaoTop(self):
        self.botaoTop.setObjectName("botaoTop")
        self.botaoTop.setGeometry(QtCore.QRect(207, 243, 40, 40))
        self.botaoTop.setStyleSheet("#botaoTop{\n"
                                    "background-color:transparent;\n"
                                    "border-image: url(\"src/images/top.png\");\n"
                                    "}\n"
                                    "")

    def __configuraBotaoConf(self):
        self.botaoConf.setObjectName("botaoConf")
        self.botaoConf.setGeometry(QtCore.QRect(265, 235, 40, 40))
        self.botaoConf.setStyleSheet("#botaoConf{\n"
                                     "background-color:transparent;\n"
                                     "border-image: url(\"src/images/number_" + str(self.som.tipo) + ".png\");\n"
                                     "}\n"
                                     "")

    def __configuraFundoLogo(self):
        self.bg_logo.setObjectName("bg_logo")
        self.bg_logo.setGeometry(QtCore.QRect(120, 120, 211, 101))
        self.bg_logo.setStyleSheet("#bg_logo{\n"
                                   "background-color:transparent;\n"
                                   "border-image: url(\"src/images/bg_logo.png\");\n"
                                   "}\n"
                                   "")

    def __configuraLogo(self):
        self.logo.setObjectName("logo")
        self.logo.setGeometry(QtCore.QRect(150, 160, 151, 41))
        self.logo.setStyleSheet("#logo{\n"
                                "background-color:transparent;\n"
                                "border-image: url(\"src/images/logo.png\");\n"
                                "}\n"
                                "")

    def __configuraDisplay(self):
        self.pontuacao.setObjectName("pontuacao")
        self.pontuacao.setGeometry(QtCore.QRect(200, 205, 51, 31))
        self.pontuacao.setMinimumSize(QtCore.QSize(41, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setKerning(True)
        self.pontuacao.setFont(font)
        self.pontuacao.setProperty("value", 0.0)
        self.pontuacao.setProperty("intValue", 0)

    def __configuraCaixaInserirNome(self):
        self.inserirNome.move(89, 440)
        self.inserirNome.resize(240, 40)
        self.inserirNome.setStyleSheet("background-color:white; color:black; font:25px")
        self.inserirNome.close()

    def __configuraBotaoOK(self):
        self.botaoOK.resize(40, 40)
        self.botaoOK.move(340, 440)
        self.botaoOK.setStyleSheet("background-color:grey; text: ok; color:black; font:15px")
        self.botaoOK.close()

    def __configuraTextoInfo(self):
        self.textoNome.resize(200, 30)
        self.textoNome.move(2, 410)
        self.textoNome.setStyleSheet("background-color:transparent; color:green; font:15px")

    def __configuraCamadasWidgets(self):
        self.bg_logo.raise_()
        self.logo.raise_()
        self.botaoVermelho.raise_()
        self.botaoAmarelo.raise_()
        self.botaoVerde.raise_()
        self.botaoAzul.raise_()
        self.pontuacao.raise_()
        self.botaoOnOff.raise_()
        self.botaoSom.raise_()
        self.botaoTop.raise_()
        self.botaoConf.raise_()



    def efeitoInicializacao(self):
        self.pausa(1000)
        self.som.tocarSomIntro()

        self.botaoAmarelo.setDown(True)
        QtCore.QTimer.singleShot(400, lambda: self.botaoAmarelo.setDown(False))
        self.botaoAmarelo.setCheckable(True)
        self.botaoAmarelo.setChecked(True)

        self.botaoAzul.setDown(True)
        QtCore.QTimer.singleShot(400, lambda: self.botaoAzul.setDown(False))
        self.botaoAzul.setCheckable(True)
        self.botaoAzul.setChecked(True)

        self.botaoVerde.setDown(True)
        QtCore.QTimer.singleShot(400, lambda: self.botaoVerde.setDown(False))
        self.botaoVerde.setCheckable(True)
        self.botaoVerde.setChecked(True)

        self.botaoVermelho.setDown(True)
        QtCore.QTimer.singleShot(400, lambda: self.botaoVermelho.setDown(False))
        self.botaoVermelho.setCheckable(True)
        self.botaoVermelho.setChecked(True)

    def efeitoErro(self):
        self.som.tocaSomErro()

        self.botaoAmarelo.setDown(True)
        QtCore.QTimer.singleShot(2800, lambda: self.botaoAmarelo.setDown(False))
        self.botaoAmarelo.setCheckable(True)
        self.botaoAmarelo.setChecked(True)

        self.botaoAzul.setDown(True)
        QtCore.QTimer.singleShot(2800, lambda: self.botaoAzul.setDown(False))
        self.botaoAzul.setCheckable(True)
        self.botaoAzul.setChecked(True)

        self.botaoVerde.setDown(True)
        QtCore.QTimer.singleShot(2800, lambda: self.botaoVerde.setDown(False))
        self.botaoVerde.setCheckable(True)
        self.botaoVerde.setChecked(True)

        self.botaoVermelho.setDown(True)
        QtCore.QTimer.singleShot(2800, lambda: self.botaoVermelho.setDown(False))
        self.botaoVermelho.setCheckable(True)
        self.botaoVermelho.setChecked(True)

        self.pausa(2800)






    def funcoesBotoes(self):
        self.botaoOnOff.clicked.connect(self.mediador.ligarDesligar)
        self.botaoAmarelo.clicked.connect(self.pressionarAmarelo)
        self.botaoAzul.clicked.connect(self.pressionarAzul)
        self.botaoVerde.clicked.connect(self.pressionarVerde)
        self.botaoVermelho.clicked.connect(self.pressionarVermelho)
        self.botaoSom.clicked.connect(self.pressionarSom)
        self.botaoConf.clicked.connect(self.pressionarConf)
        self.botaoOK.clicked.connect(self.pressionarOK)
        self.botaoTop.clicked.connect(self.pressionarTop)


    def atualizarPontuacao(self, pontuacao):
        self.pontuacao.display(pontuacao)
        self.pausa()

    def pressionarAmarelo(self):
        self.ligarAmarelo()
        self.mediador.botaoPressionado("amarelo")

    def pressionarAzul(self):
        self.ligarAzul()
        self.mediador.botaoPressionado("azul")

    def pressionarVerde(self):
        self.ligarVerde()
        self.mediador.botaoPressionado("verde")

    def pressionarVermelho(self):
        self.ligarVermelho()
        self.mediador.botaoPressionado("vermelho")

    def pressionarSom(self):
        self.mediador.funcaoMudo()


    def pressionarConf(self):
        if self.som.tipo == self.som.maxTipo:
            self.som.tipo = 1
        else:
            self.som.tipo += 1

        self.botaoConf.setStyleSheet("#botaoConf{border-image: url(\"src/images/number_" + str(self.som.tipo) + ".png\")}")

    def pressionarTop(self):
        if self.janelaTop10.isVisible() == True:
            self.janelaTop10.close()
        else:
            self.__configuraJanelaTop10()
            self.janelaTop10.show()

    def pressionarOK(self):
        if self.inserirNome.text() == "":
            self.textoNome.setStyleSheet("background-color:transparent; color:red; font:15px")
            self.textoNome.showMessage('Nome Inválido!!!')
        else:
            pontuacao = int(self.mediador.getPontuacao)
            nomeJogador = str(self.inserirNome.text())
            self.ranking.addTop10(nomeJogador, pontuacao)
            self.botaoOK.close()
            self.inserirNome.close()
            self.inserirNome.clear()
            self.ranking = ControleTop()
            self.textoNome.clearMessage()
            self.textoNome.setStyleSheet("background-color:transparent; color:green; font:15px")
            self.__configuraJanelaTop10()


    @staticmethod
    def pausa(ms=1000):
        QtTest.QTest.qWait(ms)

    def iniciarJogo(self):
        self.botaoOnOff.setStyleSheet("#botaoOnOff{\n"
                                      "background-color:transparent;\n"
                                      "border-image: url(\"src/images/bt_on.png\");\n"
                                      "}\n"
                                      "")
        self.pausa(500)
        self.habilitarBotoes()

    def jogadaErrada(self):
        self.desligarJogo()
        self.efeitoErro()


    def desligarJogo(self):
        self.botaoOnOff.setStyleSheet("#botaoOnOff{\n"
                                      "background-color:transparent;\n"
                                      "border-image: url(\"src/images/bt_off.png\");\n"
                                      "}\n"
                                      "")

        self.desabilitarBotoes()

    def tocaSequencia(self, sequencia):
        for cor in sequencia:
            if cor == "amarelo":
                self.desabilitarBotoes()
                self.ligarAmarelo()
                self.pausa(300)
                self.habilitarBotoes()

            elif cor == "azul":
                self.desabilitarBotoes()
                self.ligarAzul()
                self.pausa(300)
                self.habilitarBotoes()

            elif cor == "verde":
                self.desabilitarBotoes()
                self.ligarVerde()
                self.pausa(300)
                self.habilitarBotoes()

            elif cor == "vermelho":
                self.desabilitarBotoes()
                self.ligarVermelho()
                self.pausa(300)
                self.habilitarBotoes()

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

    def ligarVermelho(self):
        self.som.tocaSomVermelho()
        self.botaoVermelho.setDown(True)
        QtCore.QTimer.singleShot(400, lambda: self.botaoVermelho.setDown(False))
        self.botaoVermelho.setCheckable(True)
        self.botaoVermelho.setChecked(True)
        self.pausa(400)

    def ligarAmarelo(self):
        self.som.tocaSomAmarelo()
        self.botaoAmarelo.setDown(True)
        QtCore.QTimer.singleShot(400, lambda: self.botaoAmarelo.setDown(False))
        self.botaoAmarelo.setCheckable(True)
        self.botaoAmarelo.setChecked(True)
        self.pausa(400)

    def ligarVerde(self):
        self.som.tocaSomVerde()
        self.botaoVerde.setDown(True)
        QtCore.QTimer.singleShot(400, lambda: self.botaoVerde.setDown(False))
        self.botaoVerde.setCheckable(True)
        self.botaoVerde.setChecked(True)
        self.pausa(400)

    def ligarAzul(self):
        self.som.tocaSomAzul()
        self.botaoAzul.setDown(True)
        QtCore.QTimer.singleShot(400, lambda: self.botaoAzul.setDown(False))
        self.botaoAzul.setCheckable(True)
        self.botaoAzul.setChecked(True)
        self.pausa(400)

    def ativarMudo(self):
        self.som.volume = 0
        self.botaoSom.setStyleSheet("#botaoSom{\n"
                                    "background-color:transparent;\n"
                                    "border-image: url(\"src/images/sound_off.png\");\n"
                                    "}\n"
                                    "")

    def desativarMudo(self):
        self.som.volume = 1
        self.som.tipo = 4
        self.botaoSom.setStyleSheet("#botaoSom{\n"
                                    "background-color:transparent;\n"
                                    "border-image: url(\"src/images/sound_on.png\");\n"
                                    "}\n"
                                    "")

    def solicitarNome(self):
        pontuacao = self.mediador.getPontuacao
        if self.ranking.estaNoTop10(pontuacao) == True:
            self.inserirNome.show()
            self.botaoOK.show()
            self.textoNome.showMessage('Insira seu nome')
