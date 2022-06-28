from math import acos, asin, atan, cos, hypot, sin, tan, radians

"""


Desafio 18

Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.


"""

n = int(input('Digite o ângulo que deseja objetor o seno, cosseno e tangente: '))

seno = sin(radians(n))
cosseno = cos(radians(n))
tangente = tan(radians(n))

print('='*50 + 'Calculando ângulo' + '='*50)

print('O ângulo que escolheu foi {}. \n Seu seno é {:.2f}ºgraus. \n Seu cosseno é {:.2f}ºgraus. \n Sua tangente é {:.2f}ºgraus'
      .format(n,seno,cosseno,tangente))