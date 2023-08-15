lista = []


def menu():
    print("[C] - Create (Inserir um item)")
    print("[R] - Read (Mostrar toda a lista)")
    print("[U] - Update (Substituir um item)")
    print("[D] - Delete (Remove um item)")
    print("[E] - Exit (Sair")
    opcao = input("Opção: ")
    return opcao


def create():
    nome = input("Informe o nome para inserir na lista: ")
    return lista.append(nome)


def read():
    print(lista)


def update():
    indice = int(input("Infome o indice para a substituição: "))
    nome = input("Informe o novo nome: ")
    lista[indice] = nome


def delete():
    print(lista)
    indice = int(input("Informe o indice do nome que você quer retirar da lista: "))
    lista.pop(indice)


if __name__ == '__main__':
    while True:
        op = menu().lower()
        if op == "c":
            print("Create")
            create()
        elif op == "r":
            print("Read")
            read()
        elif op == "u":
            print("Update")
            update()
        elif op == "d":
            print("Delete")
            delete()
        elif op == "e":
            break
