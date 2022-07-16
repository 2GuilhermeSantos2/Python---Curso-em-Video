"""


Desafio 048

Faça que calcule a soma entre os o números ímpares que são multiplos de três e que se encontram no intervalo de 1 até 500.


"""
from time import sleep

inciar = str(input('Digite OK, para iniciar: ')).upper()
cont = 0
soma = 0

print('='*50 + 'Números impares' + '='*50)
print('Iniciando Contagem....')
sleep(1)

if inciar == "OK":
    for c in range(1, 501, 2):
        if c % 3 == 0:
            cont += 1
            soma += c
    print('O total de valores solicitado foi {}. \n'
          'E a soma deles foi {}'.format(cont, soma))
elif inciar != "OK":
    print('Contagem não iniciada digite "OK" para iniciar a contagem')

