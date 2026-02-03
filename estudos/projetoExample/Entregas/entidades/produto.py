#proxima meta, criar interface para receber as variaveis de teste 

class Produto:
    def __init__(self, id, nome, preco, quantidade):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        self.quantidade_de_vendas = 0

    def vendido_quantidade(self, quantidade=1):
        self.quantidade_de_vendas += quantidade

class CatalogoProdutos:
    produtos = {}

    @classmethod
    def adicionar(cls, produto):
        cls.produtos[produto.id] = produto

    @classmethod
    def existe(cls, id_produto):
        return id_produto in cls.produtos

    @classmethod
    def mostrar(cls, id_produto):
        produto = cls.produtos.get(id_produto)
        if produto:
            print(f"Nome: {produto.nome}")
            print(f"Preco: {produto.preco}")
        else:
            print("Produto nao encontrado")



class Pedidos:
    def __init__(self, id_produto):
        if not CatalogoProdutos.existe(id_produto):
            raise ValueError("Produto nao existe")

        self.produto = CatalogoProdutos.produtos[id_produto]
        self.tipo_entrega = None
        self.distancia = None





p1 = Produto(1, "teclado", 70, 29)
p2 = Produto(2, "mouse", 50, 21)

CatalogoProdutos.adicionar(p1)
CatalogoProdutos.adicionar(p2)

pedido = Pedidos(1)

CatalogoProdutos.mostrar(1)
CatalogoProdutos.mostrar(2)
