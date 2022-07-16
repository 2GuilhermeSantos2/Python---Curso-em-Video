"""


Desafio 050

Desenvolva um programa que leia seis números inteiros e mostre a soma apenas que forem pares. Se o valor ditado or impar, desconsidere-o.


"""

soma = 0
cont_p = 0
cont = 0
for c in range(1, 7):
    n = int(input('Digite um {}° número: '.format(c)))
    cont += 1
    if n % 2 == 0:
        soma += n
        cont_p += 1
print('Você informou {} números e {} são PARES. \n A soma foi {}'.format(cont, cont_p,soma))