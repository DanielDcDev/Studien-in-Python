#proxima meta, criar interface para receber as variaveis de teste 

class Produto:
    _proximo_id = 1
    def __init__(self, nome, preco, quantidade):
        self.id = Produto._proximo_id
        Produto._proximo_id += 1
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        self.quantidade_de_vendas = 0

    def vendido_quantidade(self, quantidade=1):
        self.quantidade_de_vendas += quantidade
    @property
    def id(self):
        return self._id

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
    _proximo_id = 1
    def __init__(self, id_produto):
        if not CatalogoProdutos.existe(id_produto):
            raise ValueError("Produto nao existe")
        self.idProduto = Pedidos._proximo_id
        Pedidos._proximo_id += 1
        self.produto = CatalogoProdutos.produtos[id_produto]
        self.tipo_entrega = None
        self.distancia = None


class Cliente:
    _proximo_id = 1

    def __init__(self,nome, senha,email,dataNascimento,endereco):
        self.nome = nome
        self.senha = senha 
        self.email = email
        self.dataNascimento = dataNascimento
        self.endereco = endereco
        