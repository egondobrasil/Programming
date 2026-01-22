#import pygame: é apenas compatível com a versão 3.11 do Python
from playsound3 import playsound

#modo simples
playsound('https://professorcelso.com.br/guns.mp3')

#modo assincrono

sound = playsound('https://professorcelso.com.br/guns.mp3', block=False)
if sound.is_alive():
    print('Tocando...')
sound.stop()