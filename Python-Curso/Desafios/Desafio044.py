"""


Desafio 044

Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

À vista dinheiro/pix: 15% de desconto
À vista no cartão: 5% de desconto
Em até 2x no cartão: Preço normal
3x ou mais no cartão: 20% de juros


"""
from time import sleep
print('='*114)
print('='*50 + 'LOJAS INFINITY' + '='*50)
print('='*114)
preço = float(input('Digite o valor do produto R$'))
escolha = (int(input('Escolha um método de pagamento \n'
                       ' [1] Para pagamento à vista em dinheiro ou pix: \n'
                       ' [2] Para pagamento à vista em no cartão de débito: \n '
                       '[3] Para até 2x no cartão de crédito: \n'
                       ' [4] Para mais de 3x no cartão de crédito:  \n'
                       '')))
print('='*114)
print('='*50 + 'LOJAS INFINITY' + '='*50)
print('Processando sua compra....')
print('='*114)
sleep(1)

din_pix = preço - (preço * 0.15)
cartao_debito = preço - (preço * 0.05)
ate_2x = preço
mais_3x = preço + (preço * 0.20)

if escolha == 1:
    print('Parabéns você pagou à vista, então ganhou um desconto de 15%. O valor do produto ficou R${:.2f}'.format(din_pix))
elif escolha == 2:
    print('Parabéns você pagou à vista no cartão de débito, então ganhou um desconto de 5%. O valor de produto ficou R${:.2f}'.format(cartao_debito))
elif escolha == 3:
    escolha_pagamento = (int(input('Em quantas vezes ira parcelar? 1x ou 2x \n'
                                   '')))
    if escolha_pagamento == 1:
        print('Você pagou em 1x. O valor final ficou R${:.2f}'.format(ate_2x))
    elif escolha_pagamento == 2:
        print('Você pagou em 2x. O valor final ficou R${:.2f}'.format(ate_2x))
    elif escolha_pagamento != 1 or 2:
        print('ERROR!!! Você tem que escolher um 1x ou 2x')
        escolha_pagamento = (int(input('Em quantas vezes ira parcelar? 1x ou 2x \n'
                                       '')))


elif escolha == 4:
    escolha_pagamento = (int(input('Em quantas vezes ira parcelar?\n'
                                   '')))
    if escolha_pagamento == 1 or escolha_pagamento == 2:
        print('Você pagou em {}x. O valor final ficou R${:.2f}'.format(escolha_pagamento,ate_2x))
    else:
        print('Você parcelou o produto em {}x. Mas ouve um juros de 20% então o valor do produto ficou R${:.2f}'.format(escolha_pagamento,mais_3x))
elif escolha != 1 or 2 or 3 or 4:
    print('ERROR!!!. Digite uma opção valida')

print('='*114)




