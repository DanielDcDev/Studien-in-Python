def dividir(a,b):
    try:
        return a / b
    except ZeroDivisionError:
        raise ValueError("Nao e possivel dividir por zero")
    

def else_finally():
    try:
        x = int("10")
    except ValueError:
        print("Erro")
    else:
        print("Tudo certo")
    finally:
        print("Sempre executa")
#Finally e bom pois fecha o arquivo, libera conexao e serve de cleanup

class SaldoInsuficienteError(Exception):
    pass

class ContaBancaria:
    def sacar(self, valor):
        if valor > self.saldo:
            raise SaldoInsuficienteError("Saldo Insuficiente")
        

class ProdutoNaoEncontradoError(Exception):
    pass
class Produto:

    def __init__(self, produtos):
        self.produtos = produtos

    def buscar(self, nome):
        for p in self.produtos:
            if p["nome"].lower() == nome.lower():
                return p 
            raise ProdutoNaoEncontradoError(f"Produto '{nome}' nao encontrado")
        
lista = [
    {"nome": "Carro", "preco": 10000},
    {"nome": "Casa", "preco": 500000}
]

p = Produto(lista)

try:
    print(p.buscar("carro"))
    print(p.buscar("aviao"))
except ProdutoNaoEncontradoError as e:
    print(e)
