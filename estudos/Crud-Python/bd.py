import sqlite3 as lite

#criando conexao
con = lite.connect('dados.db')

#criando tabelas

with con:
    cur = con.cursor()
    cur.execute("" \
    "CREATE TABLE formulario(id INTEGER PRIMARY KEY AUTOINCREMENT ," \
    "nome text," \
    "email TEXT," \
    "telefone TEXT," \
    "dia_em DATE," \
    "estado_consulta TEXT," \
    "assunto TEXT)")
