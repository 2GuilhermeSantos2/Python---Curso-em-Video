"""


Desafio 05

Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e antecessor.


"""
print('='*50 + 'Sucessor e Antecessor' + '='*50)
n = int(input('Digite um número para ver seu sucessor e antecessor: '))

a = n - 1
s = n + 1

print('O número digitado foi {}, seu antecessor é {} e sucessor é {}'.format(n, a, s))
