from db_helper import setup_db
from config import app
from entities.reference import Reference
from repositories.reference_repository import save_reference, generate_reference_key

if __name__ == "__main__":
    with app.app_context():
        setup_db()

        print("Setting test inbook reference")
        inbook_reference: Reference = Reference()
        inbook_reference.title = "Python Unit Test Automation"
        inbook_reference.booktitle = "Test Automation Tools and Frameworks"
        inbook_reference.authors = "Eugen Kiss"
        inbook_reference.year = "2020"
        inbook_reference.reference_type = "inbook"
        inbook_reference.publisher = "Academia.edu"
        inbook_reference.reference_key = generate_reference_key(inbook_reference)
        save_reference(inbook_reference)

        print("Setting test misc reference")
        misc_reference: Reference = Reference()
        misc_reference.title = "Lean Testing: Or Why Unit Tests Are Worse Than You Think"
        misc_reference.howpublished = "WebPage"
        misc_reference.year = "2021"
        misc_reference.authors = "Eugen Kiss"
        misc_reference.reference_type = "misc"
        misc_reference.reference_key = generate_reference_key(misc_reference)
        save_reference(misc_reference)
