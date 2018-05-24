import random


class Sequencia:
    def __init__(self):
        self.coresDisponiveis = ['amarelo', 'azul', 'verde', 'vermelho']
        self.coresSequencia = []

    def geraSequencia(self):
        corAleatoria = random.choice(self.coresDisponiveis)
        self.coresSequencia.append(corAleatoria)

    @property
    def obterSequencia(self):
        return self.coresSequencia

    @property
    def obterTamanho(self):
        return len(self.coresSequencia)
