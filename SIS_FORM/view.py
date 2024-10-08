##importando SQLite
import sqlite3 as dblite

#Criando Conexao
con= dblite.connect("dados.db")

#lista = ['Joao Futi Muanda','joao@mail.com',123456789,"12/19/2010",'Normal', 'Gostaria de uma Consulta']

#  Inserir Informações
def inserir_info(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO formulario(nome, email, telefone, data_em, estado, info) VALUES (?, ?, ?, ?, ?, ?)"
        cur.execute(query,i)

# item = [2,3,4,5,6,7]
# inserir_info(item)
# inserir_info(item)
# inserir_info(item)
# inserir_info(item)


# Acessando Informações
def mostrar_info():
    lista = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM formulario"
        cur.execute(query)
        info = cur.fetchall()
        print(info)
        for i in info:
            lista.append(i)
    return lista


# Atualizar Informações
def update_info(i):
    #i = ['Joao Muanda','joao3@mail.com',123456789,"12/19/2010",'Normal', 'Gostaria de uma Consulta 4'] 
    #i = ['joao',2]
    print(i)
    with con:
        cur = con.cursor()
        #query = "UPDATE formulario SET nome=? WHERE id=?"
        
        query = "UPDATE formulario SET nome=?, email=?, telefone=?, data_em=?, estado=?, info=? WHERE id=?"
        cur.execute(query, i)

# Deletar Informações
def delete_info(i):
    i = [i]
    print(i)
    with con:
        cur = con.cursor()
        query = "DELETE FROM formulario WHERE id=?"
        cur.execute(query, i)
