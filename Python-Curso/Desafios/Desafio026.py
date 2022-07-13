'''


Desafio 026

Faça um programa que leia uma frase pelo teclado e mostre:

Quantas vezes a letra "A" aparece.

Em que posição ela aparece a primeira vez.

Em que posição ela aparece pela última vez.


'''
print('='*50 + 'Analisandor de letras' + '='*50)


n = str(input('Digite uma frase: ')).upper()
print('A letra "A" aparece {} vezes'.format(n.count('A')))
print('A letra "A" aparece pela primeira vez na posição {}'.format(n.find('A') + 1))
print('A letra "A" aparece pela última vez na posição {}'.format(n.rfind('A')+1))