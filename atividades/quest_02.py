'''
02) Calcume o desconto: Escreva um script que contenha uma função
que, passados o valor da compra e a porcetam de desconto devolva 
o valor da compra com o desconto.
Os valores do valor da compra e percentual de desconto devem ser 
fornecidos pelo usuário utilizando a função input()'''

import locale

locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')

def aplicaDesconto(valor, desconto):
    valor =  valor - (valor * (desconto / 100))
    return locale.currency(valor, grouping=True, symbol=True)


valor = input('Informe o valor da compra: ')
desconto = input('Informe o percentual de desconto: ')

valor = float(valor)
desconto = float(desconto)

valor_com_desconto = aplicaDesconto(valor, desconto)

print(valor_com_desconto)
