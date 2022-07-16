"""


Desafio 055

Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor pesos lidos.


"""
from time import sleep
maior = 0
menor = 0

for p in range(1,6):
    peso = float(input('Peso da {}ª pessoa').format(p))
    if p == 1:
        maior = p
        menor = p
    else:
        if p > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('Analisando dados...' )
print('='*50 + 'Analisando peso' + '=' * 50)
sleep(1)
print('O maior peso lido foi de {}Kg. \n'
      'O menor peso lido foi {}'.format(maior,menor))