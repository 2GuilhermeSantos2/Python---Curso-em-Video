"""


Desafio 007

Desenvolva um programa que leia as notas dos 4 bimestre de um aluno, e calcule e mostre sua média.


"""
print('='*50 + 'Média de Notas' + '='*50)
n1 = float(input('Digite a nota do 1ºBimestre: '))
n2 = float(input('Digite a nota do 2ºBimestre: '))
n3 = float(input('Digite a nota do 3ºBimestre: '))
n4 = float(input('Digite a nota do 4ºBimestre: '))
m = (n1+n2+n3+n4)/4

print('A nota do 1ºBimestre foi {:.1f} \n A nota do 2ºBimestre foi {:.1f} \n A nota do 3ºBimestre foi {:.1f} \n '
      'A nota do 4ºBimestre foi {:.1f} \n A média do ano foi {:.1f}'.format(n1, n2, n3, n4, m))


