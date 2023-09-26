def linha(): 
    print("="*80)

class Objeto: 
    def __init__(self, nome, cor, peso = 0.0):
        self.nome = nome
        self.cor = cor
        self.peso = peso

    def get_nome(self):
        return self.nome
    
    def set_nome(self, novo_nome):
        self.nome = novo_nome

    def get_cor(self): 
        return self.cor
    
    def set_cor(self, nova_cor):
        self.cor = nova_cor

    def get_peso(self):
        return self.peso

    def set_peso(self, novo_peso):
        if self.peso <= 5.00:
            print("Muito leve, mude!")
            self.peso = novo_peso

    def tamanho(self, tamanho):
        tamanho = float(input("Informe o tamanho em metros quadrados: "))
        self.tamanho = tamanho

    def valor(self, valor):
        valor = float(input("Informe o valor desse objeto: "))
        self.valor = valor 

    def mais_pesado(self, obj):
        if self.peso > obj.peso: 
            print("O mais pesado é: ", self.peso, "e o mais leve é: ", obj.peso)
        elif self.peso < obj: 
            print("O mais pesado: ", obj.peso, "o mais leve: ", self.peso)
        else: 
            print("O peso dos dois objetos sao iguais.")
    
    def __str__(self):
        return f"Nome:{self.nome} / Cor:{self.cor} / Peso:{self.peso}Kg"


if __name__ == "__main__":
    obj1 = Objeto("Cubo Magico", "Colorido", 0.250)
    obj2 = Objeto("Dardo", "Vermelho", 0.050)
    obj3 = Objeto("Cadeira Gamer", "Verde", 12.0)
    print(obj1)
    obj1.tamanho(1)
    obj1.valor(1)
    print(f"O tamanho em metros quadrados: {obj1.tamanho}")
    print("O valor: ", obj1.valor)
    linha()

    obj1.mais_pesado(obj2)
    linha()

    print(obj1)
    print(obj2)
    print(obj3)