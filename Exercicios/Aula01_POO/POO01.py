def linha():
    print("-" * 50)


def mostrar_dados(self):
    print("- Nome: ", self.nome)
    print("- Mensalidade: ", self.mensalidade)
    print("- Idade: ", self.idade)


def cnh(x):
    if x.get_idade() >= 18:
        print("O aluno pode tirar cnh")
    else:
        print("O aluno ainda nao pode tirar cnh")


class Aluno:
    def __init__(self, nome, mensalidade, idade):
        self.nome = nome
        self.mensalidade = mensalidade
        self.idade = idade

    def get_nome(self):
        return self.nome

    def set_nome(self, novo_nome):
        self.nome = novo_nome

    def get_mensalidade(self):
        return self.mensalidade

    def set_mensalidade(self, valor):
        self.mensalidade = valor

    def get_idade(self):
        return self.idade

    def set_idade(self, nova_idade):
        self.idade = nova_idade

    def nova_mensalidade(self, nova_mensalidade):
        self.mensalidade = nova_mensalidade + self.mensalidade

    def aumento_mensalidade_porcentagem(self, porcentagem):
        self.mensalidade = self.mensalidade + self.mensalidade / 100 * porcentagem
        return self.mensalidade

    def reset(self):
        self.mensalidade = 1000.00
        self.idade = 18


if __name__ == '__main__':
    aluno1 = Aluno('Eduardo', 1100.00, 18)
    print(aluno1)
    aluno2 = Aluno('Lourrane', 900.00, 17)
    print(aluno2)
    linha()
    linha()
    mostrar_dados(aluno1)
    linha()
    mostrar_dados(aluno2)
    linha()
    aluno1.set_nome('Frorororois')
    print("\nAluno novo: ", aluno1.get_nome())
    print("Nova mensalidade: 1900.99")
    aluno1.nova_mensalidade(1900.99)
    print("Total: ", aluno1.get_mensalidade())
    linha()
    porcentagem = int(input("Informe a porcentagem: "))
    print(f"Mensalidade com o aumento do aluno 2: {aluno2.aumento_mensalidade_porcentagem(porcentagem):.2f}")
    linha()
    x = int(input("Informe de qual aluno quer verificar a possibilidade de cnh [1][2]: "))
    if x == 1:
        cnh(aluno1)
    elif x == 2:
        cnh(aluno2)
    else:
        print("Aluno nao identificado")

    aluno1.reset()
    aluno2.reset()

    aluno3 = Aluno('Fernando') # codigo teste para ver o erro do programa
    print(aluno3.set_nome(3)) # codigo teste para ver o erro do programa

    # linha 85 e 86 não funcionam