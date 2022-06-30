import random

"""


Desafio 19

Um professor quer sortear um dos seus quatros alunos para apagar o quadro. 
Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.


"""
print('='*50 + 'Sorteando Aluno' + '='*50)

n1 = str(input('Digite o nome do 1ºaluno: '))
n2 = str(input('Digite o nome do 2ºaluno: '))
n3 = str(input('Digite o nome do 3ºaluno: '))
n4 = str(input('Digite o nome do 4ºaluno: '))
lista = [n1,n2,n3,n4]
escolhido = random.choice(lista)

print('O aluno escolhido para apagar o quadro foi {}'.format(escolhido))