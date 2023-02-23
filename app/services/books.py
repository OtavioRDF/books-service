from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from app.utils.deps import get_db
from app.entities.schemas.books import Books, BookCreate, BooksUpdate, BooksDelete
from app.entities.crud import books as crud_books

router = APIRouter()

@router.get("/read", response_model= Books | list[Books], status_code=200)
def list_books(title: str | None = None, page: int = 1, limit: int = 50, db: Session = Depends(get_db)):
    books = crud_books.get_books(title, db, page= page, limit= limit)
    if books:
        return books
    
    raise HTTPException(
        status_code=404, 
        detail= f"No book with this title: {title} found",
        headers={"404": "Not found"}
    )

@router.post("/create", status_code=201)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    if crud_books.create_book(db, book) == False:
        raise HTTPException(
            status_code=406,
            detail= "Is not possible insert a book with a non existent genre",
            headers= {"406": "Not Acceptable"}
        )
    
    return crud_books.create_book(db, book)

@router.put("/{book_id}/update", response_model= BooksUpdate, status_code=200)
def update_book(book_id: int, book: BooksUpdate, db: Session = Depends(get_db)):
    db_book = crud_books.get_book(book_id, db)
    
    if db_book:
        return crud_books.update_book(db, book, book_id)

    raise HTTPException(
        status_code=404, 
        detail= f"No book with this id: {book_id} found",
        headers={"404": "Not found"}
    )

@router.delete("/{book_id}/delete", response_model= BooksDelete, status_code=200)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = crud_books.get_book(book_id, db)

    if book:
        return crud_books.delete_book(book_id, db)
    
    raise HTTPException(
        status_code=404, 
        detail= f"No book with this id: {book_id} found",
        headers={"404": "Not found"}
    )