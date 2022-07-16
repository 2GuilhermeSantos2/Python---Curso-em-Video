"""


Desafio 052

Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.


"""
from time import sleep

n = int(input('Digite um número: '))
tot = 0

print('='*50 + 'Números Primos' + '=' * 50)
print('Analisando número...' )
sleep(1)

for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{}'.format(c), end='')
if n < 0:
    print('Você digitou um número negativo. Não existe números primos negativos. Por favor digite outro valor.')
else:
    print('\n\033[mO número {} foi divisível {} vezes'.format(n, tot))
if tot == 2:
    print('E por isso ele é PRIMO!!!')
elif n < 0:
    print('')
else:
    print('E por isso ele NÃO É PRIMO')