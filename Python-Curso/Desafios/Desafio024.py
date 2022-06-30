"""


Desafio 24

Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".


"""


print('='*50 + 'Analisador de nome da cidade' + '='*50)


n = str(input('Digite o nome da cidade: ')).strip().capitalize()
nc = n[:5] == 'Santo'
print('O nome da sua cidade possui Santo? {}'.format(nc))