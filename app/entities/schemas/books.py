from pydantic import BaseModel 
from datetime import date

class BooksBase(BaseModel):
    title: str
    author: str
    genre_name: str
    release_date: date
    available: bool
    stock: int

class BookCreate(BooksBase):
    pass

class BooksDelete(BooksBase):
    title: str

class BooksUpdate(BooksBase):
    title: str | None
    genre_name: str | None
    release_date: date | None
    available: bool | None
    stock: int | None

class Books(BooksBase):
    id: int

    class Config:
        orm_mode = True