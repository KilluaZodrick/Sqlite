import sqlite3

banco = sqlite3.connect('banco.db')

cursor = banco.cursor()

#cursor.execute("CREATE TABLE pessoas (nome text, idade integer, email text)")

""" cursor.execute("INSERT INTO pessoas VALUES('',,'')")

banco.commit() """
cursor.execute("SELECT * FROM pessoas")
print(cursor.fetchall())