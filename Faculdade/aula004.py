def linha():
    print("-" * 30)


class Produto:
    def __init__(self, nome, vlr_compra=0.0, vlr_venda=0.0, qnt_estoque=0, qnt_minima=0):
        self.nome = nome
        self.vlr_compra = vlr_compra
        self.vlr_venda = vlr_venda
        self.qnt_estoque = qnt_estoque
        self.qnt_minima = qnt_minima

    def get_nome(self):
        return self.nome

    def set_nome(self, novo_nome):
        if len(novo_nome) <= 3:
            print("Nome invalido!")
        else:
            self.nome = novo_nome

    def get_qnt_estoque(self):
        return self.qnt_estoque

    def set_qnt_estoque(self, nova_qnt_estoque):
        if nova_qnt_estoque < 11:
            self.qnt_estoque = nova_qnt_estoque

    def get_qnt_minima(self):
        return self.qnt_minima

    def set_qnt_minima(self, nova_qnt_minima):
        self.qnt_minima = nova_qnt_minima

    def get_vlr_compra(self):
        return self.vlr_compra

    def set_vlr_compra(self, novo_vlr_compra):
        if novo_vlr_compra == self.vlr_venda:
            print("Sem lucros! Não vai ter mudança do valor.")
        else:
            self.vlr_compra = novo_vlr_compra

    def lucro(self):
        lucro = self.vlr_venda - self.vlr_compra
        return lucro

    def atualiza_estoque(self):
        qnt_vendida = int(input("Informe a quantidade vendida: "))
        self.qnt_estoque = self.qnt_estoque - qnt_vendida

    def repor_produto(self):
        reposicao = int(input("Informe a quantidade da nova carga dos produtos: "))
        self.qnt_estoque = self.qnt_estoque + reposicao

    def alerta_estoque(self):
        if self.qnt_estoque <= self.qnt_minima:
            return True
        else:
            return False

    def maior_qtd(self, obj):
        if self.qnt_estoque > obj.qnt_estoque:
            print(f"Maior qantidade de estoque {self.qnt_estoque}")
            print(f"Menor quantidade de estoque {obj.qnt_estoque}")
        elif obj.qtd_estoque > self.qnt_estoque:
            print(f"Maior quantidade de estoque {obj.qnt_estoque}")
            print(f"Menor quantidade de estoque {self.qnt_estoque}")
        else:
            print(f"Os estoques são iguais {self.qnt_estoque}")

    def maior_lucro(self, obj):
        if self.lucro() > obj.lucro():
            print(f"Maior qantidade de lucro {self.lucro()}")
            print(f"Menor quantidade de lucro {obj.lucro()}")
        elif obj.lucro() > self.lucro():
            print(f"Maior quantidade de lucro {obj.lucro()}")
            print(f"Menor quantidade de lucro {self.lucro()}")
        else:
            print(f"Os lucro são iguais {self.lucro()}")

    def listaProdutosZika(self):
        print("Quantidade de produtos cadastrados na lista zika: ", len(listaProdutos))

    def __str__(self):
        return f"{self.nome} - {self.vlr_compra} - {self.vlr_venda} - {self.qnt_estoque} - {self.qnt_minima}"


if __name__ == '__main__':
    listaProdutos = []
    arroz = Produto("Arroz Branco", 19.00, 27.50, 67, 20)
    arroz.set_qnt_minima(12)
    arroz.set_qnt_estoque(10)
    arroz.set_nome("lentilha")
    arroz.set_vlr_compra(27.50)
    print(arroz)
    print("O lucro da venda em reais: ", arroz.lucro())
    linha()
    arroz.atualiza_estoque()
    print(arroz)
    linha()
    arroz.repor_produto()
    print(arroz)
    linha()
    feijao = Produto("Feijão Fraudinho")
    coca = Produto("Coca Cola 2L", 11.50)
    chocolate = Produto("Diamante Negro", qnt_estoque=4)
    print(feijao)
    print(coca)
    print(chocolate)
    linha()
    arroz.maior_qtd(feijao)
    arroz.maior_lucro(chocolate)
    listaProdutos.append(arroz)
    listaProdutos.append(feijao)
    listaProdutos.append(coca)
    listaProdutos.append(chocolate)
    linha()
    print("Quantidade de produtos cadastrados: ", len(listaProdutos))
    linha()
    arroz.listaProdutosZika()

