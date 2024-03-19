"""
Home for our models
See schema at -filename-


Rollin Salsbery
3/8/2024
"""
from datetime import date, timedelta
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import ForeignKey, String, Date
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
#from sqlalchemy.ext.associationproxy import AssociationProxy, association_proxy
from typing import List, Optional

class Base(DeclarativeBase):
    pass

db = SQLAlchemy()


class LibraryBooks(db.Model):
    __tablename__ = 'libraries_books_table'

    library_id: Mapped[int] = mapped_column(ForeignKey("library.id"), primary_key=True)
    book_id: Mapped[int] = mapped_column(ForeignKey("book.id"), primary_key=True)
    book: Mapped["Book"] = relationship(back_populates='libraries')
    library: Mapped["Library"] = relationship(back_populates='book_inventory')
    copies: Mapped[int]
    available_copies: Mapped[int]

    def serialize_book(self):
        return {
            "id": self.book_id,
            "book": self.book.title,
            "available_copies": self.available_copies,
            "copies": self.copies
        }


class ReadersBooks(db.Model):
    __tablename__ = 'readers_books_table'

    reader_id: Mapped[int] = mapped_column(ForeignKey("reader.id"), primary_key=True)
    book_id: Mapped[int] = mapped_column(ForeignKey("book.id"), primary_key=True)
    book: Mapped["Book"] = relationship(back_populates='readers')
    reader: Mapped["Reader"] = relationship(back_populates='books_checked_out')
    checked_out_date: Mapped[date] = mapped_column(default=date.today)
    due_date: Mapped[date] = mapped_column(default=date.today() + timedelta(days=21))
    library_id = mapped_column(ForeignKey("library.id"))




class Book(db.Model):
    __tablename__ = "book"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    genre: Mapped[Optional[str]]
    book_format: Mapped[str]
    published_year: Mapped[int]

    author_id = mapped_column(ForeignKey("author.id"))
    author: Mapped["Author"] = relationship(back_populates="books_written")
    libraries: Mapped[List["LibraryBooks"]] = relationship(back_populates="book")
    readers: Mapped[List["ReadersBooks"]] = relationship(back_populates='book')
    reviews: Mapped[List["Review"]] = relationship(back_populates="book")

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author.name,
            'author_id': self.author_id,
            'genre': self.genre,
            'format': self.book_format,
            'published_year': self.published_year,
        }



class Author(db.Model):
    __tablename__ = "author"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    bio: Mapped[Optional[str]]

    books_written: Mapped[Book] = relationship(back_populates="author")

    def serialize(self):
        return {
            'name': self.name,
            'bio': self.bio,
        }


class Library(db.Model):
    __tablename__ = "library"

    id: Mapped[int] = mapped_column(primary_key=True)
    branch_name: Mapped[str]
    location: Mapped[str]

    book_inventory: Mapped[List["LibraryBooks"]] = relationship(back_populates="library")

    def serialize(self):
        return {
            'branch name': self.branch_name,
            'location': self.location
        }


class Profile(db.Model):
    """
    Profile should not be accessed directly thru API. Reader is 1-to-1 proxy
    """
    __tablename__ = "profile"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    library_card: Mapped[str] = mapped_column(String(15))
    username: Mapped[str]
    password: Mapped[str]

    reader_id: Mapped[int] = mapped_column(ForeignKey("reader.id"))
    reader: Mapped["Reader"] = relationship(back_populates="profile")


  

class Reader(db.Model):
    __tablename__ = "reader"

    id: Mapped[int] = mapped_column(primary_key=True)
    profile: Mapped["Profile"] = relationship(back_populates="reader")
    reviews: Mapped[List["Review"]] = relationship(back_populates="reviewer")
    books_checked_out: Mapped[List["ReadersBooks"]] = relationship(back_populates="reader")
    

    def serialize(self):
        return {
            'username': self.profile.username
        }


class Review(db.Model):
    __tablename__ = "review"

    id: Mapped[int] =  mapped_column(primary_key=True)
    rating: Mapped[Optional[str]]
    review_body: Mapped[Optional[str]]

    reviewer_id = mapped_column(ForeignKey("reader.id"))
    reviewer: Mapped[Reader] = relationship(back_populates="reviews")

    book_id = mapped_column(ForeignKey("book.id"))
    book: Mapped[Book] = relationship(back_populates="reviews")

    def serialize(self):
        return {
            'rating': self.rating,
            'review_body': self.review_body,
            'reviewer': self.reviewer.profile.username,
            'review_id': self.reviewer_id,
            'book': self.book.title,
            'book_id': self.book_id
        }
