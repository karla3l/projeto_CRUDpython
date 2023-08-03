from pydantic import BaseModel

class Book(BaseModel):
    
    title: str
    genre: str
    author: str
    
"""     def __init__(self, title, genre, author):
        self.title = title
        self.genre = genre
        self.author = author """
    
        