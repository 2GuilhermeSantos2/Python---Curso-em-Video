"""


Desafio 031

Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
cobrando R$0,50 por Km para viagens de até 200km e R$0,45 para viagens mais longas.


"""
from time import sleep

dv = int(input('Qual a distância da sua viagem? '))
pn = dv * 0.50
pd = dv * 0.45

print('='*50 + 'Calculando Preço' + '='*50)
print('Calculando Preço...')
sleep(1)

if dv <= 200:
    print('O valor da sua viagem ficou no total de R${:.2f}'.format(pn))
else:
    print('Você conseguiu um desconto por sua viagem ser longa o valor dela ficou no total de R${:.2f}'.format(pd))
