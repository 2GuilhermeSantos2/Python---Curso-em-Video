"""


Desafio 10

Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la.
Sabendo que cada litro de tinta, pinta um área de 2 metros quadrados.


"""
print('='*50 + 'Pinta Parede' + '='*50)
l = float(input('Digite a largura da parede: '))
a = float(input('Digite a altura da parede: '))
at = l*a
t = at/2
print('Com uma parede de {:.2f} metros de largura, e {:.2f} de altura, a area total é {:.2f} metros. Então sera necessário {:.2f} litros de tinta.'
      ' '.format(l, a, at, t))
