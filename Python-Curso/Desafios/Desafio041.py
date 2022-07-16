"""


Desafio 041

A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

Até 9 anos: Mirim
Até 14 anos: Infantil
Até 19 anos: Junior
Até 20 anos: Sênior
Acima: Master


"""
from datetime import date
from time import sleep
ano_atual = date.today().year
nascimento = int(input('Digite o a seu ano de nascimento: '))
idade = ano_atual - nascimento
print('='*50 + 'Confederação Nascional de Natação' + '='*50)
print('Conferindo seus dados....')
sleep(1)

if idade <= 9:
    print('Classificação: MIRIM')
elif idade > 9 and idade <= 14:
    print('Classificação: INFANTIL')
elif idade > 14 and idade <= 19:
    print(Classificação: 'Classificação: JUNIOR')
elif idade > 19 and idade <= 20:
    print('Classificação: Sênior')
elif idade > 20:
    print('Classificação: Master')

