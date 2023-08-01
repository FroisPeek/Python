l_altura = []
l_genereo = []
print("Digite [0] para sair do programa")
while True:
    altura = float(input("Informe a altura: "))
    if altura == 0:
        break
    l_altura.append(altura)

    genero = input("Informe o genere, [f] para feminino e [m] para masculino: ")
    l_genereo.append(genero)

print(f"A maior altura: {max(l_altura)}")
print(f"A menor altura: {min(l_altura)}")
print("A quantidade de homens: ", l_genereo.count("m"))
print("A quantidade de mulheres: ", l_genereo.count("f"))