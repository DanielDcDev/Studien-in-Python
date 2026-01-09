from calculos import soma
from calculos import diminuicao
from calculos import vezes
from calculos import divisao

try:
    n1= int(input("Digite um valor:"))
    n2= int(input("Digite um valor:"))
    opc = int(input("qual opcao deseja usar:\nSoma = 1\nSubtracao = 2\nMultiplicacao = 3\nDivisao = 4 "))
    match opc:
        case 1:
            print(soma(n1,n2))
        case 2:
            print(diminuicao(n1,n2))
        case 3:
            print(vezes(n1,n2)) 
        case 4:
            print(divisao(n1,n2))
        case _:
            print("Opcao in")
except TypeError:
    print("Erro: entrada inválida")