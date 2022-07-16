"""
for c in range(1, 7):
    print('oi')
    print(c)
print('FIM!!')

"""
"""
for c in range(6, 0, -1): = Faz em ordem decrescente de em 1 em 1
    print(c)
print('FIM!!')

"""
"""
for c in range(0, 7, 2): #Faz de 0 a 6 pulando de 2 em 2, Vai até o 7 por que o último valor já sai da condição
    print(c)
print('FIM!!')

"""
"""
inicio = int(input('Inicio:')) # Onde começa
fim = int(input('Fim: ')) # Até onde vai
passo = int(input('Passo: ')) # Quanto em quanto vai pular

for c in range(inicio, fim+1, passo):
    print(c)
print('FIM!!')

"""
s = 0
for c in range(0, 10):
    n = int(input('Digite um valor: '))
    s += n # É o mesmo de s = s + n
print('O somtório de todos os valores foi {}'.format(s))