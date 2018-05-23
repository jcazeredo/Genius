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

    def definirInterface(self, interface):
        self.interface = interface

    def definirControle(self, controle):
        self.controle = controle
