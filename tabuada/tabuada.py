from rich.table import Table
def tabuada(tabuada, operacao) -> Table:
    '''Gera a saída formatada da tabuada
    Parans:
     -tabuada: número da tabuada
     -operacao: sinal da tabuada ('+', '-', '*', '/')
    '''
    table = Table(title=f'Tabuada do {tabuada} - ({operacao})', show_header=True, header_style='bold magenta')        
    table.add_column("Espressão", justify='center', style='cyan', no_wrap=True)
    table.add_column("Resultado", justify='center', style='magenta')

    expressao = ''
    result = 0
    
    if operacao == '+':
        for i in range(1, 11):
            expressao = f'{tabuada} {operacao} {i}'
            result = tabuada + i
            table.add_row(expressao, str(result))
    elif operacao == '-':
        for i in range(1, 11):
            expressao = f'{tabuada + i} {operacao} {tabuada}'
            result = f'{tabuada + i - tabuada}'
            table.add_row(expressao, str(result))
    elif operacao == '*':
        for i in range(1, 11):
            expressao = f'{tabuada} {operacao} {i}'
            result = f'{tabuada * i}'
            table.add_row(expressao, str(result))
    elif operacao == '/':
        for i in range(1, 11):
            expressao = f'{tabuada * i} {operacao} {tabuada}'
            result = f'{(tabuada * i / tabuada):.0f}'
            table.add_row(expressao, str(result))
            # saida += f'{tabuada * i} {operacao} {tabuada} = {(tabuada * i / tabuada):.0f}\n'
    
    return table
