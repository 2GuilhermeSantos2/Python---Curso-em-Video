"""


Desafio 10

Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.


"""
print('='*50 + 'Convertor de Real para Dólar'
               '' + '='*50)
c = float(input("Digite o valor que deseja, converter: R$"))
d = c / 5.19
print('Você possui R${:.2f}, que vale US${:.2f}'.format(c,d))
