class Conta:
    def __init__(self, nome, saldo):
        self.nome = nome
        self.saldo = saldo

    def get_nome(self):
        return self.nome
    def set_nome(self, novo_nome):
        self.nome = novo_nome
    def get_saldo(self):
        return self.saldo
    def set_saldo(self, novo_saldo):
        self.saldo = novo_saldo

    def __str__(self):
        return f"Nome: {self.nome} - Saldo: {self.saldo}"
    
    def deposito(self, valor):
        self.saldo += valor

    def retirada_rn2(self, valor): 
        if isinstance(self, ContaPJ):
            print("5 reais de tarifa.")
            if self.saldo - 5 > valor :
                self.saldo = self.saldo - 5 - valor
            else: 
                print("Saldo insuficiente!")
        elif isinstance(self, ContaPF):
            print("2 reais de tarifa.")
            if self.saldo - 2 > valor :
                self. saldo = self.saldo - 2 - valor
            else: 
                print("Saldo insuficiente!")

    
class ContaPF(Conta):
    def __init__(self, nome, saldo, genero, CPF ):
        super().__init__(nome, saldo)
        self.genero = genero
        self.CPF =  CPF

    def get_genero(self):
        return self.genero
    def set_genero(self, novo_genero):
        self.genero = novo_genero
    def get_CPF(self):
        return self.CPF
    def set_CPF(self, novo_CPF):
        self.CPF = novo_CPF
    
    def __str__(self):
        return super().__str__() + f" - Gênero: {self.genero} - CPF: {self.CPF}"
    
    def retirada(self, valor):
        print("2 reais de tarifa.")
        if self.saldo - 2 > valor :
            self.saldo = self.saldo - 2 - valor
        else: 
            print("Saldo insuficiente!")

class ContaPJ(Conta):
    def __init__(self, nome, saldo, modalidade, cnpj):
        super().__init__(nome, saldo)
        self.modalidade = modalidade
        self.cnpf = cnpj

    def get_modalidade(self):
        return self.modalidade
    def set_modalidade(self, nova_modalidade):
        self.modalidade = nova_modalidade
    def get_cnpj(self):
        return self.cnpj
    def set_cnpj(self, novo_cnpj):
        self.cnpj = novo_cnpj

    def __str__(self):
        return super().__str__() + f" - Modalidade: {self.modalidade} - CNPJ: {self.cnpf}"
    
    def retirada(self, valor):
        valor = float(valor)
        print("5 reais de tarifa.")
        if self.saldo - 5 > valor :
            self.saldo = self.saldo - 5 - valor
        else: 
            print("Saldo insuficiente!")

    
if __name__ == "__main__": 
    pf1 = ContaPF("Azuporan", 1500, "homi", "777777")
    print(pf1)

    pf1.set_genero("Blue")
    print(pf1.get_genero())
    pf1.set_CPF("78327823987")
    print(pf1.get_CPF())

    print("Testando o vars --> ",vars(pf1))
    print("Testando o dict --> ", pf1.__dict__)

    pj1 = ContaPJ("Amazon", 1000, "MacroEmpresa", "2342342-23")

    # pj1.set_modalidade("MegaSuperMasterBlasterEmpresa")
    # print(pj1.get_modalidade())
    # pj1.set_cnpj("4242349-00")
    # print(pj1.get_cnpj())

    # print(pj1)

    # print("================================================"*2)
    # pf1.deposito(100)
    # print(pf1)
    # pf1.retirada(1599)
    # pf1.retirada(1597)
    # print(pf1)
    # print("================================================"*2)
    # pj1.retirada(994)
    # print(pj1)
    # print("================================================"*2)

    pf1.set_saldo(1600)
    pf1.retirada_rn2(1596)
    print(pf1)
    pj1.set_saldo(1000)
    pj1.retirada_rn2(994)
    print(pj1)