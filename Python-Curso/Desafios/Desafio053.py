"""


Desafio 053

Crie um programa que leia uma frase qualque e diga se ela é um palindromo, desconsiderando os espaços


"""
from time import sleep

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
print('='*50 + 'Palindromo' + '=' * 50)
print('Analisando Frase...' )
sleep(1)

for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('Temos um palíndromo')
else:
    print('A frase digitada não é um palíndromo')