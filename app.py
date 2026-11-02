import pygame
from PIL import Image

playlist = [
    {
        "name": "Annoying Alarm",
        "file": 'CLOCK.ogg',
        "image": 'alarm.png'
    },
    {"name": "Annoying Slurp", "file": 'hottea.ogg', "image": 'slurp.png'},
    {
        "name": "Metal Squeak",
        "file": 'metalsqueak.mp3',
        "image": 'squeak.png'
    },
    {
        "name": "Aura Farmer",
        "file": 'Aura Farmer.mp3',
        "image": 'Aura Farmer.png'
    }
]

for i in range(len(playlist)):
    print(playlist[i]["name"])

pygame.init()
pygame.mixer.music.set_volume(1.0)
choice = input("What song do you want to start with?")

found = False

for i in range(len(playlist)):
    if choice in playlist[i]["name"]:
        pygame.mixer.music.load(playlist[i]["file"])
        pygame.mixer.music.play(1)
        im = Image.open(playlist[i]["image"])
        im.show()
        found = True
        song = i
if found == False:
    print(f"No song was found with the name: {choice}")

while True:
    action = input("[p] for pause, [r] to resume, [s] for skip (must do when song is done), anything else to stop.")
    if action == "p":
        pygame.mixer.music.pause()
    elif action == "r":
        pygame.mixer.music.unpause()
    elif action == "s":
        song += 1
        if song >= len(playlist):
            song = 0
        pygame.mixer.music.load(playlist[song]["file"])
        pygame.mixer.music.play(1)
        im = Image.open(playlist[song]["image"])
        im.show()
    else:
        pygame.mixer.music.stop()
        break
    