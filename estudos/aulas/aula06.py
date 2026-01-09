def calculadora_soma(n1,n2):
    try:
        return n1 + n2
    except TypeError:
        print("Entrada invalida")
        return None
    
def calculadora_sub(n1,n2):
    try:
        return n1 - n2
    except TypeError:
        print("Entrada invalida")
        return None
def calculadora_mult(n1,n2):
    try:
        return n1 * n2
    except TypeError:
        print("Entrada invalida")
        return None
def calculadora_div(n1,n2):
    try:
        try:
            return n1 / n2
        except ZeroDivisionError:
            print("valor invalido")
            return None
    except TypeError:
        print("Entrada invalida")
        return None
#Melhor pratica 
#def calculadora_div(n1, n2):
#    try:
#        return n1 / n2
#    except ZeroDivisionError:
#        print("Erro: divisão por zero")
#    except TypeError:
#        print("Erro: entrada inválida")
    
print(calculadora_soma("a",2))
print(calculadora_sub(3,2))
print(calculadora_mult(3,5))
print(calculadora_div(10,5))

