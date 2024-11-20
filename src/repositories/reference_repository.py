from config import db
from sqlalchemy import text

#from entities.reference import Reference
#from entities.book import Book

def add_reference(type, title, year, authors, publisher, reference_key, keywords):

    author_str = ", ".join(author for author in authors)

    sql = text("INSERT INTO reference (title, year, author, publisher, reference_type) VALUES (:title, :year, :author, :publisher, :reference_type)")
    db.session.execute(sql, {"title": title, "year": year, "author": author_str, "publisher": publisher, "reference_type": type, "reference_key": reference_key, "keywords": keywords})
    db.session.commit()

def fetch_references():
    fetch = db.session.execute(text("SELECT title, year, author, publisher, reference_type  FROM reference"))
    fetched_references = fetch.fetchall()
    return fetched_references