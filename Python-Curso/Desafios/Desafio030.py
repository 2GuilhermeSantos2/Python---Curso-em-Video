"""


Desafio 30

Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.


"""
from time import sleep
n = int(input('Digite um número: '))

print('='*50 + 'PAR OU IMPAR' + '='*50)
print('Analisando o número...')
sleep(1)
if (n % 2) == 0:
    print('O número digitado é par')
else:
    print('O número digitado é impar')
