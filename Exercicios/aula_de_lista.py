lista_nota = []
nota = 0
print("Insira [-1] para sair do programa! ")
while True:
    nota = float(input("Informe a nota do aluno: "))
    if nota == -1:
        break
    else:
        lista_nota.append(nota)

print(f"A media da turma: {(sum(lista_nota) / len(lista_nota)):.2f}")
print("A quantidade de alunos: ", len(lista_nota))
