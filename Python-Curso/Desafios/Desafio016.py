from math import trunc

"""


Desafio 16

Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.


"""

n = float(input('Digite um número para ver sua porção inteira: '))
"""pi = trunc(n) Caso eu tivesse feito com 2 variáveis"""

print('='*50 + 'Porção Inteira' + '='*50)


print('O número digitado foi {} e sua porção inteira é {}.'.format(n, trunc(n)))