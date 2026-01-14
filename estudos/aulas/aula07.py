with open("estudos/aulas/ars/aquivo.txt","w") as arquivo:
    arquivo.write("Ola mundo\n")
    arquivo.write("Programa iniciado\n")
    arquivo.write("Tudo funcionando\n")
#importante
try:
    with open("dados.txt", "r") as arquivo:
        print(arquivo.read())
except FileNotFoundError:
    print("Arquivo nao encontrado")
#importante

with open("estudos/aulas/arqs/aquivo.txt","r") as arq:
    conteudo = arq.read()
    print(conteudo)
    
