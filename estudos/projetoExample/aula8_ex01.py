from datetime import datetime
def hora():
    agora = datetime.now()
    formatada = agora.strftime("%d/%m/%Y %H:%M:%S\n")
    return formatada
try:
    with open("projetoExample/log.txt","a") as al8ex1:
        al8ex1.write("Programa iniciado\n")
        al8ex1.write(hora())
        al8ex1.write("Programa finalizado\n")
    with open("projetoExample/log.txt", "r") as arq:
        print(arq.read())
except FileNotFoundError:
    print("Arquivo nao encontrado")


