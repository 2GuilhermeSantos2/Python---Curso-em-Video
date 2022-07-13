"""


Desafio 004


Faça um programa que leia algo pelo teclado e mostre na tela seu tipo primitivo e todas informações possíveis sobre ele


"""

a = input('Digite algo:')

print('Só tem espaços?, 'a.isspace())
print('É um número? ', a.isnumeric())
print('É alfabético? ', a.isalpha())
print('É alpfanumérico? ', a.isalnum())
print('Esta em maiúsculas?', a.isupper())
print('Esta em minúscula?', a.islower())
print('Esta capitalizada?' a.istitle())
