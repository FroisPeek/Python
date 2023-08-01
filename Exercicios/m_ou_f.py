l_altura = []
l_genero = []
print("Digite [0] para sair do programa")
while True:
    altura = float(input("Informe a altura: "))
    if altura == 0:
        break
    l_altura.append(altura)

    genero = input("Informe o genere, [f] para feminino e [m] para masculino: ")
    l_genero.append(genero)

print(f"A maior altura: {max(l_altura)}")
print(f"A menor altura: {min(l_altura)}")
print("A quantidade de homens: ", l_genero.count("m"))
print("A quantidade de mulheres: ", l_genero.count("f"))
print(f"A media das alturas: {(sum(l_altura) / len(l_altura)):.2f}")
print("A porcentagem de homens: ", l_genero.count("m") / len(l_genero) * 100)
