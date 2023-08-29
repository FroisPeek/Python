def linha():
    print("-" * 50)


def mostrar_dados(self):
    print("- Nome: ", self.nome)
    print("- Idade: ", self.idade)
    print("- Obra: ", self.obra)


class Construtor:
    def __init__(self, nome, idade, obra):
        self.nome = nome
        self.idade = idade
        self.obra = obra

    def get_nome(self):
        return self.nome

    def set_nome(self, novo_nome):
        self.nome = novo_nome

    def get_idade(self):
        return self.idade

    def set_idade(self, nova_idade):
        self.idade = nova_idade

    def get_obra(self):
        return self.obra

    def set_obra(self, nova_obra):
        self.obra = nova_obra


if __name__ == '__main__':
    construtor1 = Construtor("Glauber", 45, "Torre Eiffel")
    construtor2 = Construtor("Antonio", 39, "Cristo Redentor")
    construtor3 = Construtor("Ulices", 62, "Avenida Paulista")

    linha()
    print("Nome do construtor 1:", construtor1.get_nome())
    print("Idade dele:", construtor1.get_idade())
    print("Principal obra:", construtor1.get_obra())

    linha()
    print("Nome do construtor 2:", construtor2.get_nome())
    print("Idade dele:", construtor2.get_idade())
    print("Principal obra:", construtor2.get_obra())

    linha()
    print("Nome do construtor 3:", construtor3.get_nome())
    print("Idade dele:", construtor3.get_idade())
    print("Principal obra:", construtor3.get_obra())
    linha()

    construtor1.set_nome("Geremias")
    construtor2.set_nome("Jair")
    construtor3.set_nome("Osmar")

    print("\nApós atualizações --> ")
    print("Nome do construtor 1:", construtor1.get_nome())
    print("Idade dele:", construtor1.get_idade())
    print("Principal obra:", construtor1.get_obra())

    linha()
    print("Nome do construtor 2:", construtor2.get_nome())
    print("Idade dele:", construtor2.get_idade())
    print("Principal obra:", construtor2.get_obra())

    linha()
    print("Nome do construtor 3:", construtor3.get_nome())
    print("Idade dele:", construtor3.get_idade())
    print("Principal obra:", construtor3.get_obra())
    linha()
    linha()

    construtor1.set_nome("Geremias")
    construtor2.set_nome("Jair")
    construtor3.set_nome("Osmar")
