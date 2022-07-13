"""


Desafio 027

Faça um programa que leia o nome completo de uma pessoa, mostrado em seguida o primeiro e o último nome separadamente.

Ex: Ana Maria de Souza

Primeiro = Ana

Último = Souza


"""
print('='*50 + 'Analisandor de nomes' + '='*50)


n = str(input('Digite seu nome: ')).strip()
nome = n.split()
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome) - 1]))