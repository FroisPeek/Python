lista_pares = []
valor = 0
print("Informe os seguintes numeros para a media dos pares (use [0] para sair): ")
while True:
    valor = int(input("Insira os valores: "))
    if valor == 0:
        break
    if valor % 2 == 0:
        lista_pares.append(valor)

if len(lista_pares) == 0:
    print("não foi informado valores pares!")
else:
    print(f"A media dos valores pares: {(sum(lista_pares) / len(lista_pares)):.2f}")
    print("Os valores pares digitados foram: ", lista_pares)
