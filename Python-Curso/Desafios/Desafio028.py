"""


Desafio 028

Escreve um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o
usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.


"""
import random
import time
from time import sleep

ale = random.randint(0, 5)
print('Estou pensando em um número....')
time.sleep(1)
jogador = int(input('Digite um número de 0 a 5 e eu vou tentar acertar: '))
computador = ale

print('='*50 + 'Números aleatórios' + '='*50)
print('Analisando o número....')
time.sleep(1)

if jogador > 5 or jogador < 0:
    print('ERROR! Digite números entre 0 e 5')

elif jogador == computador:
    print('Você ganhou eu também pensei no número {}'.format(ale))
else:
    print('Que pena você perdeu! Eu pensei no número {}'.format(ale))

