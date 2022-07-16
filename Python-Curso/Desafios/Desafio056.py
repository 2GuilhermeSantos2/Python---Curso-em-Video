"""


Desafio 056

Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
A média de idade do grupo.
Qual é o nome do homem mais velho.
Quantas muleres tem menos de 20 anos.


"""
somaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range (1, 5):
    print('====={}ª pessoa ====='.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()
    somaidade += idade
    if p == 1 and sexo == 'M':
        maioridadehomem = idade
    if sexo == 'M' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo == 'F' and idade < 20:
        totmulher20 += 1

mediaidade = somaidade / 4
print('A média de idade do grupo [e de {}'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulheres com 20 anos'.format(totmulher20))


