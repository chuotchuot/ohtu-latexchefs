import re
import random
from sqlalchemy import text
import bibtexparser
from doi2bib.crossref import get_bib
from config import db
from entities.reference import Reference
from entities.output import Output

def save_reference(reference: Reference):

    reference.format_fields_with_multiple_values()

    if check_unique_reference_key(reference.reference_key):
        try:
            sql = text("INSERT INTO reference (title, year, authors, publisher, editors, "
                       "booktitle, reference_type, journal, volume, page, number, month, "
                       "howpublished, note, reference_key, keywords) VALUES (:title, :year, "
                       ":authors, :publisher, :editors, :booktitle, :reference_type, "
                       ":journal, :volume, :page, :number, :month, :howpublished, :note, "
                       ":reference_key, :keywords)")
            db.session.execute(sql, {"title": reference.title,
                                     "year": reference.year,
                                     "authors": reference.authors,
                                     "publisher": reference.publisher,
                                     "editors": reference.editors,
                                     "booktitle":reference.booktitle,
                                     "reference_type": reference.reference_type,
                                     "journal": reference.journal,
                                     "volume": reference.volume,
                                     "page": reference.page,
                                     "number": reference.number,
                                     "month": reference.month,
                                     "howpublished": reference.howpublished,
                                     "note": reference.note,

                                     "reference_key": reference.reference_key, 
                                     "keywords": reference.keywords})
            db.session.commit()
        except Exception as exc:
            raise ValueError("Reference key can only contain letters a-z, numbers 0-9 and "
                         "special characters '-', '_' or ':'.") from exc
    else:
        raise ValueError("Reference key has to be unique. Try using another reference key")

def get_ref_info_with_doi(doi):
    _,bibtex_data = get_bib(doi)

    parser = bibtexparser.bparser.BibTexParser()
    bibdb = bibtexparser.loads(bibtex_data, parser)

    entry = bibdb.entries[0]

    return entry

def fetch_references():
    fetch = db.session.execute(text("SELECT id, title, year, authors, publisher, editors, journal, "
                                    "booktitle, page, volume, number, month, howpublished, "
                                    "note, reference_type, reference_key, keywords FROM reference"))

    fetched_references = fetch.fetchall()
    bibtex_string_list = []
    readable_string_list = []

    for reference in fetched_references:
        output = Output(reference)
        output.set_id(reference.id)
        bibtex_string_list.append(output.create_bibtex_string())
        readable_string_list.append(output.create_readable_string())

    return readable_string_list, bibtex_string_list

def fetch_filtered_references(query):
    sql = text("""SELECT * FROM reference WHERE
                title LIKE :query
                OR title LIKE :query
                OR year LIKE :query
                OR authors LIKE :query
                OR publisher LIKE :query
                OR editors LIKE :query
                OR journal LIKE :query
                OR booktitle LIKE :query
                OR page LIKE :query
                OR volume LIKE :query
                OR number LIKE :query
                OR month LIKE :query
                OR howpublished LIKE :query
                OR note LIKE :query
                OR reference_type LIKE :query
                OR reference_key LIKE :query
                OR keywords LIKE :query""")
    fetch = db.session.execute(sql,{"query":"%"+query+"%"})
    fetched_references = fetch.fetchall()
    bibtex_string_list = []
    readable_string_list = []

    for reference in fetched_references:
        output = Output(reference)
        output.set_id(reference.id)
        bibtex_string_list.append(output.create_bibtex_string())
        readable_string_list.append(output.create_readable_string())

    return readable_string_list, bibtex_string_list

def fetch_reference_keys():
    fetch = db.session.execute(text("SELECT reference_key FROM reference"))
    fetched_keys = fetch.scalars().all()
    return fetched_keys

def fetch_one_reference(ref_id: int):
    sql = text("SELECT id, title, year, authors, publisher, editors, journal, "
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

def edit_reference(reference_id, reference: Reference) -> None:
    reference.format_fields_with_multiple_values()
    try:
        sql = text("UPDATE reference SET title = :title, year = :year, authors = :authors, "
                "publisher = :publisher, editors = :editors, booktitle = :booktitle, page = :page, "
                "journal = :journal, number = :number, howpublished = :howpublished,"
                "month = :month, note = :note, keywords = :keywords WHERE id = :id")

        db.session.execute(sql, {"title": reference.title,
                                "year": reference.year,
                                "authors": reference.authors,
                                "publisher": reference.publisher,
                                "editors": reference.editors,
                                "booktitle": reference.booktitle,
                                "journal": reference.journal,
                                "page": reference.page,
                                "number": reference.number,
                                "month": reference.month,
                                "howpublished": reference.howpublished,
                                "note": reference.note,
                                "keywords": reference.keywords,
                                "id": reference_id})
        db.session.commit()
    except Exception as exc:
        raise ValueError("There was an issue with updating reference values") from exc

def check_unique_reference_key(reference_key: str) -> bool:
    if reference_key == "":
        return False
    sql = text("SELECT NOT EXISTS ("
               "    SELECT 1 FROM reference"
               "    WHERE reference_key = :reference_key"
               ") AS unique")
    result = db.session.execute(sql, {"reference_key":reference_key}).fetchone()
    db.session.commit()

    return result.unique

def generate_reference_key(reference: Reference) -> str:
    regex: str = r"[^a-zA-Z0-9\-:_]"

    reference_key: str = ""
    title: str = ""
    if reference.title != "":
        title = reference.title
    elif reference.booktitle != "":
        title = reference.booktitle

    if title != "":
        titleStr: str = ""
        array: list[str] = reference.title.split(" ")
        wordCount: int = min(len(array), 3)
        for i in range(wordCount):
            if array[i].lower() == "the" and i == 0:
                continue
            titleStr += array[i]
            if i + 1 != wordCount:
                titleStr += "-"
        reference_key += titleStr

    if reference.year != "":
        reference_key += f"-{reference.year}"

    reference_key = re.sub(regex, "", reference_key)

    if check_unique_reference_key(reference_key):
        return reference_key

    additional: list[str] = []

    if reference.journal != "":
        additional.append(reference.journal)

    if reference.authors != "":
        authors: list[str] =  [re.sub(regex, "", author) for author in reference.authors.split(";")]
        for author in authors:
            additional.append(author)

    if reference.publisher != "":
        additional.append(reference.publisher)

    for addition in additional:
        reference_key += f"-{addition}"
        if check_unique_reference_key(reference_key):
            break

    reference_key = re.sub(regex, "", reference_key)

    while not check_unique_reference_key(reference_key):
        reference_key += str(random.randint(0,9))

    return reference_key
