#importando SQLite
import sqlite3 as dblite

#Criando Conexao
con= dblite.connect("dados.db")

# criando tabela
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE formulario(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, email TEXT, telefone TEXT, data_em DATE, estado TEXT, info TEXT)")