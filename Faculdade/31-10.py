class Veiculo(object):      
    qtd_veiculos = 0

    def __init__(self, valor, modelo, km=0):  
        self.valor = valor                   
        self.modelo = modelo
        self.km = km
        Veiculo.qtd_veiculos+=1
    def get_valor(self):                    
        return self.valor
    def set_valor(self, novo_valor):          
        self.valor = novo_valor
    def get_modelo(self):
        return self.modelo
    def set_modelo(self, novo_modelo):
        self.modelo = novo_modelo
    def get_km(self):
        return self.km
    def set_km(self, nova_km):
        self.km = nova_km
    
    @classmethod #Pega a quantidade de objetos criados! 
    def get_qtd_veiculos(self):
        return self.qtd_veiculos
    
    def atualiza_valor(self, vlr_aumento):       
        if vlr_aumento > 0:
            self.valor += vlr_aumento
        else:
            print('Erro: valor negativo.')
    def atualiza_valor_pct(self, pct):
        if pct > 0:
            self.valor = self.valor + self.valor * pct / 100
        else:
            print('Erro: porcentagem negativa.')

    def situacao(self):
        if self.km == 0:
            print("Veiculo zero km!")
        elif self.km <= 20000:
            print("Veiculo semi-novo!")
        else:
            print("Veiculo usado!")

    def situacao2(self):
        if isinstance(self, Moto):
            if self.km == 0:
                print("Moto zero km!")
            elif self.km <= 20000:
                print("Moto semi-nova!")
            else:
                print("Moto usada!")
        elif isinstance(self, Carro):
            if self.km == 0:
                print("Carro zero km!")
            elif self.km <= 1000:
                print("Carro semi-novo!")
            else:
                print("Carro usado!")

    def ipva(self):
        if isinstance(self, Carro):
            x = (3/100 * self.valor) + 100
        if isinstance(self, Moto):
            x = (2/100 * self.valor) 

class Carro(Veiculo):      
    def __init__(self, valor, modelo, km=0, qtd_portas=4):
        super().__init__(valor, modelo, km)  
        self.qtd_portas = qtd_portas
    def get_qtd_portas(self):
        return self.qtd_portas
    def set_qtd_portas(self, nova_qtd):
        self.qtd_portas = nova_qtd
    def __str__(self):                      
        s = f"Valor: {self.valor:.2f}, modelo: {self.modelo}, " \
            f"Km: {self.km}, qtd. portas: {self.qtd_portas}"
        return s


class Moto(Veiculo):          
    def __init__(self, valor, modelo, km=0, cilindradas=0):  
        super().__init__(valor, modelo, km) 
        self.cilindradas = cilindradas
    def get_cilindradas(self):
        return self.cilindradas
    def set_cilindradas(self, novo_valor):
        self.cilindradas = novo_valor


if __name__ == '__main__':
    c1 = Carro(300000.0, "BMW MK3", 10, 4)
    c2 = Carro(100000.0, "Hilux 2012", 314500)
    c3 = Carro(15000, "Audi a3")
    m1 = Moto(10000, "XRE", 100000.0, 150)
    m2 = Moto(40000, "BMW MOTO ZIKA", 14)

    c3.atualiza_valor(5000)
    print("Novo valor:", c3.get_valor())
    c3.atualiza_valor_pct(10)
    print("Valor com porcentagem a mais: ", c3.get_valor())

    print("-"*80)

    c3.situacao2()
    m1.situacao2()
    c2.situacao()
    m2.situacao()

    print("Total de objetos criados: ",Veiculo.get_qtd_veiculos())