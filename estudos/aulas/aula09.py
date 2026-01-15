import json
class Usuario:

    ARQUIVO = "/arqs/usuario.json"

    def salvar(self):
        try:
            with open(self.ARQUIVO , "r" , encoding="utf-8") as f:
                usuarios = json.load(f)
        except FileNotFoundError:
            usuarios = []

        usuarios.append({
            "nome": self.nome,
            "idade": self.idade,
            "email": self.email
        })

        with open(self.ARQUIVO, "w", encoding="utf-8") as f:
            json.dump(usuarios, f, indent=4, ensure_ascii=False)


        u1 = Usuario("Daniela", 25, "daniela@gmail.com")
        u1.salvar()

        u2 = Usuario("Maria", 22, "maria@hotmail.com")
        u2.salvar()

print(Usuario.u1)