from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from app.utils.deps import get_db
from app.entities.schemas.genres import Genres, GenresCreate, GenresUpdate, GenresDelete
from app.entities.crud import genres as crud_genres

router = APIRouter()

@router.post("/create", response_model= GenresCreate, status_code=201)
def create_genre(genre: GenresCreate, db: Session = Depends(get_db)):
    return crud_genres.create_genre(genre, db)

@router.get("/read", response_model= list[Genres],status_code=200)
def list_genres(genre: str | None = None, books: str | None = None, page: int = 1, limit: int = 50, db: Session = Depends(get_db)):
    genres = crud_genres.get_genres(genre, books, db, page= page, limit= limit)
    
    if genres:
        return genres
    
    raise HTTPException(
        status_code=404, 
        detail="genre not found", 
        headers={"404": "Not found"}
    )

@router.put("/{genre_id}/update", response_model= GenresUpdate, status_code=200)
def update_genre(genre_id: int, genre: GenresUpdate, db: Session = Depends(get_db)):
    db_genre = crud_genres.get_genre(genre_id, db)
    
    if db_genre:
        return crud_genres.update_genre(genre, genre_id, db)

    raise HTTPException(
        status_code=404, 
        detail= f"No genre with this id: {genre_id} found",
        headers={"404": "Not found"}
    )

@router.delete("/{genre_id}/delete", response_model= GenresDelete, status_code=200)
def delete_genre(genre_id: int, db: Session = Depends(get_db)):
    genre = crud_genres.get_genre(genre_id, db)

    if genre:
        return crud_genres.delete_genre(genre_id, db)
    
    raise HTTPException(
        status_code=404, 
        detail= f"No book with this id: {genre_id} found",
        headers={"404": "Not found"}
    )