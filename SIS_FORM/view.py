##importando SQLite
import sqlite3 as dblite

#Criando Conexao
con= dblite.connect("dados.db")

lista = ['Joao Futi Muanda','joao@mail.com',123456789,"12/19/2010",'Normal', 'Gostaria de uma Consulta']

#  Inserir Informações
# with con:
#     cur = con.cursor()
#     query = "INSERT INTO formulario(nome, email, telefone, data_em, estado, info) VALUES (?, ?, ?, ?, ?, ?)"
#     cur.execute(query,lista)

# Acessando Informações

with con:
    cur = con.cursor()
    query = "SELECT * FROM formulario"
    cur.execute(query)
    info = cur.fetchall()
    print(info)


# Atualizar Informações
lista = ['joao',1]
with con:
    cur = con.cursor()
    query = "UPDATE formulario SET nome=? WHERE id=?"
    cur.execute(query, lista)

# Deletar Informações
lista = [1]
with con:
    cur = con.cursor()
    query = "DELETE FROM formulario WHERE id=?"
    cur.execute(query, lista)
