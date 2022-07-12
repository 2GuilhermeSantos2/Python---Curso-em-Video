"""


Desafio 35

Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.


"""
from time import sleep

r1 = float(input('1ºSegmento: '))
r2 = float(input('2ºSegmento: '))
r3 = float(input('3ºSegmento: '))

print('='*50 + 'Analisador de Triângulos' + '='*50)
print('Analisando os segmentos....')
time.sleep(1)

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR TRIÂNGULOS')
else:
    print('Os segmentos acima NÃO PODEM FORMAR TRIÂNGULOS')
