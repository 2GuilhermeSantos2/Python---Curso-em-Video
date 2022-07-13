"""


Desafio 038

Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:

O primeiro valor é maior.
O segundo valor é maior.
Não existe valor maior, os dois são iguais.


"""
from time import sleep

n1 = int(input('Digite o 1ºvalor: '))
n2 = int(input('Digite o 2ºvalor: '))

print('='*50 + 'Comparando números' + '='*50)
print('Comparando números....')
sleep(1)

if n1 > n2:
    print('O maior valor é {} \n E o menor valor é {}'.format(n1,n2))
elif n1 < n2:
    print('O maior valor é {} \n E o menor valor é {}'.format(n2,n1))
elif n1 == n2:
    print('Ambos os valores são iguais')

