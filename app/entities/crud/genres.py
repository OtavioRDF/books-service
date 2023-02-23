from sqlalchemy.orm import Session

from app.entities.models import genres
from app.entities.schemas import genres as genres_schema

def create_genre(genre: genres_schema.GenresCreate, db: Session):
    db_genre = genres.Genres(
        books_genres= genre.books_genres
    )
    db.add(db_genre)
    db.commit()
    db.refresh(db_genre)

    return db_genre

def get_genres(genre: str | None, books: str | None, db: Session, page: int = 0, limit: int = 100):
    if genre and books:
        return db.query(genres.Books).filter(genres.Books.genre_name == genre).all()
    
    elif genre:
        return db.query(genres.Genres).filter(genres.Genres.books_genres == genre).all()
    
    skip = 0 
    if page != 1: skip = page * 50
    return db.query(genres.Genres).offset(skip).limit(limit).all()

def get_genre(id: int, db: Session):
    return db.query(genres.Genres).filter(genres.Genres.id == id).first()

def update_genre(genre: genres_schema.GenresUpdate, id: int, db: Session):
    updated_genre = genre.dict(exclude_unset= True)

    db.query(genres.Genres).filter(genres.Genres.id == id).update(updated_genre)
    db.commit()

    return genre

def delete_genre(id: genres_schema.GenresDelete, db: Session):
    genre = db.query(genres.Genres).filter(genres.Genres.id == id).first()
    db.delete(genre)
    db.commit()

    return genre