'''
Escreva um programa que processe a média de uma determinada
quantidade de notas escolares fornecidas pelo usuário. O script
deve receber o nome do aluno e, em seguida, as notas que serão 
armazenadas em uma lista. A média deve ser calculada e exibida 
ao final com o status do aluno, de acordo com as regras abaixo:
- Aprovado(a): média maior ou igual a 7
- Recuperação: média maior ou igual a 5 e menor que 7
- Reprovado(a): média inferior a 5
Aluno: Nome do aluno
Notas: 10.0 9.5 8.4 10.0
Média: 8.7
Status: Aprovado(a)
--------------------------------
'''

import os

os.system('cls')

# Declaração de variáveis
alunos = []
media = 0
status = ''
notas_str = ''

while True:
    nome = input('Aluno(a): ')
    
    notas = []

    # Implementar alteração que permite ao usuário definir
    # a quandidade de notas que será processada

    i = 0
    while i < 4:
        nota = float(input(f'{i + 1}ª nota: '))

        if nota < 0 or nota > 10:
            print('Nota inválida! Informe uma nota entre 0 e 10')
            continue
        notas.append(nota)
        notas_str += str(nota) + ' '
        i += 1
    
    media = sum(notas) / len(notas)
    notas_str = notas_str.strip()
    
    if media >= 7.0:
        status = 'Aprovado(a)'
    elif media < 5.0:
        status = 'Reprovado(a)'
    else:
        status = 'Em recuperação'
    
    # Dicionário com dados de UM aluno
    aluno = {
        'nome': nome,
        'notas': notas_str,
        'media': media,
        'status': status
    }

    notas_str = ''

    alunos.append(aluno)

    os.system('cls')
    print('Aluno(a) cadastrado(a) com sucesso')
    print('Cadastrar novo(a) aluno(a)? ')
    
    continuar = input('Digite "S" para sim ou "N" para não: ')

    if continuar != "S":
        break

os.system('cls')

# Saída
for a in alunos:
    print(f'Aluno: {a['nome']}')
    print(f'Notas: {a['notas']}')
    print(f'Média: {a['media']}')
    print(f'Situação: {a['status']}')
    print('-' * 30)
