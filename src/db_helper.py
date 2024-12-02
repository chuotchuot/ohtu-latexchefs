from sqlalchemy import text
from config import db, app

TABLE_NAME = "reference"

def table_exists(name):
    sql = text(
        "SELECT EXISTS ("
        "   SELECT 1"
        "   FROM information_schema.tables"
        f"   WHERE table_name = '{name}'"
        ")"
    )

    print(f"Checking if table {name} exists")

    result = db.session.execute(sql)
    db.session.commit()
    return result.fetchall()[0][0]

def setup_db():
    if table_exists(TABLE_NAME):
        print(f"Table {TABLE_NAME} exist. Dropping existing table")
        sql = text(f"DROP TABLE {TABLE_NAME}")
        db.session.execute(sql)
        db.session.commit()

    print(f"Creating table {TABLE_NAME}")
    sql = (text(
        f"CREATE TABLE {TABLE_NAME} ("
        "   id SERIAL PRIMARY KEY,"
        "   title TEXT NOT NULL,"
        "   author TEXT,"
        "   year INT,"
        "   publisher TEXT,"
        "   editor TEXT,"
        "   journal TEXT,"
        "   booktitle TEXT,"
        "   page TEXT,"
        "   volume TEXT,"
        "   number TEXT,"
        "   month TEXT,"
        "   howpublished TEXT,"
        "   note TEXT,"
        "   reference_type TEXT NOT NULL,"
        "   reference_key TEXT NOT NULL UNIQUE"
        "       CONSTRAINT valid_ref_key CHECK (reference_key ~ '^[a-zA-Z0-9_:-]*$'),"
        "   keywords TEXT,"
        "   CONSTRAINT type_constraint CHECK"
            "(" 
            "(reference_type = 'book' "
                "AND author IS NOT NULL "
                "AND year IS NOT NULL "
                "AND publisher IS NOT NULL "
                "AND editor IS NOT NULL) "
            "OR (reference_type = 'article' "
                "AND author IS NOT NULL "
                "AND year IS NOT NULL "
                "AND journal IS NOT NULL) "
            "OR (reference_type = 'inbook' "
                "AND author IS NOT NULL "
                "AND year IS NOT NULL "
                "AND publisher IS NOT NULL "
                "AND booktitle IS NOT NULL) "
            "OR (reference_type = 'misc'"
                "AND howpublished IS NOT NULL)"
            "))"
        ))
    db.session.execute(sql)
    db.session.commit()

def reset_db():
    print(f"Clearing contents from table {TABLE_NAME}")
    sql = text(f"DELETE FROM {TABLE_NAME}")
    db.session.execute(sql)
    db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        setup_db()
