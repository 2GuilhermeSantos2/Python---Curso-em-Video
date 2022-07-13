"""


Desafio 022

Crie um programa que leia o nome completo de pessoa e mostre:

O nome com todas as letras maiúsculas

O nome com todas as letras minúsculas

Quantas letras ao todo (sem considerar espaços)

Quantas letras tem o primeiro


"""

n = str(input('Digite seu nome: ')).strip()

print('='*50 + 'Analisandor nome' + '='*50)


print('Seu nome em maiúsculo fica {}'.format(n.upper()))
print('Seu nome em minúsculo fica {}'.format(n.lower()))
print('Seu nome tem ao todo {} letras'.format(len(n)-n.count(' ')))
print('Seu primeiro nome tem {} letras'.format(n.find(' ')))

