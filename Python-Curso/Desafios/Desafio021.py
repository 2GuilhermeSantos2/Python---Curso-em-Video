import pygame
import playsound
import vlc

"""


Desafio 21

Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.


"""
print('='*50 + 'Tocador MP3' + '='*50)


pygame.init()
pygame.mixer.music.load('impossible.mp3')
pygame.mixer.music.play()
pygame.event.wait()
input()