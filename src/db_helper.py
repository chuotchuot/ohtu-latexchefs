from config import db, app
from sqlalchemy import text

table_name = "reference"

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
    if table_exists(table_name):
       print(f"Table {table_name} exist. Dropping existing table")
       sql = text(f"DROP TABLE {table_name}")
       db.session.execute(sql)
       db.session.commit()
    
    print(f"Creating table {table_name}")
    sql = (text(
        f"CREATE TABLE {table_name} ("
        "   id SERIAL PRIMARY KEY," 
        "   title TEXT,"
        "   author TEXT," 
        "   year INT," 
        "   publisher TEXT," 
        "   editor TEXT,"
        "   reference_type TEXT,"
        "   reference_key TEXT,"
        "   keywords TEXT"
        ")"
        ))
    db.session.execute(sql)
    db.session.commit()

def reset_db():
    print(f"Clearing contents from table {table_name}")
    sql = text(f"DELETE FROM {table_name}")
    db.session.execute(sql)
    db.session.commit()

if __name__ == "__main__":
    with app.app_context():
      setup_db()