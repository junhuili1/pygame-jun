import pygame

pygame.init()
pygame.mixer.music.set_volume(1.0)
pygame.mixer.music.load('beep.mp3')
pygame.mixer.music.play(1)