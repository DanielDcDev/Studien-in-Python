def maior(valores):
    return max(valores)

def menor(valores):
    return min(valores)

def media(valores):
    if not valores:
        return 0
    return sum(valores) / len(valores)

def filtroDuplo(*numeros):
    numeros = [1, 4, 7, 9, 12, 15, 20, 22]
    pares = [n for n in numeros if n > 5 and n % 3 == 0]
    print("numeros pares:")
    print(pares)