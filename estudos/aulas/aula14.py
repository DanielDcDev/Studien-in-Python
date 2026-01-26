from abc import ABC, abstractmethod
class Funcionario(ABC):
    def __init__(self,nome):
        self.nome = nome
    
    @abstractmethod
    def calcular_pagamento(self):
        pass

class PJ(Funcionario):
    def __init__(self, nome, valor_hora, horas):
        super().__init__(nome)
        self.valor_hora = valor_hora
        self.horas = horas

    def calcular_pagamento(self):
        return self.valor_hora * self.horas

 
class CLT(Funcionario):
    def __init__(self, nome, salario, bonus):
        super().__init__(nome)
        self.salario = salario
        self.bonus = bonus

    def calcular_pagamento(self):
        return self.salario + self.bonus

    
funcionarios = [
    CLT("Maiara", 3000, 500),
    PJ("Carol", 80, 160),
    CLT("Joao", 2800, 400)
]

for f in funcionarios:
    print(f"{f.nome} recebe {f.calcular_pagamento()}")

