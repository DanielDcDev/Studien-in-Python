#Crie:
#Classe Pagamento com método pagar()
#Classes:
#CartaoCredito
#Pix
#Boleto
#Classe Pedido que usa um pagamento (composição)

from abc import ABC, abstractmethod

class Pagamento(ABC):
    @abstractmethod
    def pagar(self):
        pass

class CartaoCredito(Pagamento):
    def pagar(self):
        print("Pagamento realizado com Cartao de Credito")

class Pix(Pagamento):
    def pagar(self):
        print("Pagamento realizado via Pix")

class Boleto(Pagamento):
    def pagar(self):
        print("Pagamento realizado com Boleto")

class Pedido:
    def __init__(self, pagamento: Pagamento):
        self.pagamento = pagamento

    def finalizar(self):
        self.pagamento.pagar()

pedido1 = Pedido(Pix())
pedido2 = Pedido(CartaoCredito())
pedido3 = Pedido(Boleto())

pedido1.finalizar()
pedido2.finalizar()
pedido3.finalizar()
