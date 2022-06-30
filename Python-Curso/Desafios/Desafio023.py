"""


Desafio 23

Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.

Exemplo:

Digite o número: 1834

unidade:4

dezena:3

centena:8

unidade: 1


"""
print('='*50 + 'Analisandor de números' + '='*50)

n = int(input('Digite um números: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10

print('Analisando o número...')
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))