"""


Desafio 14

Faça um programa que converta uma temperatura digitada em ºC em ºF


"""

temc = float(input('Digite a temperatura em ºC para converter para ºF: '))
temf = (temc * 1.8) + 32

print('='*50 + 'Convertor de temperatura' + '='*50)
print('{:.1f}ºC, é igua a {:.1f}ºF'.format(temc, temf))
