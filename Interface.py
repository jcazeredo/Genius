from ControleSom import ControleSom
from ControleTop import ControleTop
from PyQt5 import QtCore, QtGui, QtWidgets, QtTest


class Interface:
    def __init__(self, janela, mediador):
        self.__mediador = mediador
        self.__janela = janela
        self.__som = ControleSom()
        self.__ranking = ControleTop()

        self.__configuraUi()
        self.__funcoesBotoes()
        self.__efeitoInicializacao()

    def __configuraUi(self):
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


        self.__janela.setCentralWidget(self.__centralwidget)
        self.__menubar.setGeometry(QtCore.QRect(0, 0, 451, 21))
        self.__menubar.setObjectName("menubar")
        self.__janela.setMenuBar(self.__menubar)
        self.__statusbar.setObjectName("statusbar")
        self.__janela.setStatusBar(self.__statusbar)
        _translate = QtCore.QCoreApplication.translate
        self.__janela.setWindowTitle(_translate("Genius", "Genius"))
        QtCore.QMetaObject.connectSlotsByName(self.__janela)

    def __configuraJanela(self):
        self.__centralwidget = QtWidgets.QWidget(self.__janela)
        self.__menubar = QtWidgets.QMenuBar(self.__janela)
        self.__statusbar = QtWidgets.QStatusBar(self.__janela)

        self.__janela.setObjectName("Genius")
        self.__janela.resize(451, 500)
        self.__janela.setStyleSheet("background-color:#1d1d1d;")
        self.__centralwidget.setObjectName("centralwidget")

    def __configuraJanelaTop10(self):
        self.__ranking.abrirArquivo()
        self.__ranking.ordenarTop10()
        top10 = self.__ranking.getTop10
        self.__ranking = ControleTop()
        texto = "Classificação\tPontuação\tNome\n\n"

        for i in range(10):
            jogador = top10[i]
            texto = str(texto) +(str(i+1) + "°\t\t" + str(jogador[1]) + '\t\t'  + str(jogador[0]) + '\n')

        self.__janelaTop10 = QtWidgets.QLabel(texto)
        self.__janelaTop10.setWindowTitle("Top 10")
        self.__janelaTop10.setObjectName("Top 10")
        self.__janelaTop10.resize(451,250)
        self.__janelaTop10.move(902, 83)
        self.__janelaTop10.setStyleSheet("background-color:#1d1d1d; color:green; font:bold 15px; subcontrol-position: right center")

    def __configuraBotaoVermelho(self):
        self.__botaoVermelho = QtWidgets.QPushButton(self.__centralwidget)
        self.__botaoVermelho.setObjectName("botaoVermelho")
        self.__botaoVermelho.setGeometry(QtCore.QRect(230, 20, 200, 200))
        self.__botaoVermelho.setStyleSheet("#botaoVermelho{\n"
                                         "background-color:transparent;\n"
                                         "border-image: url(\"src/images/bt_vermelho.png\");\n"
                                         "}\n"
                                         "\n"
                                         "#botaoVermelho:pressed{\n"
                                         "background-color:transparent;\n"
                                         "border-image: url(\"src/images/bt_vermelhoAct.png\");\n"
                                         "}")

    def __configuraBotaoAmarelo(self):
        self.__botaoAmarelo = QtWidgets.QPushButton(self.__centralwidget)
        self.__botaoAmarelo.setObjectName("botaoAmarelo")
        self.__botaoAmarelo.setGeometry(QtCore.QRect(20, 230, 200, 200))
        self.__botaoAmarelo.setStyleSheet("#botaoAmarelo{\n"
                                        "background-color:transparent;\n"
                                        "border-image: url(\"src/images/bt_amarelo.png\");\n"
                                        "}\n"
                                        "\n"
                                        "#botaoAmarelo:pressed{\n"
                                        "background-color:transparent;\n"
                                        "border-image: url(\"src/images/bt_amareloAct.png\");\n"
                                        "}")

    def __configuraBotaoVerde(self):
        self.__botaoVerde = QtWidgets.QPushButton(self.__centralwidget)
        self.__botaoVerde.setObjectName("botaoVerde")
        self.__botaoVerde.setGeometry(QtCore.QRect(20, 20, 200, 200))
        self.__botaoVerde.setStyleSheet("#botaoVerde{\n"
                                      "background-color:transparent;\n"
                                      "border-image: url(\"src/images/bt_verde.png\");\n"
                                      "}\n"
                                      "\n"
                                      "#botaoVerde:pressed{\n"
                                      "background-color:transparent;\n"
                                      "border-image: url(\"src/images/bt_verdeAct.png\");\n"
                                      "}")

    def __configuraBotaoAzul(self):
        self.__botaoAzul = QtWidgets.QPushButton(self.__centralwidget)
        self.__botaoAzul.setObjectName("botaoAzul")
        self.__botaoAzul.setGeometry(QtCore.QRect(230, 230, 200, 200))
        self.__botaoAzul.setStyleSheet("#botaoAzul{\n"
                                     "background-color:transparent;\n"
                                     "border-image: url(\"src/images/bt_azul.png\");\n"
                                     "}\n"
                                     "\n"
                                     "#botaoAzul:pressed{\n"
                                     "background-color:transparent;\n"
                                     "border-image: url(\"src/images/bt_azulAct.png\");\n"
                                     "}")

    def __configuraBotaoOnOff(self):
        self.__botaoOnOff = QtWidgets.QPushButton(self.__centralwidget)
        self.__botaoOnOff.setObjectName("botaoOnOff")
        self.__botaoOnOff.setGeometry(QtCore.QRect(200, 280, 51, 51))
        self.__botaoOnOff.setStyleSheet("#botaoOnOff{\n"
                                      "background-color:transparent;\n"
                                      "border-image: url(\"src/images/bt_off.png\");\n"
                                      "}\n"
                                      "")

    def __configuraBotaoSom(self):
        self.__botaoSom = QtWidgets.QPushButton(self.__centralwidget)
        self.__botaoSom.setObjectName("botaoSom")
        self.__botaoSom.setGeometry(QtCore.QRect(145, 235, 40, 40))
        self.__botaoSom.setStyleSheet("#botaoSom{\n"
                                    "background-color:transparent;\n"
                                    "border-image: url(\"src/images/sound_on.png\");\n"
                                    "}\n"
                                    "")

    def __configuraBotaoTop(self):
        self.__botaoTop = QtWidgets.QPushButton(self.__centralwidget)
        self.__botaoTop.setObjectName("botaoTop")
        self.__botaoTop.setGeometry(QtCore.QRect(207, 243, 40, 40))
        self.__botaoTop.setStyleSheet("#botaoTop{\n"
                                    "background-color:transparent;\n"
                                    "border-image: url(\"src/images/top.png\");\n"
                                    "}\n"
                                    "")

    def __configuraBotaoConf(self):
        self.__botaoConf = QtWidgets.QPushButton(self.__centralwidget)
        self.__botaoConf.setObjectName("botaoConf")
        self.__botaoConf.setGeometry(QtCore.QRect(265, 235, 40, 40))
        self.__botaoConf.setStyleSheet("#botaoConf{\n"
                                     "background-color:transparent;\n"
                                     "border-image: url(\"src/images/number_" + str(self.__som.tipo) + ".png\");\n"
                                     "}\n"
                                     "")

    def __configuraFundoLogo(self):
        self.__bg_logo = QtWidgets.QPushButton(self.__centralwidget)
        self.__bg_logo.setObjectName("bg_logo")
        self.__bg_logo.setGeometry(QtCore.QRect(120, 120, 211, 101))
        self.__bg_logo.setStyleSheet("#bg_logo{\n"
                                   "background-color:transparent;\n"
                                   "border-image: url(\"src/images/bg_logo.png\");\n"
                                   "}\n"
                                   "")

    def __configuraLogo(self):
        self.__logo = QtWidgets.QPushButton(self.__centralwidget)
        self.__logo.setObjectName("logo")
        self.__logo.setGeometry(QtCore.QRect(150, 160, 151, 41))
        self.__logo.setStyleSheet("#logo{\n"
                                "background-color:transparent;\n"
                                "border-image: url(\"src/images/logo.png\");\n"
                                "}\n"
                                "")

    def __configuraDisplay(self):
        self.__display = QtWidgets.QLCDNumber(self.__centralwidget)
        self.__display.setObjectName("pontuacao")
        self.__display.setGeometry(QtCore.QRect(200, 205, 51, 31))
        self.__display.setMinimumSize(QtCore.QSize(41, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setKerning(True)
        self.__display.setFont(font)
        self.__display.setProperty("value", 0.0)
        self.__display.setProperty("intValue", 0)

    def __configuraCaixaInserirNome(self):
        self.__inserirNome = QtWidgets.QLineEdit(self.__janela)
        self.__inserirNome.move(89, 440)
        self.__inserirNome.resize(240, 40)
        self.__inserirNome.setStyleSheet("background-color:white; color:black; font:25px")
        self.__inserirNome.close()

    def __configuraBotaoOK(self):
        self.__botaoOK = QtWidgets.QPushButton('OK', self.__janela)
        self.__botaoOK.resize(40, 40)
        self.__botaoOK.move(340, 440)
        self.__botaoOK.setStyleSheet("background-color:grey; text: ok; color:black; font:15px")
        self.__botaoOK.close()

    def __configuraTextoInfo(self):
        self.__textoNome = QtWidgets.QStatusBar(self.__janela)
        self.__textoNome.resize(200, 30)
        self.__textoNome.move(2, 410)
        self.__textoNome.setStyleSheet("background-color:transparent; color:green; font:15px")

    def __configuraCamadasWidgets(self):
        self.__bg_logo.raise_()
        self.__logo.raise_()
        self.__botaoVermelho.raise_()
        self.__botaoAmarelo.raise_()
        self.__botaoVerde.raise_()
        self.__botaoAzul.raise_()
        self.__display.raise_()
        self.__botaoOnOff.raise_()
        self.__botaoSom.raise_()
        self.__botaoTop.raise_()
        self.__botaoConf.raise_()

    def __efeitoInicializacao(self):
        self.__pausa(1000)
        self.__som.tocarSomIntro()

        self.__botaoAmarelo.setDown(True)
        QtCore.QTimer.singleShot(400, lambda: self.__botaoAmarelo.setDown(False))
        self.__botaoAmarelo.setCheckable(True)
        self.__botaoAmarelo.setChecked(True)

        self.__botaoAzul.setDown(True)
        QtCore.QTimer.singleShot(400, lambda: self.__botaoAzul.setDown(False))
        self.__botaoAzul.setCheckable(True)
        self.__botaoAzul.setChecked(True)

        self.__botaoVerde.setDown(True)
        QtCore.QTimer.singleShot(400, lambda: self.__botaoVerde.setDown(False))
        self.__botaoVerde.setCheckable(True)
        self.__botaoVerde.setChecked(True)

        self.__botaoVermelho.setDown(True)
        QtCore.QTimer.singleShot(400, lambda: self.__botaoVermelho.setDown(False))
        self.__botaoVermelho.setCheckable(True)
        self.__botaoVermelho.setChecked(True)

    def __efeitoErro(self):
        self.__som.tocaSomErro()

        self.__botaoAmarelo.setDown(True)
        QtCore.QTimer.singleShot(2800, lambda: self.__botaoAmarelo.setDown(False))
        self.__botaoAmarelo.setCheckable(True)
        self.__botaoAmarelo.setChecked(True)

        self.__botaoAzul.setDown(True)
        QtCore.QTimer.singleShot(2800, lambda: self.__botaoAzul.setDown(False))
        self.__botaoAzul.setCheckable(True)
        self.__botaoAzul.setChecked(True)

        self.__botaoVerde.setDown(True)
        QtCore.QTimer.singleShot(2800, lambda: self.__botaoVerde.setDown(False))
        self.__botaoVerde.setCheckable(True)
        self.__botaoVerde.setChecked(True)

        self.__botaoVermelho.setDown(True)
        QtCore.QTimer.singleShot(2800, lambda: self.__botaoVermelho.setDown(False))
        self.__botaoVermelho.setCheckable(True)
        self.__botaoVermelho.setChecked(True)

        self.__pausa(2800)

    def __funcoesBotoes(self):
        self.__botaoOnOff.clicked.connect(self.__mediador.ligarDesligar)
        self.__botaoAmarelo.clicked.connect(self.__pressionarAmarelo)
        self.__botaoAzul.clicked.connect(self.__pressionarAzul)
        self.__botaoVerde.clicked.connect(self.__pressionarVerde)
        self.__botaoVermelho.clicked.connect(self.__pressionarVermelho)
        self.__botaoSom.clicked.connect(self.__pressionarSom)
        self.__botaoConf.clicked.connect(self.__pressionarConf)
        self.__botaoOK.clicked.connect(self.__pressionarOK)
        self.__botaoTop.clicked.connect(self.__pressionarTop)

    def __pressionarAmarelo(self):
        self.__ligarAmarelo()
        self.__mediador.botaoPressionado("amarelo")

    def __pressionarAzul(self):
        self.__ligarAzul()
        self.__mediador.botaoPressionado("azul")

    def __pressionarVerde(self):
        self.__ligarVerde()
        self.__mediador.botaoPressionado("verde")

    def __pressionarVermelho(self):
        self.__ligarVermelho()
        self.__mediador.botaoPressionado("vermelho")

    def __pressionarSom(self):
        self.__mediador.funcaoMudo()

    def __pressionarConf(self):
        if self.__som.tipo == self.__som.maxTipo:
            self.__som.tipo = 1
        else:
            self.__som.tipo += 1

        self.__botaoConf.setStyleSheet("#botaoConf{border-image: url(\"src/images/number_" + str(self.__som.tipo) + ".png\")}")

    def __pressionarTop(self):
        if self.__janelaTop10.isVisible() == True:
            self.__janelaTop10.close()
        else:
            self.__configuraJanelaTop10()
            self.__janelaTop10.show()

    def __pressionarOK(self):
        if self.__inserirNome.text() == "":
            self.__textoNome.setStyleSheet("background-color:transparent; color:red; font:15px")
            self.__textoNome.showMessage('Nome Inválido!!!')
        else:
            pontuacao = int(self.__mediador.getPontuacao)
            nomeJogador = str(self.__inserirNome.text())
            self.__ranking.addTop10(nomeJogador, pontuacao)
            self.__botaoOK.close()
            self.__inserirNome.close()
            self.__inserirNome.clear()
            self.__ranking = ControleTop()
            self.__textoNome.clearMessage()
            self.__textoNome.setStyleSheet("background-color:transparent; color:green; font:15px")
            self.__configuraJanelaTop10()


    @staticmethod
    def __pausa(ms=1000):
        QtTest.QTest.qWait(ms)


    def __desligarJogo(self):
        self.__botaoOnOff.setStyleSheet("#botaoOnOff{\n"
                                      "background-color:transparent;\n"
                                      "border-image: url(\"src/images/bt_off.png\");\n"
                                      "}\n"
                                      "")

        self.__desabilitarBotoes()

    def __desabilitarBotoes(self):
        self.__botaoAmarelo.setEnabled(False)
        self.__botaoAzul.setEnabled(False)
        self.__botaoVerde.setEnabled(False)
        self.__botaoVermelho.setEnabled(False)

    def __habilitarBotoes(self):
        self.__botaoAmarelo.setEnabled(True)
        self.__botaoAzul.setEnabled(True)
        self.__botaoVerde.setEnabled(True)
        self.__botaoVermelho.setEnabled(True)

    def __ligarVermelho(self):
        self.__som.tocaSomVermelho()
        self.__botaoVermelho.setDown(True)
        QtCore.QTimer.singleShot(400, lambda: self.__botaoVermelho.setDown(False))
        self.__botaoVermelho.setCheckable(True)
        self.__botaoVermelho.setChecked(True)
        self.__pausa(400)

    def __ligarAmarelo(self):
        self.__som.tocaSomAmarelo()
        self.__botaoAmarelo.setDown(True)
        QtCore.QTimer.singleShot(400, lambda: self.__botaoAmarelo.setDown(False))
        self.__botaoAmarelo.setCheckable(True)
        self.__botaoAmarelo.setChecked(True)
        self.__pausa(400)

    def __ligarVerde(self):
        self.__som.tocaSomVerde()
        self.__botaoVerde.setDown(True)
        QtCore.QTimer.singleShot(400, lambda: self.__botaoVerde.setDown(False))
        self.__botaoVerde.setCheckable(True)
        self.__botaoVerde.setChecked(True)
        self.__pausa(400)

    def __ligarAzul(self):
        self.__som.tocaSomAzul()
        self.__botaoAzul.setDown(True)
        QtCore.QTimer.singleShot(400, lambda: self.__botaoAzul.setDown(False))
        self.__botaoAzul.setCheckable(True)
        self.__botaoAzul.setChecked(True)
        self.__pausa(400)



    def iniciarJogo(self):
        self.__botaoOnOff.setStyleSheet("#botaoOnOff{\n"
                                      "background-color:transparent;\n"
                                      "border-image: url(\"src/images/bt_on.png\");\n"
                                      "}\n"
                                      "")
        self.__pausa(500)
        self.__habilitarBotoes()

    def tocaSequencia(self, sequencia):
        for cor in sequencia:
            if cor == "amarelo":
                self.__desabilitarBotoes()
                self.__ligarAmarelo()
                self.__pausa(300)
                self.__habilitarBotoes()

            elif cor == "azul":
                self.__desabilitarBotoes()
                self.__ligarAzul()
                self.__pausa(300)
                self.__habilitarBotoes()

            elif cor == "verde":
                self.__desabilitarBotoes()
                self.__ligarVerde()
                self.__pausa(300)
                self.__habilitarBotoes()

            elif cor == "vermelho":
                self.__desabilitarBotoes()
                self.__ligarVermelho()
                self.__pausa(300)
                self.__habilitarBotoes()

    def jogadaErrada(self):
        self.__desligarJogo()
        self.__efeitoErro()

    def atualizarPontuacao(self, pontuacao):
        self.__display.display(pontuacao)
        self.__pausa()

    def ativarMudo(self):
        self.__som.volume = 0
        self.__botaoSom.setStyleSheet("#botaoSom{\n"
                                      "background-color:transparent;\n"
                                      "border-image: url(\"src/images/sound_off.png\");\n"
                                      "}\n"
                                      "")

    def desativarMudo(self):
        self.__som.volume = 1
        self.__som.tipo = 4
        self.__botaoSom.setStyleSheet("#botaoSom{\n"
                                      "background-color:transparent;\n"
                                      "border-image: url(\"src/images/sound_on.png\");\n"
                                      "}\n"
                                      "")

    def solicitarNome(self):
        pontuacao = self.__mediador.getPontuacao
        if self.__ranking.estaNoTop10(pontuacao) == True:
            self.__inserirNome.show()
            self.__botaoOK.show()
            self.__textoNome.showMessage('Insira seu nome')