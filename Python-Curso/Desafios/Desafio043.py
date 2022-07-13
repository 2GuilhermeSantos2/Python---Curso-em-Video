"""


Desafio 043

Desenvolva uma lógica que leia o peso e a altura de uma pessa, calcule seu IMC e mostre seu status , de acordo com a tabela abaixo:

Abaixo de 18.5: Abaixo do peso
Entre 18.5 e 25: Peso ideal
25 até 30: Sobrepeso
30 até 40: Obesidade
Acima de 40: Obesidade Mórbidada


"""
from time import sleep

altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))
imc = peso/(altura*altura)
print('='*50 + 'IMC' + '='*50)
print('Calculando o IMC....')
sleep(1)

if imc < 18.5:
    print('Você esta abaixo do peso')
elif imc > 18.5 and imc < 25:
    print('Você esta no peso ideal')
elif imc >= 25 and imc < 30:
    print('Você esta com sobrepeso')
elif imc >= 30 and imc < 40:
    print('Você esta com obesidade')
elif imc > 40:
    print('Você esta com obesidade mórbidade')
