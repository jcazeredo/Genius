from Mediado import Mediado
from Sequencia import Sequencia


class ControleJogo(Mediado):
    def __init__(self, mediador):
        super().__init__(mediador)
        self.coresSequencia = None
        self.jogoIniciado = False
        self.jogada = 0
        self.pontos = 0

    def iniciarJogo(self):
        self.coresSequencia = Sequencia()
        self.jogoIniciado = True

    def novaSequencia(self):
        self.coresSequencia.geraSequencia()
        return self.coresSequencia.obterSequencia

    def checaJogada(self, cor):
        sequencia = self.coresSequencia.obterSequencia
        corCorreta = sequencia[self.jogada]

        self.jogada = self.jogada + 1
        if cor == corCorreta:
            return True

        return False

    @property
    def obterJogadasRestantes(self):
        tamanhoSequencia = self.coresSequencia.obterTamanho
        return tamanhoSequencia - self.jogada

    def atualizarPontuacao(self):
        self.pontos = self.pontos + 1

    def zeraJogadas(self):
        self.jogada = 0

    @property
    def obterPontuacao(self):
        return self.pontos

    @property
    def estaLigado(self):
        return self.jogoIniciado

    def desligarJogo(self):
        self.coresSequencia = None
        self.jogoIniciado = False
        self.jogada = 0
        self.pontos = 0
