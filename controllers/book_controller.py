import sqlite3
import models.book as books

def create_book(book: books.Book):
    conn = sqlite3.connect("files/library.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO book (title, genre, author) VALUES (?,?,?)", (book.title, book.genre, book.author))
    conn.commit()
    conn.close()
    
def list_books():
    conn = sqlite3.connect("files/library.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM book")
    books = cursor.fetchall()
    conn.close()
    return books

def update_books(id, book):
    conn = sqlite3.connect("files/library.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE book SET title =?, genre =?, author =? WHERE id =?", (book.title, book.genre, book.author, id))
    conn.commit()
    conn.close()
    
def delete_book(id):
    conn = sqlite3.connect("files/library.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM book WHERE id =?", (id,))
    conn.commit()
    conn.close()
    
