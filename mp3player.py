#import pygame: é apenas compatível com a versão 3.11 do Python
from playsound3 import playsound

#modo simples
playsound('guns.mp3')

#modo assincrono

sound = playsound('guns.mp3', block=False)
if sound.is_alive():
    print('Tocando...')
sound.stop()