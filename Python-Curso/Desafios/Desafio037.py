"""

Desafio 037



Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão



1 para binário

2 para Octal

3 poara Hexadecimal



"""
from time import sleep
print('='*50)
escolha = int(input('Escolha uma opção para converter seu número: \n '
      '[1] Bínario \n'
      ' [2] Octal \n '
      '[3] Hexadecimal \n'
                    ''
               ''))
print('='*50),
n = int(input('Digite o número que será convertido: '))
binario = bin(n)
octal = oct(n)
hexadecimal = hex(n)
print('='*50 + 'Conversor de números' + '='*50)
print('Convertendo seu número....')
sleep(1)
if escolha == 1:
    print('Seu número em binário fica: \n {}'.format(binario)[2:])
elif escolha == 2:
    print('Seu número em octal fica: \n {}'.format(octal[2:]))
elif escolha == 3:
    print('Seu número em hexadecimal fica: \n {}'.format(hexadecimal[2:]))
elif escolha != 1 or 2 or 3:
    print('Opção inválida, digite um opção válida!')
