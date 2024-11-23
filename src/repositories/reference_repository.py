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
    fetch = db.session.execute(text("SELECT id, title, year, author, publisher, reference_type, reference_key, keywords FROM reference"))
    fetched_references = fetch.fetchall()
    return fetched_references

def fetch_reference(id: int):
    sql = text("SELECT id, title, year, author, publisher, reference_type, reference_key, keywords FROM reference WHERE id = :id LIMIT 1")
    fetch = db.session.execute(sql, {"id": id})
    fetched_reference = fetch.fetchone()
    return fetched_reference

def delete_reference(id: int) -> None:
    sql = text("DELETE FROM reference WHERE id = :id")
    db.session.execute(sql, {"id": id})
    db.session.commit()

def edit_reference(id: int, title: str, year: int, authors: list[str], publisher: str, reference_key: str, keywords: str) -> None:
    author_str = ", ".join(author for author in authors)
    try:
        sql = text("UPDATE reference SET title = :title, year = :year, author = :author, publisher = :publisher, reference_key = :reference_key, keywords = :keywords WHERE id = :id")
        db.session.execute(sql, {"title": title, "year": year, "author": author_str, "publisher": publisher, "reference_key": reference_key, "keywords": keywords, "id": id})
        db.session.commit()
    except:
        raise ValueError("Reference key can only contain letters a-z, numbers 0-9 and special characters - and _.")
    