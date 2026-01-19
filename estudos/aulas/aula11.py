from abc import ABC, abstractclassmethod
# Basico de Heranca  
class Animal:
    def falar(self):
        print("O animal faz um som")

class Cachorro(Animal):
    pass

c = Cachorro()
c.falar()

#Super
#serve para chamar o metodo da classe

class Automoveis:
    def __init__(self, nome):
        self.nome = nome

class Carro(Automoveis):
    def __init__(self, nome):
        super().__init__(nome)
#sem o super vira um codigo duplicada
class Animal1:
    def falar(self):
        print("som generico")
class Cachorro1(Animal1):
    def falar(self):
        print("Latido")
class Gato1(Animal1):
    def falar(self):
        print("Miau")
class Vaca1(Animal1):
    def falar(self):
        print("Moo")
animais = [Cachorro1(), Gato1(), Vaca1()]
for a in animais:
    a.falar()

#Conceito metodo abstrato

class funcionario(ABC):
    @abstractclassmethod
    def calcular_salario(self):
        pass