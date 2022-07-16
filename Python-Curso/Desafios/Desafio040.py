"""


Desafio 040

Crie um programa que leia as notas dos 4 bimestre de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

Média abaixo de 5
Reprovado

Media entre 5 e 6.9
Recuperação

Média 7 ou superior
Aprovado


"""
from time import sleep

b1 = float(input('Digite a nota do 1ºBimestre: '))
b2 = float(input('Digite a nota do 2ºBimestre: '))
b3 = float(input('Digite a nota do 3ºBimestre: '))
b4 = float(input('Digite a nota do 4ºBimestre: '))
media = (b1 + b2 + b3 + b4) / 4

if media < 5:
    print('Sua média foi {:.1f}, portanto foi REPROVADO!'.format(media))
elif  7 > media >= 5:
    print('Sua média foi {:.1f}, portanto esta de RECUPERAÇÃO!'.format(media))
elif media >=7:
    print('PARABÉNS sua média foi {:.1f}, portanto foi APROVADO'.format(media))
