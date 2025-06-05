senac = 'SERVIÇO NACIONAL DE APRENDIZAGEM COMERCIAL'
print('Tamanho da string:', len(senac))

print(senac[0])
print(senac[1])
print(senac[2])
print(senac[3])
print(senac[4])
print(senac[5])
print(senac[6])

print('-' * 40)

for i in senac:
    print(i, end='')

print()

termo_pesquisa = 'COMERCIAL'

if termo_pesquisa in senac:
    print('A palavra', termo_pesquisa, 'existe na string senac')

if termo_pesquisa not in senac:
    print('A palavra', termo_pesquisa, 'não existe na string senac')
