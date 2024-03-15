from abc import ABC, abstractmethod
class Carro(ABC):
    ct = 0
    precoBase = 100
    def __init__(self, modelo):
        self.modelo = modelo
        Carro.ct += 1
    def get_modelo(self):
        return self.modelo
    def set_modelo(self, novoModelo):
        self.modelo = novoModelo

    @abstractmethod
    def precoDiaria(self):
        pass
    @classmethod
    def get_precoDiaria(self):
        return self.precoDiaria
    @classmethod
    def set_precoDiaria(self, novoPreco):
        self.precoBase = novoPreco

    @classmethod
    def get_qtdCarros(cls):
        return cls.ct

class Economico(Carro):
    def __init__(self, modelo):
        super().__init__(modelo)
    def precoDiaria(self):
        return self.precoBase + (self.precoBase * 0.05)

class Intermediario(Carro):
    def __int__(self, modelo):
        super().__init__(modelo)
    def precoDiaria(self):
        return self.precoBase + (self.precoBase * 0.1)

if __name__ == '__main__':
    Carro1 = Economico("Chevet")
    CarroJ = Intermediario("Gol Bolinha")
    Carro1.set_precoDiaria(180)
    print("Nome do carro: ",Carro1.get_modelo())
    print("Preço do carro: ", Carro1.precoDiaria())
    print(Carro.get_qtdCarros())
    print('+---------------------------------------------------------------------+')
    print("Nome do carro: ", CarroJ.get_modelo())
    print("Preço do carro: ", CarroJ.precoDiaria())

