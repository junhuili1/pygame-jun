import pygame

playlist = [
    {
        "name": "Annoying Alarm",
        "file": 'CLOCK.ogg'
    },
    {"name": "Annoying Slurp", "file": 'hottea.ogg'}
]

pygame.init()
pygame.mixer.music.set_volume(1.0)
pygame.mixer.music.load(playlist[0]["name"])                                                                                                                                                                      :
pygame.mixer.music.play(1)

if input("e") == "o":
    pygame.mixer.music.stop()