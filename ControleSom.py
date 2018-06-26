import pygame

class ControleSom:
    def __init__(self):
        pygame.mixer.pre_init(frequency=44100, size=-16, channels=1, buffer=512)
        pygame.mixer.init()
        self._volume = 1
        self._tipo = 1
        self._maxTipo = 6
        self._somBtVermelho = pygame.mixer.Sound("src/sounds/som_vermelho_" + str(self._tipo) + ".ogg")
        self._somBtAmarelo = pygame.mixer.Sound("src/sounds/som_amarelo_" + str(self._tipo) + ".ogg")
        self._somBtVerde = pygame.mixer.Sound("src/sounds/som_verde_" + str(self._tipo) + ".ogg")
        self._somBtAzul = pygame.mixer.Sound("src/sounds/som_azul_" + str(self._tipo) + ".ogg")
        self._somErro = pygame.mixer.Sound("src/sounds/som_erro_" + str(self._tipo) + ".ogg")
        self._somIntro = pygame.mixer.Sound("src/sounds/som_intro_" + str(self._tipo) + ".ogg")

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo
        self._somBtVermelho = pygame.mixer.Sound("src/sounds/som_vermelho_" + str(tipo) + ".ogg")
        self._somBtAmarelo = pygame.mixer.Sound("src/sounds/som_amarelo_" + str(tipo) + ".ogg")
        self._somBtVerde = pygame.mixer.Sound("src/sounds/som_verde_" + str(tipo) + ".ogg")
        self._somBtAzul = pygame.mixer.Sound("src/sounds/som_azul_" + str(tipo) + ".ogg")
        self._somErro = pygame.mixer.Sound("src/sounds/som_erro_" + str(tipo) + ".ogg")
        self._somIntro = pygame.mixer.Sound("src/sounds/som_intro_" + str(tipo) + ".ogg")

    @property
    def maxTipo(self):
        return self._maxTipo

    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, volume):
        self._volume = volume
        self._somBtVermelho.set_volume(volume)
        self._somBtAmarelo.set_volume(volume)
        self._somBtVerde.set_volume(volume)
        self._somBtAzul.set_volume(volume)
        self._somErro.set_volume(volume)
        self._somIntro.set_volume(volume)



    def tocaSomVermelho(self):
        self._somBtVermelho.play()

    def tocaSomAmarelo(self):
        self._somBtAmarelo.play()

    def tocaSomVerde(self):
        self._somBtVerde.play()

    def tocaSomAzul(self):
        self._somBtAzul.play()

    def tocaSomErro(self):
        self._somErro.play()

    def tocarSomIntro(self):
        self._somIntro.play()
