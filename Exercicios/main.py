def linha():
    print("\n------------------------------------------------------------------------")


lista = []
while True:
    x = int(input("Insira o valor: "))
    if x == 0:
        break
    else:
        lista.append(x)
linha()
print("A quantidade de elementos armazenados na lista: ", len(lista))
print("Soma dos valores da lista: ", sum(lista))
print("Maior valor da lista: ", max(lista))
print("Menor valor da lista: ", min(lista))
y = int(input("Informe um valor para verificar se ele esta na lista: "))
if y in lista:
    print(f"O valor {y} está na lista, e sua posição no indice: {lista.index(y)}")
else:
    print(f"O valor {y} não está na lista.")
print("A lista em ordem crescente: ", sorted(lista))

lista.insert(1, 33)
print("A lista o valor 33 adicionado: ", lista)

lista.sort(reverse=True)
print("Mostre a lista em ordem descrescente: ", lista)

media = sum(lista)/len(lista)
print(f"A media dos valores da lista: {media}")
print(f"A media com três casa decimais: {media:.3f}")

ct = 0
for i in range(len(lista)):
    if lista[i] >= 10:
        ct += 1
porcentagem = ct / len(lista) * 100
print("Porcentagem dos numeros maiores que dez na lista: ", porcentagem)
