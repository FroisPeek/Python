def mostrar_dados(self):
    print("- Nome: ", self.nome)
    print("- RA: ", self.ra)
    print("- Curso: ", self.curso)


def linha():
    print("-" * 50)


class Aluno:
    def __init__(self, nome, ra, curso):
        self.nome = nome
        self.ra = ra
        self.curso = curso

    def get_nome(self):
        return self.get_nome()

    def set_nome(self, novo_nome):
        self.nome = novo_nome

    def get_ra(self):
        return self.get_ra()

    def set_ra(self, novo_ra):
        if novo_ra < 0:
            novo_ra = int(input("Informe um valor valido (positivo): "))
            self.ra = novo_ra
        else:
            self.ra = novo_ra

    def get_curso(self):
        return self.curso

    def set_curso(self, novo_curso):
        self.curso = novo_curso

    def adicionar_curso(self):
        cursos_add = input("Informe os cursos: ")
        if self.curso != "":
            self.curso = cursos_add + ", " + self.curso
        else:
            self.curso = cursos_add + self.curso

    def trancar(self):
        return "está pensando em trancar o curso."


if __name__ == '__main__':
    aluno1 = Aluno("Frois", 132, "ciencias da computacao")
    aluno2 = Aluno("Thiago", 542, "")  # Se nao for informado o parametro do objeto, o programa vai dar erro.
    aluno3 = Aluno("Fernando", "", "")  # Ent, informo um parametro vazio com string vazia = "".

    linha()
    linha()
    mostrar_dados(aluno1)
    linha()
    mostrar_dados(aluno2)
    linha()
    mostrar_dados(aluno3)
    linha()
    linha()
    print("\nTestando novos métodos do aluno1: ")
    aluno1.set_nome("Glauber")
    aluno1.set_ra(-1)  # informando um valor negativo para cair na condicao if
    aluno1.set_curso("ADS")
    mostrar_dados(aluno1)
    linha()
    linha()

    print("\nTeste das funcoes --> ")
    aluno1.adicionar_curso()
    aluno2.adicionar_curso()
    linha()
    mostrar_dados(aluno1)  # vai informa o curso ja mencionado e o curso adicionado
    mostrar_dados(aluno2)  # como nao tinha nenhum curso atribuido, vai ter apenas o curso adicionado
    linha()
    x = int(input("Informe qual aluno esta pensando em trancar o curso [1, 2, 3]: "))
    if x == 1:
        print(f"{aluno1.nome} {aluno1.trancar()}")
    elif x == 2:
        print(f"{aluno2.nome} {aluno2.trancar()}")
    elif x == 3:
        print(f"{aluno3.nome} {aluno3.trancar()}")
    else:
        print("informe um valor valido")
