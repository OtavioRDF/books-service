from pydantic import BaseModel 

class GenresBase(BaseModel):
    books_genres: str 

class GenresCreate(GenresBase):
    pass

class GenresUpdate(GenresBase):
    pass

class GenresDelete(GenresBase):
    pass

class Genres(GenresBase):
    id: int 

    class Config:
        orm_mode = True