#Exercicios
class ContaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        return self.__saldo

    def sacar(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
            return self.__saldo
        else:
            print("Saldo insuficiente")
            return self.__saldo

    def get_saldo(self):
        return self.__saldo


# TESTE
conta = ContaBancaria(1000)

print("Saldo inicial:", conta.get_saldo())
print("Apos deposito:", conta.depositar(200))
print("Apos saque:", conta.sacar(300))

# SEGUNDO EXERCICIO

class Funcionario:
    aumento = 1.1  # atributo de classe

    def __init__(self, salario):
        self.salario = salario

    @classmethod
    def alterar_aumento(cls, novo_valor):
        cls.aumento = novo_valor

    def calc_salario(self):
        return self.salario * Funcionario.aumento


# TESTE
f1 = Funcionario(1000)

print("Salario atual:", f1.calc_salario())

Funcionario.alterar_aumento(1.2)

print("Salario com aumento:", f1.calc_salario())
# TERCEIRO EXERCICIO
class Endereco:
    def __init__(self, cidade, pais):
        self.__cidade = cidade
        self.__pais = pais 

    def mostrar_cidade(self):
        return self.__cidade

    def mostrar_pais(self):
        return self.__pais


class Pessoa:
    def __init__(self, nome, endereco):
        self.__nome = nome
        self.__endereco = endereco  # objeto Endereco

    def mostrar_dados(self):
        return (
            f"Nome: {self.__nome}\n"
            f"Cidade: {self.__endereco.mostrar_cidade()}\n"
            f"Pais: {self.__endereco.mostrar_pais()}"
        )


# TESTE
e1 = Endereco("Santarem", "Portugal")
p1 = Pessoa("Mateus", e1)

print(p1.mostrar_dados())