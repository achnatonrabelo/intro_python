'''
Crie um scrit que simule um jogo de advinhação, onde o computador
gera um número aleatório entre 1 e 10, e o usuário tem que adivinhar
qual o número sorteado pelo computador. O usuário terá 3 tentativas
para acertar o número
'''

import random, os

os.system('cls')

print('''Tenta advinhar o número sorteado entre 1 e 10. 
Você tem 3 tentativas...''')

numero_sorteado = random.randrange(1, 11)
tentativas = 3

palpite = int(input('Qual o seu palpite para o número sorteado? '))

while tentativas > 0:
    tentativas -= 1
    if palpite == numero_sorteado:
        print('Bingo!!! Você acertou o número sorteado')
        break # Encerra imediatamente a execução do laço
    elif palpite < numero_sorteado:
        print('Seu palpite foi menor que o número sorteado')
    else:   
        print('Seu palpite foi maior que o número sorteado')

    palpite = int(input(f'Você ainda tem {tentativas} tentativa. Tente novamente: '))

print('********** FIM DO SCRIPT **********')
