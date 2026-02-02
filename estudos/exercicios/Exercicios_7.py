
from abc import ABC, abstractmethod
class Transporte():
    @abstractmethod
    def calcular_frete(self):
        return self.distancia*self.tipo
class Caminhao(Transporte):
    def __init__(self,distancia,tipo):
        self.distancia = distancia
        self.tipo = tipo
        
    def calcular_frete(self):
        return super().calcular_frete(self.distancia,self.tipo)
    
caminhao1 = Caminhao(12,1)
print(caminhao1.calcular_frete())
