"""


Desafio 042

Refaça o desafio 025 dos triângulos acrescentando o recurso de mostrar que tipo de triângulo sera formado:

Equiátero: todos os lados iguais
Isosceles: dois lados iguais
Escalenos: Todos os lados diferentes


"""
from time import sleep

r1 = float(input('1ºSegmento: '))
r2 = float(input('2ºSegmento: '))
r3 = float(input('3ºSegmento: '))

print('='*50 + 'Analisador de Triângulos' + '='*50)
print('Analisando os segmentos....')
time.sleep(1)

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR TRIÂNGULOS',  end=' ')
    if r1 == r2 and r2 == r3:
        print('EQUILÁTERO')
    elif r1 != r2 and r2 != r3 and r3 != r1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Os segmentos acima NÃO PODEM FORMAR TRIÂNGULOS')

