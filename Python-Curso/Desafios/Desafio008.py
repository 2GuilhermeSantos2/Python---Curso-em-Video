"""


Desafio 08

Escreva um programa que leia um valor em metros e o exiba convertido em centímeros e milimetro.


"""
print('='*50 + 'Conversor de m para cm e mm' + '='*50)
n = float(input('Digite um valor: '))
c = n * 100
m = n * 1000

print('O valor digitado foi {}, \n Seu valor em centimetros é {:.2f} \n Seu valor em milimetros é {:.2f}'.format(n,c,m))
