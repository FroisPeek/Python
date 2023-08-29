listaVeiculos = []


def linha():  # def apenas pra criar uma divisão entre as questões
    print("-" * 50)

    # código das aulas de POO em python.
    # tudo feito para estudos futuros.


def mostrar_dados(self):  # def mostrar dados, economiza linhas que seriam feitas em print
    print("- Modelo: ", self.modelo)
    print("- Ano: ", self.ano)
    print("- Valor: ", self.valor)


def qtd_veiculos():
    listaVeiculos.append(Veiculo)


class Veiculo:  # class principal, caracterizando o objeto
    def __init__(self, modelo, ano, valor):
        self.modelo = modelo  # caracteristica modelo
        self.ano = ano  # caracteristica ano
        self.valor = valor  # caracteristica valor

    def get_modelo(self):
        return self.get_modelo()

    def set_modelo(self, novo_modelo):
        self.modelo = novo_modelo

    def get_ano(self):
        return self.ano()

    def set_ano(self, novo_ano):
        self.ano = novo_ano

    def get_valor(self):
        return self.valor

    def set_aumento_valor(self, aumento_valor):  # função para adicionar valor ao valor principal do objeto
        self.valor = self.valor + aumento_valor

    def set_valor(self, novo_valor):  # função para informar uma nova caracteristica ao objeto
        if novo_valor < 0:  # substituindo o valor anterior com a condição de ser valor positivo
            self.valor = float(input("Informe um valor valido (positivo): "))
        else:
            self.valor = novo_valor

    def retorna_dados(self):
        dados = f'Modelo: {self.modelo}, {self.ano}, {self.valor}'  # retornar dados, imprime os dados concatenados
        return dados


if __name__ == '__main__':
    veiculo1 = Veiculo("Mercedes", 2022, 190000)  # declaração do objeto 1
    veiculo2 = Veiculo("BMW MK 3", 2012, 250500)  # declaração do objeto 2

    mostrar_dados(veiculo1)
    linha()
    mostrar_dados(veiculo2)
    linha()
    linha()
    print("Os dados concatenados: ", veiculo1.retorna_dados())
    print("Os dados concatenados: ", veiculo2.retorna_dados())
    linha()

    linha()
    veiculo1.set_aumento_valor(float(input("Informe o valor para ser adicionado ao preço total: R$")))
    veiculo2.set_valor(500000)

    print("\nNovos dados: ")
    mostrar_dados(veiculo1)
    linha()
    mostrar_dados(veiculo2)

    linha()
    modelo_carro_novo = input("Informe o modelo: ")
    ano_carro_novo = int(input("Informe  o ano do carro: "))
    veiculo3 = Veiculo(modelo_carro_novo, ano_carro_novo, 0)
    linha()
    mostrar_dados(veiculo3)
    linha()

    veiculo4 = Veiculo("Gol quadrado", 0, 0)
    veiculo5 = Veiculo("Gol bolinha", 2002, 0)

    mostrar_dados(veiculo4)
    linha()
    mostrar_dados(veiculo5)

    linha()
