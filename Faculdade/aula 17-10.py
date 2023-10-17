class Veiculo:
    def __init__(self, valor, modelo, km = 1):
        self.valor = valor
        self.modelo = modelo 
        self.km = km
        
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
    def set_km(self, novo_km):
        self.km = novo_km
        
    def __str__(self):
        return f"Valor - {self.valor} / Modelo - {self.modelo} / Km - {self.km}"
    
    def acrescenta(self, valor):
        if valor <= 0:
            print("valor inserido não permitido!")
        else:
            self.valor += valor
        
    def acrescemta_pct(self, pct):
        self.valor += pct/100 * self.valor
        
class Carro(Veiculo):
    def __init__(self, valor, modelo, km=1, qnt_portas = 4):
        super().__init__(valor, modelo, km)
        self.qnt_portas = qnt_portas
        
    def __str__(self):
        return super().__str__() + f"Qnt_Portas - {self.qnt_portas}"
        
class Moto(Veiculo):
    def __init__(self, valor, modelo, km=1, cilindradas = 150):
        super().__init__(valor, modelo, km)
        self.cilindradas = cilindradas
        
    def __str__(self):
        return super().__str__() + f"Cilindradas - {self.cilindradas}"
        
if __name__ == "__main__":
    carro1 = Carro(300.000, "Honda Civic Type R", 0)
    carro2 = Carro(10.000, "Celta 2010", 314.000, 2)
    carro3 = Carro(100.000, "Evoque Prata", 120.000, 4)
    print(carro1)
    print(carro2)
    print(carro3)
    moto1 = Moto(15.000, "XRE", 15.000, 500)
    moto2 = Moto(25.000, "Hornet", 0)
    print(moto1)
    print(moto2)
    print("Utilizando o vars --> ", vars(carro1))
    print("Utilizando o dict --> ", carro1.__dict__)
    carro1.acrescenta(20)
    print(carro1.valor)
    carro1.acrescenta(0)
    carro1.acrescemta_pct(5)
    print(carro1.valor)