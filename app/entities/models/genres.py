from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from app.entities.database import Base

class Genres(Base):
    __tablename__ = 'genres'
    
    id = Column(Integer, primary_key= True,  index= True, autoincrement= True)
    books_genres = Column(String(length= 30), unique= True, index= True)
    
    books = relationship('Books', back_populates='genres', cascade= 'save-update, delete')