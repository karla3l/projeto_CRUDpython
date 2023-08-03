from fastapi import FastAPI
import controllers.book_controller as controller
import models.book as books
import config.sql_functions as sqlfun

class Routers:
    
    def __init__(self):
        self.app = FastAPI()
        sqlfun.create_table()
        
    def crud_routers(self):
        
        @self.app.post("/book/create")
        def create_book(book: books.Book ):
            controller.create_book(book)
            return ('message: Sucessfully created')
        
        @self.app.get("/book/list")
        def list_books(): 
            return controller.list_books()
         
        @self.app.put("/book/update/{id}")   
        def update_books(id: int, book: books.Book):
            controller.update_books(id, book)
            return {'message': 'Book updated'}
         
        @self.app.delete("/book/delete/{id}")    
        def delete_book(id: int):
            controller.delete_book(id)
            return {'message': 'Book deleted'}