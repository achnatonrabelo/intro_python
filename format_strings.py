aluno = "Rodrigo Bastos"
idade = 16
nacionalidade = "brasileiro"
sexo = "masculino"

print(
    "Seu nome é", 
    aluno, 
    ", você tem", 
    idade, 
    "anos de idade, é", 
    nacionalidade, 
    "e do sexo", 
    sexo
)

mensagem = "Seu nome é " + aluno + ", você tem " + str(idade) + " anos de idade, é " + nacionalidade + " e do sexo " + sexo

print(mensagem)

mensagem = f"Seu nome é {aluno}, você tem {idade} anos de idade, " \
f"é \n{nacionalidade} e do sexo {sexo}"
print(mensagem)

mensagem = f"""Seu nome é {aluno}, você tem {idade} anos de idade, é 
\t{nacionalidade} e do sexo {sexo}"""
print(mensagem)
