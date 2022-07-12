"""


Desafio 33

Faça um programa que leia três números e mostre qual é o maior e qual é o menor.


"""

n1 = int(input('Digite o 1º valor: '))
n2 = int(input('Digite o 2º valor: '))
n3 = int(input('Digite o 3º valor: '))
menor = n1
maior = n1

if n2 < n1 and n2 < n3:
    menor = n2
elif n3 < n1 and n3 < n2:
    menor = n3
elif n2 > n1 and n2 > n3:
    maior = n2
elif n3 > n1 and n3 > n2:
    maior = n3

print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))
