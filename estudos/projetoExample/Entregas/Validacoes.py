import re
def email_valido(email: str) -> bool:
    padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(padrao, email) is not None

def senha_valida(senha):
    return print("metodo nao concluido")

def endereco_valido(endereco):
    return print("metodo nao concluido")
def data_nascimento_valido(dtNascimento):
    return print("metodo nao concluido")
def produto_existe(idProduto):
    #deve retornar se ele existe 
    return print("metodo nao concluido")
def produto_existeA(idProduto):
    #deve retornar tudo do produto_existe mais a quantidade
    return print("metodo nao concluido")
def NenhumProdutoCadastradoError(Exception):
    pass
def validar_catalogo_nao_vazio(produtos):
    if not produtos:
        raise NenhumProdutoCadastradoError()