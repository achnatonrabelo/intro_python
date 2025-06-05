'''
03) Escreva um script que converta a uma temperatura de graus 
Fahrenheit para graus Celsius. A saída deve evidenciar os valores
das temperaturas nas duas unidades.
'''

import os

print('Conversor de temperatura de Fahrenheit para Ceisius')

temp_fahrenheit = float(input('Informe a temperatura em Fahrenheit: '))

temp_celsius = 5 / 9 * (temp_fahrenheit - 32) # C = 5/9(F-32)

os.system('cls')

print(f'''A temperatura em graus Celsius correspondente a
{temp_fahrenheit}ºF é de {temp_celsius:.2f}ºC''')