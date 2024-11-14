from config import db, app
from sqlalchemy import text

table_name = "references"

def setup_db():
    pass

if __name__ == "__main__":
    with app.app_context():
      setup_db()