from  abc import ABC,abstractmethod
class Veiculo(ABC):
    def __init__(self, nome, gasolina):
        self.nome = nome
        self.gasolina = gasolina

    @abstractmethod
    def calcular_consumo(self):
        pass

class Carro(Veiculo):
    def calcular_consumo(self):
        return self.gasolina  * 10
    
class Moto(Veiculo):
    def calcular_consumo(self):
        return self.gasolina * 25
    

Veiculos = [
    Moto("Honda CBX", 20),
    Carro("Mitsubichi",25),
    Moto("BMW CB500", 34)
]

for f in Veiculos:
    print(f.nome, "-", f.calcular_consumo())