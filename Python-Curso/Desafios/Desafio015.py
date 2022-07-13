"""


Desafio 015

Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelo quais foi alugado.
Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.


"""

km = float(input('Quantos Km foram percorridos? '))
dia = int(input('Quantos dias o carro ficou alugado? '))
valor_d = dia * 60
valor_km = km * 0.15

valor_total = valor_d + valor_km

print('='*50 + 'Aluguel de Carro' + '='*50)

print('Um carro que ficou alugado por {} dias e rodou {:.2f}km. \n Ficou valor de R${:.2f} pelos Km rodados e R${:.2f} pelos dias alugados.'
      '\n Ficando em um total de R${:.2f}'.format(dia, km, valor_km, valor_d, valor_total))