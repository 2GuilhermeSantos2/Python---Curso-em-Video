nome = str(input('Qual é seu nome?'))

if nome == 'Guilherme':
    print('Que nome bonito!', end=' ')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.', end=' ')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino', end=' ')
else:
    print('Seu nome é bem normal.', end=' ')
print('Tenha um bom dia, {}!'.format(nome))
