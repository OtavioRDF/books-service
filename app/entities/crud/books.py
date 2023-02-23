from sqlalchemy.orm import Session

from app.entities.models import books
from app.entities.schemas import books as books_schema

def get_book(id: int, db: Session):
    return db.query(books.Books).filter(books.Books.id == id).first()

def get_books(title: str | None, db: Session, page: int = 1, limit: int = 50):
    if title:
        return db.query(books.Books).filter(books.Books.title == title).first()
    
    skip = 0
    if page != 1: skip = page * 50
    return db.query(books.Books).offset(skip).limit(limit).all()

def create_book(db: Session, book: books_schema.BookCreate):
    genre = db.query(books.Genres).filter(books.Genres.books_genres == book.genre_name).first()

    if genre:
        db_book = books.Books(
            title=book.title,
            author=book.author,
            genre_name=book.genre_name, 
            available= book.available,
            stock= book.stock, 
            release_date= book.release_date 
        )
        db.add(db_book)
        db.commit()
        db.refresh(db_book)

        return db_book
    
    return False  

def update_book(db: Session, book: books_schema.BooksUpdate, book_id: int):
    updated_book = book.dict(exclude_unset= True)
    db.query(books.Books).filter(books.Books.id == book_id).update(updated_book)
    db.commit()

    return book

def delete_book(book_id: books_schema.BooksDelete, db: Session):
    book = db.query(books.Books).filter(books.Books.id == book_id).first()
    db.delete(book)
    db.commit()

    return book