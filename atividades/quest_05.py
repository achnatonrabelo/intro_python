'''
Escreva um script em Python que calcule o índice de massa
corporal (IMC) de uma pessoa. O usuário terá que fornecer os dados
do seu peso e altura. Como saída o script deve apresentar um resultado
conforme a tabela abaixo:

Acima de 40.0: Obesidade grau III
Entre 35.0 e 39.9: Obesidade grau II
Entre 30.0 e 34.9: Obesidade grau I
Entre 25.0 e 29.9: Sobrepeso
Entre 18.6 e 24.9: Normal
18.5 ou menos: Abaixo do normal
'''

import os
from rich import print
from helper import imc

os.system('cls')

peso = float(input('Informe o seu peso: '))
altura = float(input('Informe a sua altura:'))

calc_imc, status = imc(peso, altura)

tabela_imc = '''Acima de 40.0: Obesidade grau III
Entre 35.0 e 39.9: Obesidade grau II
Entre 30.0 e 34.9: Obesidade grau I
Entre 25.0 e 29.9: Sobrepeso
Entre 18.6 e 24.9: Normal
18.5 ou menos: Abaixo do normal
'''

print(tabela_imc)
print(f'Seu índice de massa corporal está em {calc_imc:.2f} e seu status é {status}')
