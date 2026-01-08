from datetime import datetime

from estatisticas import maior
from estatisticas import menor
from estatisticas import media
from estatisticas import filtroDuplo

from calculos import soma
from calculos import diminuicao
from calculos import vezes

numeros = [3, 9, 15, 20, 1, 4]
def main():
    print("Executando programa")
    print("Maior:", maior(numeros))
    print("Menor:", menor(numeros))
    print("Media:", media(numeros))
    filtroDuplo(1, 4, 7, 9, 12, 15, 20, 22)
    print("calculos: ")
    print(soma(1,2))
    print(diminuicao(5,4))
    print(vezes(17,4))

    agora = datetime.now()
    formatada = agora.strftime("%d/%m/%Y %H:%M:%S")
    print("Agracedemos o uso do codigo \n"+formatada)

if __name__ == "__main__":
    main()