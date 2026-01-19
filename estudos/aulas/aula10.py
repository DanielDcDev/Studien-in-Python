#bloco2
class Conta:
    def __init__(self, saldo):
        self.__saldo = saldo
    
    def get_saldo(self):
        return self.__saldo
    
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor

#bloco 3 

class Produto:
    imposto  = 0.2

    @classmethod
    def alterar_imposto(cls, novo_valor):
        cls.imposto = novo_valor

# Utilizamos o self quando se trata de um objeto
# Ja o cls utilizamos quando se trata de uma classe inteira

#bloco 4 

class Endereco: 
    def __init__(self, cidade):
        self.cidade = cidade

class Usuario:
    def __init__(self,nome, endereco):
        self.nome = nome
        self.endereco =  endereco




