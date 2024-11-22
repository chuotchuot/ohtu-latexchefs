from config import db
from sqlalchemy import text

#from entities.reference import Reference
#from entities.book import Book

def add_reference(type, title, year, authors, publisher, reference_key, keywords):

    author_str = ", ".join(author for author in authors)
    try:
        sql = text("INSERT INTO reference (title, year, author, publisher, reference_type, reference_key, keywords) VALUES (:title, :year, :author, :publisher, :reference_type, :reference_key, :keywords)")
        db.session.execute(sql, {"title": title, "year": year, "author": author_str, "publisher": publisher, "reference_type": type, "reference_key": reference_key, "keywords": keywords})
        db.session.commit()
    except:
        raise ValueError("Reference key can only contain letters a-z, numbers 0-9 and special characters - and _.")

def fetch_references():
    fetch = db.session.execute(text("SELECT title, year, author, publisher, reference_type  FROM reference"))
    fetched_references = fetch.fetchall()
    return fetched_references

def delete_reference(id: int) -> None:
    sql = text("DELETE FROM reference WHERE id = :id")
    db.session.execute(sql, {"id": id})
    db.session.commit()