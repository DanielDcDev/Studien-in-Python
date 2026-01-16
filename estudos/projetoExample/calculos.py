def soma(n,n1):
    res = n+n1
    return res

def diminuicao(n,n1):
    res = n-n1
    return res

def vezes(n,n1):
    res = n*n1
    return res
def divisao(n,n1):
    try:
        res = n/n1
        return res
    except ZeroDivisionError:
        return "Erro: divisão por zero"








