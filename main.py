import sqlite3

conn = sqlite3.connect("example.db")
cursor = conn.cursor()

# Criando uma tabela
cursor.execute("""CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER    
)""")

conn.commit()