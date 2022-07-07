"""


Desafio 34

Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.

Para salários superiores a R$1.250,00, calcule um aumento de 10%.

Para os inferiores ou iguais, o aumento é de 15%.


"""
from time import sleep

pn = float(input('Qual seu salário? '))
ps = pn + (pn * 0.10)
pi = pn + (pn * 0.15)

print('='*50 + 'Verificador de Aumento' + '='*50)
print('Analisando o salário...')
sleep(1)

if pn <= 1250:
    print('Seu novo salário é de R${:.2f}'.format(pi))
else:
    print('Seu novo salário é de R${:.2f}'.format(ps))