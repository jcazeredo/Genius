class Mediador:
    def __init__(self):
        self.interface = None
        self.controle = None

    def ligarDesligar(self):
        if self.controle.estaLigado:
            self.interface.desligarJogo()
            self.controle.desligarJogo()
        else:
            self.interface.iniciarJogo()
            self.controle.iniciarJogo()

            sequencia = self.controle.novaSequencia()
            self.interface.novaSequencia(sequencia)

    def botaoPressionado(self, cor):
        jogadaCorreta = self.controle.checaJogada(cor)
        if jogadaCorreta:
            jogadasRestantes = self.controle.obterJogadasRestantes

            if jogadasRestantes == 0:
                self.controle.atualizarPontuacao()
                pontuacao = self.controle.obterPontuacao
                self.interface.atualizarPontuacao(pontuacao)
                self.controle.zeraJogadas()
                sequencia = self.controle.novaSequencia()
                self.interface.novaSequencia(sequencia)
        else:
            self.controle.desligarJogo()
            self.interface.jogadaErrada()
            self.interface.desligarJogo()
            self.interface.atualizarPontuacao(0)

    def definirInterface(self, interface):
        self.interface = interface

    def definirControle(self, controle):
        self.controle = controle
