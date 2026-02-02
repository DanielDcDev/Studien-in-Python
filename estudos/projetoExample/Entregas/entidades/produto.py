class Produto:
 #esta classe nos so queremos criar o produto, para que depois possamos fazer dele a classe pai dos pedidos
    def __init__(self, id, nome, preco, quantidade):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

class Pedidos:
    def __init__(self, produto :Produto.nome, distancia, tipoEntrega):
        self.produto = Produto.nome
        