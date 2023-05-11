import sqlite3 as sql

con = sql.connect('form_db.db') # definindo o nome do banco de dados
cur = con.cursor() # definindo o cursor
cur.execute('DROP TABLE IF EXISTS users') #se existir alguma tabela usuário, ele irá fazer o drop dela

sql = '''CREATE TABLE "users" (
    "ID" INTEGER PRIMARY KEY AUTOINCREMENT,
    "NOME" TEXT,
    "IDADE" TEXT,
    "ENDERECO" TEXT,
    "CIDADE" TEXT,
    "NUMERO" TEXT,
    "ESTADO" TEXT,
    "EMAIL" TEXT
    )'''

cur.execute(sql)
con.commit() # commit registra os dados
con.close() # close serve para fechar o banco de dados
