import sqlite3

conn = sqlite3.connect("example.db")
cursor = conn.cursor()

cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)",
(31, "Alice")) 

conn.commit()