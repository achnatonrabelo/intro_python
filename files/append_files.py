with open('./alunos.txt', 'a') as f:
    f.write('Lídia Costa\n')

with open('./alunos.txt') as f:
    print(f.read())