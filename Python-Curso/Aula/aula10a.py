"""
nome = str(input('Qual é seu nome? ')).capitalize()

if nome == 'Guilherme':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')
print('Bom dia, {}'.format(nome))

"""

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2

if m >= 6:
    print('Aprovado')
elif m == 5:
    print('Recuperação')
else:
    print('Reprovado')
print('A sua média foi {:.1f}'.format(m))