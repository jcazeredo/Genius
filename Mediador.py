class Mediador:
    def __init__(self):
        self.interface = None
        self.controle = None
        self.__pontuacao = 0

    def ligarDesligar(self):
        jogoIniciado = self.controle.estaLigado
        if jogoIniciado:
            self.interface.desligarJogo()
            self.interface.atualizarPontuacao(0)
            self.controle.desligarJogo()
        else:
            self.interface.iniciarJogo()
            self.controle.iniciarJogo()
            sequencia = self.controle.novaSequencia()
            self.interface.tocaSequencia(sequencia)

    def botaoPressionado(self, cor):
        jogoIniciado = self.controle.estaLigado

        if jogoIniciado:

            jogadaCorreta = self.controle.checaJogada(cor)
            if jogadaCorreta:
                jogadasRestantes = self.controle.obterJogadasRestantes

                if jogadasRestantes == 0:
                    self.controle.atualizarPontuacao()
                    pontuacao = self.controle.obterPontuacao
                    self.interface.atualizarPontuacao(pontuacao)
                    self.controle.zeraJogadas()
                    sequencia = self.controle.novaSequencia()
                    self.interface.tocaSequencia(sequencia)
            else:
                self.__pontuacao = self.controle.obterPontuacao
                self.controle.desligarJogo()
                self.interface.jogadaErrada()
                self.interface.atualizarPontuacao(0)
                self.interface.solicitarNome()


    def funcaoMudo(self):
        estaMudo = self.controle.estaMudo

        if estaMudo == True:
            self.interface.desativarMudo()
            self.controle.estaMudo = False
        else:
            self.interface.ativarMudo()
            self.controle.estaMudo = True

    def definirInterface(self, interface):
        self.interface = interface

    def definirControle(self, controle):
        self.controle = controle

    @property
    def getPontuacao(self):
        return self.__pontuacao
