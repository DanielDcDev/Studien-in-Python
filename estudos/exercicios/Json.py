import json

CAMINHO = "estudos/aulas/arqs/usuarioExe.json"

def salvar_usuario(nome, idade, email):
    try:
        with open(CAMINHO, "r", encoding="utf-8") as arquivo:
            usuarios = json.load(arquivo)
    except FileNotFoundError:
        usuarios = []

    usuarios.append({
        "nome": nome,
        "idade": idade,
        "email": email
    })

    with open(CAMINHO, "w", encoding="utf-8") as arquivo:
        json.dump(usuarios, arquivo, indent=4, ensure_ascii=False)

    return usuarios


print(salvar_usuario("Daniela", 25, "daniela@gmail.com"))
print(salvar_usuario("Maria", 22, "maria@hotmail.com"))
