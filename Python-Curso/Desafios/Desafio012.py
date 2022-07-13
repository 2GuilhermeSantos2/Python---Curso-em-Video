"""


Desafio 012

Faça um algoritimo que leia o preço de produto e mostre seu novo preço, com 5% de desconto.


"""

print('='*50 + 'Loja dos Descontos' + '='*50)
print('='*50 + 'O GERENTE FICOU MALUCO 35%OFF' + '='*50)

v = float(input('Insira o valor do produto para ver seu preço com desconto: R$'))
d = v - (v * 0.35)
print('O preço do produto era R${:.2f}, e com desconto ficou R${:.2f}. Parabéns, obrigado, volte sempre'.format(v, d))

