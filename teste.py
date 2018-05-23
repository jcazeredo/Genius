import pygame
pygame.mixer.init()
pygame.mixer.music.load('genius/sounds/amarelo.ogg')
pygame.mixer.music.play(0)
while pygame.mixer.music.get_busy():
	pygame.time.Clock().tick(10)
