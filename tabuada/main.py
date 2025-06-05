from rich.console import Console
from rich.panel import Panel

from helpers import clear_screen
from tabuada import tabuada

console = Console()

def display_menu():
    MENU_TABUADA = '''[bold green][1][/bold green]: -> Tabuada de 1 a 10
[bold green][2][/bold green]: -> Adição (+)
[bold green][3][/bold green]: -> Subtração (-)
[bold green][4][/bold green]: -> Multiplicação (*)
[bold green][5][/bold green]: -> Divisão (/)
[bold green][0][/bold green]: -> Sair do Programa'''

    console.print(MENU_TABUADA)

clear_screen()

while True:
    display_menu()
    try:
        numero = input('Informe a tabuada desejada: ')
        
        if not numero.isdigit():
            raise ValueError('A tabuada deve ser um número inteiro entre 1 e 10.')
        
        numero = int(numero)

        if numero < 1 or numero > 10:
            raise ValueError('[bold red]Número fora do intervalor da tabuada![/bold red]')

        operacao = input('Informe a operação desejada (+, -, *, /): ')
        
        if operacao not in ('+', '-', '*', '/'):
            raise ValueError('[bold red]Operação inválida![/bold red]')
        
        # Objeto Table retornado, armazenado na variável "saida"
        table = tabuada(numero, operacao)
        panel = Panel(table, title='Tabuada', expand=False)
        
        clear_screen()
        console.print(panel)

        continuar = input('Deseja continuar? (s/n): ').strip().lower()
        clear_screen()
        if continuar != 's':
            clear_screen()
            console.print('[bold green]Programa encerrado.[/bold green]')
            break

    except ValueError as ve:
        clear_screen()
        console.print(f'[bold red]Erro: {ve}[/bold red]')
    except KeyboardInterrupt:
        clear_screen()
        console.print('\n[bold red]Programa encerrado pelo usuário.[/bold red]')
        break
