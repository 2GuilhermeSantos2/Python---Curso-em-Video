"""


Desafio 036

Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.


"""
from time import sleep


valor_casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite seu salário: '))
anos = int(input('Digite em quantos anos ira pagar: '))
prestação = valor_casa / (anos * 12)
minimo = salario * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(valor_casa, anos), end='')
print(', a prestação será de R${:.2f}'.format(prestação))
if prestação <= minimo:
    print('Empréstimo CONCEDIDO')
else:
    print('Empréstimo NEGADO!')
