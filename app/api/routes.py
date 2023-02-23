from fastapi import APIRouter

from app.services import books, genres

api_router = APIRouter()

api_router.include_router(books.router, prefix="/books", tags=["books"])
api_router.include_router(genres.router, prefix="/genres", tags=["genres"])