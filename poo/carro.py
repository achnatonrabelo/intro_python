# Definição da classe Carro
class Carro:
    # Atributos da classe Carro
    def __init__(self, fabricante, modelo, ano):  
        self.fabricante = fabricante
        self.modelo = modelo
        self.ano = ano
        print(f'Carro {self.modelo} criado...')

    # Método info que retorna os dados do objeto carro
    def info(self) -> str:
        saida = ''
        saida += f'Modelo: {self.modelo}\n'
        saida += f'Fabricante: {self.fabricante}\n'
        saida += f'Ano: {self.ano}'

        return saida
