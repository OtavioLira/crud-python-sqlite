import sqlite3

conn = sqlite3.connect("example.db")
cursor = conn.cursor()

cursor.execute("DELETE FROM users WHERE name = ?",
("Alice")) 

conn.commit()