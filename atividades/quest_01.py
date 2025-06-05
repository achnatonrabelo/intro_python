'''
01) Escreva um script que solicita do usuário o seu nome
completo, data de nascimento, e imprima uma mensagem
como a seguir:
Ex: Seu nome é XXXXX e você tem xxx anos de idade
obs: utilizar a função input() e formatar a saída com f-Strings
'''
import datetime

try:
    # ENTRADA DE DADOS
    nome_completo = input('Informe seu nome: ')
    data_nascimento = input('Informe a data so seu nascimento: ')

    # PROCESSAMENTO DE DADOS
    dados_data = data_nascimento.split('/')

    dia = int(dados_data[0])
    mes = int(dados_data[1])
    ano = int(dados_data[2])

    data_nascimento = datetime.datetime(ano, mes, dia)

    ano_atual = datetime.datetime.now().year
    ano_nascimento = data_nascimento.year

    idade = ano_atual - ano_nascimento

    # SAÍDA DE DADOS
    print(f'Seu nome é {nome_completo} e você tem {idade} anos de idade')
except:
    print('Data inválida! Insira no formato DD/MM/AAAA Tente novamente')