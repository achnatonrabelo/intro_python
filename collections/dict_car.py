carro_01 = {
    'fabricante': 'Chevrolet',
    'modelo': 'Onix',
    'ano': 2023,
    'novo': False
}

carro_02 = {
    'fabricante': 'Fiat',
    'modelo': 'Chronus',
    'ano': 20235,
    'novo': True
}

carros = [carro_01, carro_02]

for carro in carros:
    print(f'Fabricante: {carro.get('fabricante')}')
    print(f'Modelo: {carro.get('modelo')}')
    print(f'Ano: {carro.get('ano')}')
    print(f'É novo: {carro.get('novo')}')
    print('-' * 50)

# print(type(carro))
# print(carro)
# print('-' * 50)
# print(f'Fabricante: {carro["fabricante"]}')
# print(f'Modelo: {carro["modelo"]}')
# print(f'Ano: {carro["ano"]}')
# print(f'É novo? {'Sim' if carro["novo"] else 'Não'}')