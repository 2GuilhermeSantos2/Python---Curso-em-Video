"""


Desafio 29

Escreve um programa que leia a velocidade de um carro.

Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que foi multado.

A multa vai custar R$7,00 por cada Km acima do limite.


"""
from time import sleep

vel = int(input('Digite a velocidade do carro: '))
mul =  (vel - 80) * 7
print('='*50 + 'Leitor de velocidade' + '='*50)
print('Analisando a velocidade...')
sleep(1)

if vel <=80:
    print('Você esta a {}Km/h. Você esta no limite permitido dirija em segurança!'.format(vel))
else:
    print('Você esta a {}Km/h. Como esta acima do limite sera aplicado uma multa de R${:.2f}'.format(vel,mul))
