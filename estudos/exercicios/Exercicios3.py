import json

class Produto:
    CAMINHO = "estudos/arqs/ProdutosEX3.json"

    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def salvar(self):
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

p1 = Produto("Carro", 12000, 3)
p1.salvar()