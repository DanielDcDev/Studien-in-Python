from abc import ABC, abstractmethod

class Transporte(ABC):
    @abstractmethod
    def calcular_frete(self):
        pass

class Caminhao(Transporte):
    def __init__(self, distancia):
        self.distancia = distancia
        self.tipo = 23

    def calcular_frete(self):
        return self.distancia * self.tipo

class Aviao(Transporte):
    def __init__(self, distancia):
        self.distancia = distancia
        self.tipo = 150

    def calcular_frete(self):
        return self.distancia * self.tipo

class Navio(Transporte):
    def __init__(self, distancia):
        self.distancia = distancia
        self.tipo = 220

    def calcular_frete(self):
        return self.distancia * self.tipo

class Entrega:
    def __init__(self, transporte: Transporte):
        self.transporte = transporte

    def calcular(self):
        return self.transporte.calcular_frete()

entrega1 = Entrega(Caminhao(60))
entrega2 = Entrega(Aviao(1532))
entrega3 = Entrega(Navio(254))

print(f"R$ {entrega1.calcular()}")
print(f"R$ {entrega2.calcular()}")
print(f"R$ {entrega3.calcular()}")
