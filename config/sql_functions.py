import sqlite3


def create_table():
    conn = sqlite3.connect("files/library.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS book
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       title VARCHAR NOT NULL,
                       genre VARCHAR NOT NULL,
                       author VARCHAR NOT NULL)''')
    conn.commit()
    conn.close()