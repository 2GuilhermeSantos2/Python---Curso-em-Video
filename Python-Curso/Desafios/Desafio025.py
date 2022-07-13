"""


Desafio 025

Crie um programa que leia o nome de uma pessoa e diga se ele tem "SILVA" no nome.


"""
print('='*50 + 'Analisador nome' + '='*50)


n = str(input('Digite seu nome: ')).strip().capitalize()
ns = 'Silva' in n
print('Seu nome tem Silva? {}'.format(ns))