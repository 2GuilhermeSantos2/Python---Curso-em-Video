import random

"""


Desafio 19

O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. 
Faça um programa que leia o nome dos quatros alunos e mostre a ordem sorteda.


"""
n1 = str(input('Digite o nome do 1ºaluno: '))
n2 = str(input('Digite o nome do 2ºaluno: '))
n3 = str(input('Digite o nome do 3ºaluno: '))
n4 = str(input('Digite o nome do 4ºaluno: '))
lista = [n1,n2,n3,n4]
ordem = random.sample(lista, k=len(lista))
print('A ordem de apresentação de trabalhos será {}'.format(ordem))

