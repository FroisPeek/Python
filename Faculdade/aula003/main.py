from datetime import date


def linha():
    print("-" * 50)


def mostrarDados(self):
    print("- Nome: ", self.nome)
    print("- Peso: ", self.peso)
    print("- Altura: ", self.altura)
    print("- Ano de Nascimento: ", self.anoNascimento)


class Pessoa:
    def __init__(self, nome, peso, altura, anoNascimento=2000):
        self.nome = nome
        self.peso = peso
        self.altura = altura
        self.anoNascimento = anoNascimento

    def get_nome(self):
        return self.get_nome()

    def set_nome(self, novo_nome):
        if len(novo_nome) == 0:
            print("Nome invalido!")
        else:
            self.nome = novo_nome

    def get_peso(self):
        return self.get_peso()

    def set_peso(self, novo_peso):
        self.peso = novo_peso

    def get_altura(self):
        return self.get_altura()

    def set_altura(self, nova_altura):
        self.altura = nova_altura

    def get_anoNascimento(self):
        return self.anoNascimento

    def set_anoNascimento(self, novo_ano):
        self.anoNascimento = novo_ano

    def imc(self):
        imc = self.peso / (self.altura * self.altura)
        print(f"- O IMC : {imc:.2f}")

    def CalculaIdade(self):
        data = date.today()
        data_ano = data.strftime("%Y")
        conta = int(data_ano) - self.anoNascimento
        return conta

    def __str__(self):
        s = f"{self.nome}, {self.peso}, {self.anoNascimento}"
        return s

    def maisVelho(self, obj):

        if self.anoNascimento < obj.anoNascimento:
            print("Ano de nascimento mais velho: ", self.anoNascimento)
            print("Ano de nascimento mais novo: ", obj.anoNascimento)
        elif obj.anoNascimento < self.anoNascimento:
            print("Ano de nascimento mais velho: ", obj.anoNascimento)
            print("Ano de nascimento mais novo: ", self.anoNascimento)
        else:
            print("Os valores são iguais.")


if __name__ == '__main__':
    pessoa1 = Pessoa("Eduardo", 65, 1.85, 2005)
    pessoa2 = Pessoa("Lourrane", 60, 1.63, 2006)

    linha()
    print("Pessoa cadastrada em: ", pessoa1)
    mostrarDados(pessoa1)
    linha()
    print("Pessoa cadastrada em: ", pessoa2)
    mostrarDados(pessoa2)
    linha()

    print("6- No main, teste os métodos dos atributos da classe Pessoa (consulte e mostre")
    print("Mostre o atributo nome e mostre o atributo ano de nascimento")
    print("--->")
    pessoa2.set_nome("Fernando")
    pessoa2.set_anoNascimento(2005)
    mostrarDados(pessoa2)

    linha()
    print("Teste do IMC -->")
    mostrarDados(pessoa1)
    pessoa1.imc()
    linha()

    print("Pessoa 3 cadastrada: ")
    pessoa3 = Pessoa("Thiago", 68, 1.80, 2005)
    mostrarDados(pessoa3)
    linha()

    print("Dados com o valor default em ano nascimento: ")
    pessoa4 = Pessoa("Glauber", 123, 1.50)
    mostrarDados(pessoa4)
    linha()

    print("Crie o método calcula_idade, ele recebe o objeto e retorna a idade da pessoa.")
    print(f"A idade da pessoa1: {pessoa1.CalculaIdade()}")
    linha()

    print("Testando o metodo str: ")
    print(pessoa1)
    linha()

    print("QUESTAO SUPREMA 15 >>>>>>>>>>>>>>>")
    pessoa1.maisVelho(pessoa4)
