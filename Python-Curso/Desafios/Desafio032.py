"""


Desafio 032

Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.


"""
from time import sleep
from calendar import isleap
ano = int(input('Digite um ano para saber se ele é Bissexto: '))

print('='*50 + 'Verificador de ano bissexto' + '='*50)
print('Analisando o ano...')
sleep(1)

if isleap(ano):
    print('Esse ano é Bissxeto')
else:
    print('Que pena esse ano não é Bissexto')