from math import acos, asin, atan, cos, hypot, sin, tan, radians

"""


Desafio 017

Faça um programa que leia o comprimento do cateto oposta e cateto adjacente de um triângulo retângulo,
calcule e mostre o comprimento da hipotenusa.


"""
print('='*50 + 'Calculando hipotenusa' + '='*50)

co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
hip = hypot(co,ca)
print('O comprimento da hipotenusa é {:.2f}'.format(hip))