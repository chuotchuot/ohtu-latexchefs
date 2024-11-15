from config import db
from sqlalchemy import text

#from entities.reference import Reference
#from entities.book import Book

def add_reference(type, title, year, authors, publisher):

    author_str = ", ".join(author for author in authors)

    sql = text("INSERT INTO reference (title, year, author, publisher, reference_type) VALUES (:title, :year, :author, :publisher, :reference_type)")
    db.session.execute(sql, {"title": title, "year": year, "author": author_str, "publisher": publisher, "reference_type": type})
    db.session.commit()