"""


Desafio 006

Crie um algoritimo que leia um número e mostre seu dobro, triplo e raiz quadrada.


"""
print('='*50 + 'Dobro, Triplo e Raiz Quadrada' + '='*50)
n = int(input('Digite um número: '))

d = n * 2
t = n * 3
r = n ** (1/2)

print('O número digitado foi {}, \n Seu dobro é {} \n Seu triplo é {} \n Sua raiz quadrada é {}'.format(n, d, t, r))
