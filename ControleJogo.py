from Mediado import Mediado
from Sequencia import Sequencia


class ControleJogo(Mediado):
    def __init__(self, mediador):
        super().__init__(mediador)
        self.coresSequencia = None
        self.jogoIniciado = False

    def iniciarJogo(self):
        self.coresSequencia = Sequencia()
        self.jogoIniciado = True

    def novaSequencia(self):
        self.coresSequencia.geraSequencia
        return self.coresSequencia.obterSequecia

    def botaoPressionado(self, cor_botao):
        pass

    def botaoCorreto(self):
        pass

    def botaoErrado(self):
        pass

    @property
    def estaLigado(self):
        return self.jogoIniciado

    def desligarJogo(self):
        self.jogoIniciado = False
