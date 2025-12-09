def parImpar(num):
    if num % 2 == 0:
        print('par')
    else:
        print('impar')

def loop(i):
    for i in range(10 ,0 ,-1):
        print(i)

def listaFrutos():
    frutas = ["maca","banana","uva","pera"]
    for i in frutas:
        print(i)

def enumerates():
    frutas = ["maca","banana","uva","pera"]
    for i, fruta in enumerate(frutas):
        print(i, fruta)

def soma():
    n = int(input("Primeiro numero: "))
    n1 = int(input("Segundo numero: "))
    res = n+n1
    print(res)

def filtro():
    numeros = [1, 4, 7, 9, 12, 15, 20, 22]
    pares = [numeros for numeros in range(20) if numeros % 2 == 0]
    print(pares)


#parImpar(11)
#loop(10)
#listaFrutos()
#enumerates()
#soma()
#filtro()
