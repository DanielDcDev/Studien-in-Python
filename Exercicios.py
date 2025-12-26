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

def filtrarPalavrasGrandes():
    palavras = ["sol", "elefante", "ar", "computador", "mar"]
    grandes = [p for p in palavras if len(p) > 3]
    print(grandes)

def filtrarPalavrasGrandesFuncao(palavras):
    return [p for p in palavras if len(p) > 3]

def dicionarioNotas():
    notas = {"Ana": 8.5, "Lucas": 7.0, "Marcos": 5.0,"Daniela": 8.7,"Carolina": 10.0}  
    
    for nome, nota in notas.items():
        print(f"{nome} tirou {nota}")

def classificaNumeros():
    pares = [n for n in range(50) if n % 2 == 0]
    print(pares)

def filtroDuplo():
    numeros = [1, 4, 7, 9, 12, 15, 20, 22]
    pares = [n for n in numeros if n > 5 and n % 3 == 0]
    print(pares)
    
def estatistica():
   valores = [3, 9, 15, 20, 1, 4] 
   maior = max(valores)
   menor = min(valores)
   media = sum(valores) / len(valores)
   print("Maior valor:", maior)
   print("Menor valor:", menor)
   print("Media:", media)


#parImpar(11)
#loop(10)
#listaFrutos()
#enumerates()
#soma()
#filtro()
#filtrarPalavrasGrandes()
#dicionarioNotas()
#classificaNumeros()
#filtroDuplo()
estatistica()