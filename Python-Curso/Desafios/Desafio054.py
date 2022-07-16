"""
Desafio 054

Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já maiores.

"""
from datetime import date
from time import sleep

atual = date.today().year
totmaior = 0
totmenor = 0

ano_atual = date.today().year
for c in range(1, 8):
    nascimento = int(input('Digite o ano que a {}ªpessoa nasceu: '.format(c)))
    idade = atual - nascimento
    if idade >=18:
        totmaior += 1
    else:
        totmenor += 1
print('='*50 + 'Maior ou menor de idade' + '=' * 50)
print('Analisando nascimento...' )
sleep(1)

print('Foram dectadas {} pessoas, menores de idades. \nForam dectadas {} pessoas, maiores de idades'.format(totmenor, totmaior))





