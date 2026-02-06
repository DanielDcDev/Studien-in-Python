    #proxima meta, criar interface para receber as variaveis de teste 
from Validacoes import validar_catalogo_nao_vazio, NenhumProdutoCadastradoError
class Produto:
    _proximo_id = 1
    def __init__(self, nome, preco, quantidade, peso):
        self._id = Produto._proximo_id
        Produto._proximo_id += 1
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        self.quantidade_de_vendas = 0
        self.peso = peso

    @property
    def id(self):
        return self._id
    
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

class CatalogoProdutos:
    produtos = {}

    @classmethod
    def _validar_nao_vazio(cls):
        if not cls.produtos:
            raise NenhumProdutoCadastradoError()
    
    @classmethod
    def buscar_por_id(cls,id_produto):
        return cls.produtos.get(id_produto)
    
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

    @classmethod
    def modificar_produto(cls,id_produto,nome = None,preco = None,quantidade = None, peso = None):
        produto = cls.produtos.get(id_produto)

        if not produto:
            raise ValueError("Produto nao encontrado")
        
        if nome is not None:
            produto.nome = nome
        if preco is not None:
            produto.preco = preco
        if quantidade is not None:
            produto.quantidade = quantidade
        if peso is not None:
            produto.peso = peso
        
    @classmethod
    def deletar_produto(cls, id_produto):
 #So quem pode deletar e o Administrador
        if id_produto not in cls.produtos:
            raise ValueError("Produto nao encontrado")
        del cls.produtos[id_produto]           
    
    @classmethod
    def mostrar_todos_produtos(cls):
        try:
            for produto in cls.produtos.values():
                print(
                    f"ID: {produto.id} |"
                    f"Nome: {produto.nome} |"
                    f"Preco: {produto.preco} |"
                    f"Quantidade: {produto.quantidade}|"
                    f"Peso: {produto.peso}"
                )
        except NenhumProdutoCadastradoError:
            print("nenhum produto Cadastrado")

    @classmethod
    def reduzir_estoque(cls,id_produto, quantidade):
        produto = cls.buscar_por_id(id_produto)
        if not produto:
            raise ValueError("Produto nao encontrado")
        
        if produto.quantidade <quantidade:
            raise ValueError("Estoque insuficiente")
        
        produto.quantidade -= quantidade



class CatalogoPedidos:
    pedidos = {}

    @classmethod
    def adicionar_pedido(cls,pedido ):
      #  cls.pedidos[Pedidos.id] = Pedidos
        pass
        

class Cliente:
    _proximo_id = 1

    def __init__(self,nome, senha,email,dataNascimento,endereco):
        self.id = Cliente._proximo_id
        Cliente._proximo_id += 1 
        self.nome = nome
        self.senha = senha 
        self.email = email
        self.dataNascimento = dataNascimento
        self.endereco = endereco

class Entregadores:
    _proximo_id =1

    def __init__(self,nome,loginEntre,senhaEntre,qtdEntre):
        self.id = Entregadores._proximo_id
        Entregadores._proximo_id +=1
        self.nome = nome
        self.loginEntregador = loginEntre
        self.senhaEntregador = senhaEntre
        self.quantidadeEntregas = qtdEntre

    @property
    def id(self):
        return self._id


p1 = Produto("Carro", 12000,12, 500)
p2 = Produto("Cacanique", 1000,10,47)

CatalogoProdutos.adicionar(p1)
CatalogoProdutos.adicionar(p2)

CatalogoProdutos.mostrar_todos_produtos()
