import math
from abc import ABC, abstractmethod

def linha():
    print('-' * 60)

class FormaGeometrica(ABC):
    ct = 0

    def __init__(self):
     FormaGeometrica.ct += 1

    @classmethod
    def get_qtd_formas(cls):
        return cls.ct

    @abstractmethod
    def area(self):
        ...

    @abstractmethod
    def perimetro(self):
        pass

    def msg(self):
        print('Mensagem fixa >>> cu')
        v = self
        print("questao 20", v)
        v = self.__class__
        print("questao 21", v)
        v = self.__class__.__name__
        print("questao 22", v)

class Quadrado(FormaGeometrica):
    def  __init__(self,lado):
        super().__init__()
        self.lado = lado

    def get_lado(self):
        return self.lado

    def set_lado(self, novo_lado):
        self.lado = novo_lado

    def perimetro(self, lado):
        return self.lado * 4

    def area(self, lado):
        self.lado * self.lado

class Circulo(FormaGeometrica):
    def __init__(self, raio):
        super().__init__()
        self.raio = raio

    def get_raio(self):
        return self.raio

    def set_raio(self, novoRaio):
        self.raio = novoRaio

    def perimetro(self, raio):
        return 2 * math.pi * self.raio

    def area(self):
        return "{:.2f}".format(math.pi * pow(self.raio, 2))

if __name__ == '__main__':
    objetoQuadrado = Quadrado(3)
    objetoCirculo = Circulo(12)
    print("Lado:", objetoQuadrado.get_lado())
    linha()
    objetoQuadrado.set_lado(2)
    print('Lado:', objetoQuadrado.get_lado())
    linha()
    print("Area:", objetoCirculo.area())
    objetoCirculo.msg()
    print(FormaGeometrica.get_qtd_formas())