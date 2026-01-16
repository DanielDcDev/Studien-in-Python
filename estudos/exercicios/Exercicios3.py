import json


class Produto:
    CAMINHO = "estudos/arqs/ProdutosEX3.json"

    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def salvar(self):
        produtos = Produto.carregar()
        
        try:
            with open(self.CAMINHO, "r", encoding="utf-8") as arq:
                produtos = json.load(arq)

                # garantia extra
                if not isinstance(produtos, list):
                    produtos = []

        except (FileNotFoundError, json.JSONDecodeError):
            produtos = []

        produtos.append({
            "nome": self.nome,
            "preco": self.preco,
            "quantidade": self.quantidade
        })


        with open(self.CAMINHO, "w", encoding="utf-8") as arq:
            json.dump(produtos, arq, indent=4, ensure_ascii=False)
    
    def valor_total(self):
        #multiplicar o valor pela quantidade
        return self.preco * self.quantidade
    
    @staticmethod
    def carregar():
        try:
            with open(Produto.CAMINHO, "r", encoding="utf-8") as arq:
                return json.load(arq)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
        
    @staticmethod
    def listar():
        try:
            with open(Produto.CAMINHO, "r", encoding="utf-8") as arq:
                produtos = json.load(arq)
                if not isinstance(produtos, list):
                    return []
                return produtos
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    @staticmethod
    def buscar_por_nome(nome):
        produtos = Produto.listar()
        for produto in produtos:
            if produto["nome"].lower() == nome.lower():
                return produto
        return None

    @staticmethod
    def deletar(nome):
        produtos = Produto.listar()

        novos_produtos = [
            p for p in produtos
            if p["nome"].lower() != nome.lower()
            ]

        if len(produtos) == len(novos_produtos):
            return False
        with open(Produto.CAMINHO, "w", encoding="utf-8") as arq:
            json.dump(novos_produtos, arq, indent=4, ensure_ascii= False)
         
        return True
    
    def if_exist_delete(nome):
        if Produto.deletar(nome):
            print("Produto removido com sucesso")
        else:
            print("Produto nao encontrado")

    @staticmethod
    def produto_achado_if(produto):
        if produto:
            print("Produto encontrado:",produto)
        else:
            print("Produto nao encontrado")

    @staticmethod
    def limpar():
        with open(Produto.CAMINHO, "w", encoding="utf-8") as arq:
            json.dump([], arq, indent=4, ensure_ascii=False)
        return "Todos os produtos foram removidos"

    @staticmethod
    def limpar_Robusto(confirmar=False):
        if confirmar:
            with open(Produto.CAMINHO, "w", encoding="utf-8") as arq:
                json.dump([], arq, indent=4, ensure_ascii=False)


p1 = Produto("Carro", 12000, 3)
p1.salvar()
p2 = Produto("casa", 120000, 2)
p2.salvar()
p3 = Produto("Iphone 17", 1200, 12)
p3.salvar()

print(f"{p1.nome} - Total: {p1.valor_total()}")
print(f"{p2.nome} - Total: {p2.valor_total()}")
print(f"{p3.nome} - Total: {p3.valor_total()}")

#for p in Produto.listar():
   #print(p)

produto = Produto.buscar_por_nome("carro")
Produto.produto_achado_if(produto)

Produto.if_exist_delete("")

#Produto.limpar()
Produto.limpar(confirmar=False)




