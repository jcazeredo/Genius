import random


class Sequencia:
    def __init__(self):
        self.coresDisponiveis = ['amarelo', 'azul', 'verde', 'vermelho']
        self.coresSequencia = []
        self.geraSequencia()

    def geraSequencia(self):
        corAleatoria = random.choice(self.coresDisponiveis)
        self.coresSequencia.append(corAleatoria)

    @property
    def obterSequecia(self):
        return self.coresSequencia
