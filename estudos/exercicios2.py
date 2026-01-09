def nivel1(nome="Usuario"):
    print(f"Ola, {nome}!")
nivel1("Carlos")

def nivel2(*numeros):
    return sum(numeros)
print(nivel2(1, 2, 3, 4))

def nivel3(*numeros):
    return max(numeros)
print(nivel3(1,2,3,12,65,344,23,656,8,545))

quadrado = lambda x:x *x
print(quadrado(20))