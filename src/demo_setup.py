from db_helper import setup_db
from config import app
from entities.reference import Reference
from repositories.reference_repository import save_reference, generate_reference_key

if __name__ == "__main__":
    with app.app_context():
        setup_db()
        reference1: Reference = Reference()
        reference1.title = "Test Title"
        reference1.authors = "Author"
        reference1.year = "2024"
        reference1.reference_type = "book"
        reference1.publisher = "Publisher"
        reference1.reference_key = generate_reference_key(reference1)
        save_reference(reference1)
