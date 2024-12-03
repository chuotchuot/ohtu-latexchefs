from sqlalchemy import text
from bibtexparser.bibdatabase import BibDatabase
import bibtexparser
from config import db

#from entities.reference import Reference
#from entities.book import Book

def add_reference(inputs):
    author_str = " and ".join(author for author in inputs["authors"])
    keywords_str = ", ".join(keyword for keyword in inputs["keywords"])
    editors_str = " and ".join(editor for editor in inputs["editors"])


    if check_unique_reference_key(inputs["ref_key"]):
        try:
            sql = text("INSERT INTO reference (title, year, author, publisher, editor, booktitle, "
                       "reference_type, journal, volume, page, number, month, howpublished, note, "
                       "reference_key, keywords) VALUES (:title, :year, "
                       ":author, :publisher, :editor, :booktitle, :reference_type, "
                       ":journal, :volume, :page, :number, :month, :howpublished, :note, "
                       ":reference_key, :keywords)")
            db.session.execute(sql, {"title": inputs["title"],
                                     "year": inputs["year"],
                                     "author": author_str,
                                     "publisher": inputs["publisher"],
                                     "editor": editors_str,
                                     "booktitle": inputs["booktitle"],
                                     "reference_type": inputs["ref_type"],
                                     "journal": inputs["journal"],
                                     "volume": inputs["volume"],
                                     "page": inputs["page"],
                                     "number": inputs["number"],
                                     "month": inputs["month"],
                                     "howpublished": inputs["howpublished"],
                                     "note": inputs["note"],

                                     "reference_key": inputs["ref_key"], 
                                     "keywords": keywords_str})
            db.session.commit()
        except Exception as exc:
            raise ValueError("Reference key can only contain letters a-z, numbers 0-9 and "
                         "special characters '-', '_' or ':'.") from exc
    else:
        raise ValueError("Reference key has to be unique. Try using another reference key")

def create_input_dictionary():
    inputs = {}
    inputs["ref_type"] = ""
    inputs["title"] = ""
    inputs["year"] = ""
    inputs["authors"] = ""
    inputs["publisher"] = ""
    inputs["editors"] = ""
    inputs["booktitle"] = ""
    inputs["journal"] = ""
    inputs["volume"] = ""
    inputs["page"] = ""
    inputs["number"] = ""
    inputs["month"] = ""
    inputs["howpublished"] = ""
    inputs["note"] = ""
    inputs["ref_key"] = ""
    inputs["keywords"] = ""
    return inputs

def fetch_references():
    fetch = db.session.execute(text("SELECT id, title, year, author, publisher, editor, journal, "
                                    "booktitle, page, volume, number, month, howpublished, "
                                    "note, reference_type, reference_key, keywords FROM reference"))
    fetched_references = fetch.fetchall()
    bibtex_string_list = []
    readable_string_list = []
    for i in fetched_references:
        bibtex_string_list.append({"id":i.id,"text":create_bibtex_string(i)})
        readable_string_list.append({"id":i.id,"text":create_readable_string(i)})

    return readable_string_list, bibtex_string_list

def create_bibtex_instance(current_reference):
    bibtex_dict = {
        "ENTRYTYPE" : str(current_reference.reference_type),
        "ID"        : str(current_reference.reference_key)
    }
    reference_values = ["title","author","year","publisher","editor",
                        "journal","booktitle","page","volume","number",
                        "month","howpublished","note","keywords"]
    for value in reference_values:
        if getattr(current_reference, value):
            bibtex_dict[value] = str(getattr(current_reference, value))
    #print(bibtex_dict["author"])
    bibtex_dict = bibtex_seperate_multiple(bibtex_dict)
    return bibtex_dict

def bibtex_seperate_multiple(bibtex_dict):
    if "author" in bibtex_dict:
        bibtex_dict["author"] = bibtex_dict["author"].replace(" and "," and \n          ")
        #menee rikki jos authorina " and "
    if "keywords" in bibtex_dict:
        bibtex_dict["keywords"] = bibtex_dict["keywords"].replace(", ",",\n             " )
        #menee rikki jos keywordina ", "
        #vois muuttaa databasee ettei voi mennä rikki
    return bibtex_dict

def create_bibtex_string(current_reference):
    bibdb = BibDatabase()
    bibdb.entries = []
    bibdb.entries.append(create_bibtex_instance(current_reference))
    string = bibtexparser.dumps(bibdb)
    return string

def create_readable_string(reference):
    temp = {    'title': reference.title,
                'author': reference.author,
                'year': str(reference.year),
                'publisher': reference.publisher,
                'editor': reference.editor,
                'booktitle': reference.booktitle,
                'journal': reference.journal,
                'volume': reference.volume,
                'page': reference.page,
                'number': reference.number,
                'month': reference.month,
                'howpublished': reference.howpublished,
                'note': reference.note,
                }
    string = ""
    for i in temp.values():
        if i and string == "":
            string += i
        elif i:
            string += f", {i}"
    return string


def fetch_reference(ref_id: int):
    sql = text("SELECT id, title, year, author, publisher, editor, journal, "
               "booktitle, page, volume, number, month, howpublished, "
               "note, reference_type, reference_key, keywords "
               "FROM reference WHERE id = :id LIMIT 1")
    fetch = db.session.execute(sql, {"id": ref_id})
    fetched_reference = fetch.fetchone()
    return fetched_reference

def delete_reference(ref_id: int) -> None:
    sql = text("DELETE FROM reference WHERE id = :id")
    db.session.execute(sql, {"id": ref_id})
    db.session.commit()

def edit_reference(ref_id: int, inputs: dict) -> None:
    author_str = " and ".join(author for author in inputs["authors"])
    keywords_str = ", ".join(keyword for keyword in inputs["keywords"])
    editors_str = " and ".join(editor for editor in inputs["editors"])

    try:
        sql = text("UPDATE reference SET title = :title, year = :year, author = :author, "
                "publisher = :publisher, editor = :editor, booktitle = :booktitle, "
                "reference_key = :reference_key, "
                "keywords = :keywords WHERE id = :id")
        db.session.execute(sql, {"title": inputs["title"],
                                "year": inputs["year"],
                                "author": author_str,
                                "publisher": inputs["publisher"],
                                "editor": editors_str,
                                "booktitle": inputs["booktitle"],
                                "reference_type": inputs["ref_type"],
                                "reference_key": inputs["ref_key"],
                                "keywords": keywords_str,
                                "id": ref_id})
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
