"""


Desafio 045

Crie um programa que faça o computador jogar Jokenpô com você.


"""
from time import sleep
from random import randint
computador = randint(0,2)
jogador = int(input('Escolha \n'
                    '[0] Pedra \n'
                    '[1] Papel \n'
                    '[2] Tesoura \n'))
itens = ('Pedra', 'Papel', 'Tesoura')
print('='*50 + 'JOKENPO' + '='*50)
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')

if jogador == 0: #Jogador joga  PEDRA
    if computador == 0: #Computador joga PEDRA
        print('EMPATE')
    elif computador == 1: #Computador joga PAPEL
        print('Eu ganhei, eu joguei {} e você jogou {}'.format(itens[computador], itens[jogador]))
    elif computador == 2: #Computador joga TESOURA
        print('Você ganhou, eu joguei {} e você jogou {}'.format(itens[computador],itens[jogador]))
elif jogador == 1: #Jogador joga PAPEL
    if computador == 0: #Computador joga PEDRA
        print('Você ganhou eu joguei {} e você jogou {}'.format(itens[computador],itens[jogador]))
    elif computador == 1: #Computador joga PAPEL
        print('EMPATE')
    elif computador == 2: #Computador joga TESOURA
        print('Eu ganhei, eu jogue {} e você jogou {}'.format(itens[computador], itens[jogador]))
elif jogador == 2: #Jogador jogou TESOURA
    if computador == 0: #Computador jogou PEDRA
        print('Eu ganhei, eu jogue {} e você jogou {}'.format(itens[computador], itens[jogador]))
    elif computador == 1: #Computador jogou PAPEL
        print('Você ganhou eu joguei {} e você jogou {}'.format(itens[computador], itens[jogador]))
    elif computador == 2: #Computador jogou Tesoura
        print('EMPATE')
elif jogador != 1 or jogador != 2 or jogador != 3:
    print('ERROR!!! Jogada inválida')


