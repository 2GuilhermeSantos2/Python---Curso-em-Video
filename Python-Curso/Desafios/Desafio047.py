"""


Desafio 047

Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 0 e 50.


"""

from time import sleep

inciar = str(input('Digite OK, para iniciar: ')).upper()

print('='*50 + 'Números pares' + '='*50)
print('Iniciando Contagem....')
sleep(1)

if inciar == 'OK':
    print('Mostrando números pares entre 0 e 50: ')
    for c in range(0, 52, 2):
        print(c, end= ' ')
    print('FIM!!!')
elif inciar != 'OK':
    print('Contagem não iniciada digite "OK" para iniciar a contagem')
