import sqlite3 as sq

with sq.connect("example.db") as con:
    cur = con.cursor()
    
    cur.execute("""CREATE TABLE  IF NOT EXISTS example(
        user_id INTEGER PRIMARY KEY  AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL
        )""")
        
        