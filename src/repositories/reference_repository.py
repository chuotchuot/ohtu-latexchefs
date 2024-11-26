from sqlalchemy import text
from config import db
import bibtexparser
from bibtexparser.bibdatabase import BibDatabase

#from entities.reference import Reference
#from entities.book import Book

def add_reference(ref_type, title, year, authors, publisher, reference_key, keywords):
    author_str = ", ".join(author for author in authors)

    if check_unique_reference_key(reference_key):
        try:
            sql = text("INSERT INTO reference (title, year, author, publisher, reference_type, "
                       "reference_key, keywords) VALUES (:title, :year, :author, :publisher, "
                       ":reference_type, :reference_key, :keywords)")
            db.session.execute(sql, {"title": title, "year": year, "author": author_str,
                                     "publisher": publisher, "reference_type": ref_type,
                                     "reference_key": reference_key, "keywords": keywords})
            db.session.commit()
        except Exception as exc:
            raise ValueError("Reference key can only contain letters a-z, numbers 0-9 and "
                         "special characters '-', '_' or ':'.") from exc
    else:
        raise ValueError("Reference key has to be unique. Try using another reference key")

def fetch_references():
    fetch = db.session.execute(text("SELECT title, year, author, publisher, "
                                    "reference_type, reference_key, keywords FROM reference"))
    fetched_references = fetch.fetchall()
    
    bibtex_string_lista = []
    for i in fetched_references:
        bibtex_string_lista.append(create_bibtex_string(i))

    return fetched_references, bibtex_string_lista

def create_bibtex_string(kirja):
    bibdb = BibDatabase()
    bibdb.entries = []
    temp = {    'author': kirja.author,
                'title': kirja.title,
                'year': str(kirja.year),
                'ID': kirja.reference_key,
                'keyword': kirja.keywords,
                'ENTRYTYPE': kirja.reference_type,}#add publisher
    bibdb.entries.append(temp)
    string = bibtexparser.dumps(bibdb)
    return string




def fetch_reference(ref_id: int):
    sql = text("SELECT id, title, year, author, publisher, reference_type, reference_key, "
               "keywords FROM reference WHERE id = :id LIMIT 1")
    fetch = db.session.execute(sql, {"id": ref_id})
    fetched_reference = fetch.fetchone()
    return fetched_reference

def delete_reference(ref_id: int) -> None:
    sql = text("DELETE FROM reference WHERE id = :id")
    db.session.execute(sql, {"id": ref_id})
    db.session.commit()

def edit_reference(ref_id: int, title: str, year: int, authors: list[str], publisher: str,
                   reference_key: str, keywords: str) -> None:
    author_str = ", ".join(author for author in authors)
    try:
        sql = text("UPDATE reference SET title = :title, year = :year, author = :author, "
                   "publisher = :publisher, reference_key = :reference_key, "
                   "keywords = :keywords WHERE id = :id")
        db.session.execute(sql, {"title": title, "year": year, "author": author_str,
                                 "publisher": publisher, "reference_key": reference_key,
                                 "keywords": keywords, "id": ref_id})
        db.session.commit()
    except Exception as exc:
        raise ValueError("Reference key can only contain letters a-z, numbers 0-9 and "
                         "special characters '-', '_' or ':'.") from exc

def check_unique_reference_key(reference_key):

    sql = text("SELECT NOT EXISTS ("
               "    SELECT 1 FROM reference"
               "    WHERE reference_key = :reference_key"
               ") AS unique")
    result = db.session.execute(sql, {"reference_key":reference_key}).fetchone()
    db.session.commit()

    return result.unique
