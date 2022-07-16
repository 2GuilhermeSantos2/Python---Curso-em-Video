"""


Desafio 049

Refaça o Desafio 009, mostrando a tabuada de número que o usuário escolher, só que agor utilizando laço for.


"""
from time import sleep

print('='*50 + 'Tabuada' + '='*50)

n = int(input('Digite um número para ver sua tabuada: '))
mul = 0
resul = 0

print('='*50 + 'Processando Tabuada' + '='*50)
sleep(1)

for c in range(1, 11):
    mul += 1
    resul = n * mul
    print('{} X {} = {}'.format(n, mul, resul))
