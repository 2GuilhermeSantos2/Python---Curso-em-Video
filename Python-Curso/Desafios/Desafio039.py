"""


Desafio 039

Faça um programa que leio ano de nascimento de um jovem e informe, de acordo com a sua idade:

Se ele ainda vai se alistar ao serviço militar.
Se é a hora de se alistar.
Se já ássou do tempo de alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.


"""
from datetime import date

nome = str(input('Digite seu nome: ')).capitalize()
ano = int(input('Digite o ano que você nasceu: '))
ano_atual = date.today().year
idade = atual - nascimento
if idade == 18:
    print('Você tem que se alistar imediamente {}'.format(nome))
elif idade < 18:
    saldo = 18 - idade
    ano = ano_atual + saldo
    print('Você ainda não tem 18 anos {}, ainda faltam {} anos para o alistamento'.format(nome, saldo))
    print('Seu alistamento sera em {}')
elif idade > 18:
    saldo = idade - 18
    ano = ano_atual - saldo
    print('Você, já deveria ter se alistatado {}, há {} anos'.format(nome,saldo))
    print('Seu alistamento foi em {} ')

