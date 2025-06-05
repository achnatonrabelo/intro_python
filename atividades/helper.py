# Definição da função imc()
def imc(peso, altura):
    imc = peso / (altura ** 2)
    if imc > 40.0:
        status = '[bold red]Obesidade grau III[/bold red]'
    elif imc >= 35.0 and imc <= 39.9:
        status = '[bold red]Obesidade grau II[/bold red]'
    elif imc >= 30.0 and imc <= 34.9:
        status = '[bold red]Obesidade grau I[/bold red]'
    elif imc >= 25.0 and imc <= 29.9:
        status = '[bold red]Sobrepeso[/bold red]'
    elif imc >= 18.6 and imc <= 24.9:
        status = '[bold red]Normal[/bold red]'
    else:
        status = '[bold red]Abaixo do normal[/bold red]'
    
    return imc, status