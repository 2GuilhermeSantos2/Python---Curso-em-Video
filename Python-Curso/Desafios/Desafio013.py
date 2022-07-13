"""


Desafio 013

Faça um algoritimo que leia o salário de um funcionário e mostre seu salário com 15% de aumento.


"""

print('='*50 + 'Reajuste de salário' + '='*50)

sa = float(input('Digite seu sálario para calcular o reajuste de 15%: R$'))
sn = sa + (sa * 0.15)
print('Seu salário antigo era R${:.2f}, agora com reajuste de 15% passou para R${:.2f}'.format(sa, sn))
