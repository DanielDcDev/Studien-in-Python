#Argumentos padrão
def saudacao(nome="Daniel"):
    print(f"Ola, {nome}")
saudacao()
saudacao("Lucas")
#args
def soma(*numeros):
    return sum(numeros)
print(soma(1,2,3,4,5,6))
#Kwargs
def dados(**info):
    for chave, valor in info.items():
        print(chave, ":", valor)
dados(nome="Ana", idade=22, cidade="SP")
dados(nome="Carlos", idade=40, cidade="BA")
#lambda
dobro = lambda x:x *2
print(dobro(1))
#escopo de variavel
x = 10
def teste():
    x = 5 
    print(x)
teste()
print(x)
#modificando variavel global
def alterar():
    global x
    x = 20 

alterar()
print(x)


