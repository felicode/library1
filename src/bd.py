#Base de Dados connection

import mysql.connector as mariadb

#conectar a BD

db = mariadb.connect(
        user="root",
        password="",
        host="localhost",
        port="3306",
        database=""
    )
c = db.cursor() # c = cursor

#criar BD 'ipluso_escola'

try:
    c.execute("create database ipluso_escola")
except:
    pass
    #print("BD ja existe")


#conectar a BD ipluso_escola

db = mariadb.connect(
        user="root",
        password="",
        host="localhost",
        port="3306",
        database="ipluso_escola"
    )

c = db.cursor()  # c = cursor

#criar tabelas (disciplinas, alunos e professores)


try:
    c.execute("create table disciplinas ( nome varchar(100) )")
    #print("Tabela disciplinas criada")
except:
        pass
    #print("Tabela disciplinas já existe")

try:
    c.execute("create table alunos ( nome varchar(100), apelido_aluno varchar(100), num_aluno varchar(100) )")
    #print("Tabela alunos criada")
except:
        pass
    #print("tabela alunos já existe")
    
try:
    c.execute("create table professores ( nome varchar(100), apelido_prof varchar(100), num_prof varchar(100) )")
    #print("Tabela professores criada")
except:
        pass
    #print("Tabela professores já existe")


#em caso de testar ou editar, aoenas tirar comentarios

#apagar disciplinas pelo o nome

"""
name = 'TesteDisciplina'
query = f"delete from disciplinas where nome = '{name}' "

c.execute(query)
db.commit()
"""

#dropar tabelas

"""
query = "drop table disciplinas"
c.execute(query)
db.commit()
"""

#dropar database

"""
query = "drop database ipluso_escola"
c.execute(query)
db.commit()
"""

#inserir valores

"""
nome_aluno = 'Teste'
sql = f"insert into alunos (nome) values ('{nome_aluno}')"
c.execute(sql)
db.commit()
"""

#print das linhas

"""
c.execute("select * from disciplinas")

for x in c:
        print(x)
"""

#mostar base de dados existentes

"""
try:
    c.execute("show databases")

    for x in c:
            print(x)
except:
        print("Ja existe")
"""
