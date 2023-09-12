class Objeto:
    def __init__(self, tamanho, peso, preco=0):
        self.tamanho = tamanho
        self.peso = peso
        self.preco = preco

    def get_tamanho(self):
        return self.tamanho

    def set_tamanho(self, novo_tamanho):
        self.tamanho = novo_tamanho

    def get_peso(self):
        return self.peso

    def set_peso(self, novo_peso):
        self.peso = novo_peso

    def get_preco(self):
        return self.preco

    def set_preco(self, novo_preco):
        if preco < 0:
            print("Valor negativo, informe um novo valor!")
            self.preco = novo_preco

    def tamanho2(self):
        tamanho_quadrado = self.tamanho * self.tamanho
        print("O tamanho ao quadrado: ")
        return tamanho_quadrado

    def pesoleve(self):
        peso_leve = self.peso - 10
        print("O peso menos 10kg: ")
        return peso_leve

    def __str__(self):
        return f"{self.tamanho} - {self.peso} - {self.preco}"


if __name__ == '__main__':
    maquita = Objeto(0.50, 6.9, 400)
    lava_roupa = Objeto(1.5, 11)
    #colher = Objeto(0.10)  # vai dar erro no codigo por falta de um argumento.

    print("LAVA ROUPAS BRASTEMP: ")
    print(str(lava_roupa))


    print(lava_roupa.tamanho2())
    print(lava_roupa.pesoleve())
