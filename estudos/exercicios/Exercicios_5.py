#aula 11


class Veiculo:
    def __init__(self, marca, portas):
        self.morca = marca
        self.portas = portas

    def mover(self):
        print("Andando")

class Carro(Veiculo):
    def mover(self):
        print("110 kmh")

    def __init__(self, marca, portas):
        super().__init__(marca, portas)

class Moto(Veiculo):
    def mover(self):
        print("100 kmh")
    def __init__(self, marca, portas):
        super().__init__(marca, portas)

veiculos = [Carro("citroem", 4), Moto("Honda",0)]

for a in veiculos:
    a.mover()


from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, salario):
        self.salario = salario

    @abstractmethod
    def calcular_salario(self):
        pass

class CLT(Funcionario):
    def calcular_salario(self):
        return self.salario * 1.1  # 10% aumento


class PJ(Funcionario):
    def calcular_salario(self):
        return self.salario * 1.3  # 30% aumento
    

funcionarios = [
    CLT(1000),
    PJ(1000)
]

for f in funcionarios:
    print(f.calcular_salario())