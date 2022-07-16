"""


Desafio 046

Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio, indo 10 até 0, com uma pausa de 1 segundo entre.


"""
import emoji
from time import sleep

inciar = str(input('Digite OK, para iniciar a sequencia de fogos: ')).upper()
inicio = 10
fim = 0

print('='*50 + 'Fogos de Artificio' + '='*50)
print('Iniciando Contagem....')
sleep(1)

if  inciar == "OK":
    for c in range(inicio, fim, -1):
        print(c)
        sleep(1)
    print(emoji.demojize('FELIZ ANO NOVO'))
elif inciar != "OK":
    print('Contagem não iniciada digite "OK" para iniciar a contagem')


