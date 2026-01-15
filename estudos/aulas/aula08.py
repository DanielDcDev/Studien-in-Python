import json

dados = {
    "nome":"Carlos",
    "Idade":25,
    "Skills": ["Python","Git","Linux"]
}
with open("estudos/aulas/arqs/dados.json","w",encoding="utf=8") as arquivo:
    json.dump(dados, arquivo, indent=4, ensure_ascii=False)
try:
    with open("estudos/aulas/arqs/dados.json", "r", encoding="utf=8") as arquivo:
        dados =json.load(arquivo)
except FileNotFoundError:
    dados ={}

#print(dados["nome"])
#9print(dados["Skills"])

def salvar_operacao(operacao, n1,n2):
    try:
        with open("estudos/aulas/arqs/historico.json", "r") as arquivo:
            historico = json.load(arquivo)
    except FileNotFoundError:
        historico = []
        
    historico.append({
        "operacao": operacao,
        "n1": n1,
        "n2": n2,
        "resultado" : n1 + n2
    })

    with open("estudos/aulas/arqs/historico.json", "w") as arquivo:
        json.dump(historico, arquivo, indent=4)


    return historico

print(salvar_operacao("soma",13 ,7,))
