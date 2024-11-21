import sqlite3 as sql

con = sql.connect ('form_db.db')
cur = con.cursor()
cur.execute('DROP TABLE IF EXISTS users')

sql = '''CREATE TABLE "users" (
    "ID" INTEGER PRIMARY KEY AUTOINCREMENT,
    "NOME" TEXT,
    "IDADE" TEXT,
    "ENDEREÇO" TEXT,
    "NUMERO" TEXT,
    "CIDADE" TEXT,
    "ESTADO" TEXT,
    "EMAIL" TEXT
)'''

cur.execute(sql)
con.commit()#o commit registra os dados
con.close()