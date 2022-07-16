"""


Desafio 051

Desenvolva um programa que leia o primeiro termo e a razão de um PA. No final, mostre os 10 primeiros termos dessa progressão.


"""
from time import sleep
print('='*50 + '=' * 50)
print('='*50 + '10 TERMOS DE UMA PA' + '=' * 31)
print('='*50 + '=' * 50)

p1 = int(input('Digte o primeiro termo: '))
r = int(input('Digite a razão: '))
d = p1 + (10 - 1) * r

print('='*50 + ' 10 Termos de uma PA' + '=' * 50)
print('='*50 + 'Processando dados' + '='*50)
sleep(1)

print('Primeiro Termo: {}'.format(p1))
print('Razão: {}'.format(r))

for c in range(p1,d,r):
    print('{}'.format(c), end=' -> ')
print('FIM!!!')

