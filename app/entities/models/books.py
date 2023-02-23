from sqlalchemy import Boolean, Column, ForeignKey,String, Integer, Date
from sqlalchemy.orm import relationship

from app.entities.database import Base

class Books(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key= True, index= True, autoincrement= True)
    title = Column(String(length= 125), nullable= False)
    author = Column(String(length=30), nullable= False)
    genre_name = Column(String(length= 30), ForeignKey('genres.books_genres', ondelete= 'CASCADE', onupdate='CASCADE'), nullable= False)
    available = Column(Boolean, default= True, nullable= False)
    stock = Column(Integer, nullable= False)
    release_date = Column(Date, nullable= False)
    
    genres = relationship('Genres', back_populates='books')