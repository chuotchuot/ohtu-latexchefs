import unittest
from entities.reference import Reference
from repositories import reference_repository

class TestReferenceInput(unittest.TestCase):

    def setUp(self):

        self.test_book_dict = {
            "ENTRYTYPE": "book",
            "ID": "PyUnitTest-17",
            "title": "Python Unit Test Automation",
            "author": "Ashwin Pajankar",
            "year": "2017",
            "publisher": "Berkeley, CA : Apress : Imprint: Apress",
            "editor": "Joku random"
        }

        self.test_author_and_keyword_dict = {
            "ENTRYTYPE": "book",
            "ID": "PyUnitTest-17",
            "title": "Python Unit Test Automation",
            "author": "Ashwin Pajankar and Pashwin Ajankar",
            "year": "2017",
            "publisher": "Berkeley, CA : Apress : Imprint: Apress",
            "editor": "Joku random",
            "keywords": "Testing, Automation"
        }

        self.test_book = Reference(
            "Python Unit Test Automation",
            "book",
            "PyUnitTest-17",
            "2017",
            "Ashwin Pajankar",
            "Berkeley, CA : Apress : Imprint: Apress",
            "Joku random"
        )

    def test_creating_bibtex_string(self):
        # Fix weird formatting without breaking the test
        test_string = """@book{PyUnitTest-17,
 author = {Ashwin Pajankar},
 editor = {Joku random},
 publisher = {Berkeley, CA : Apress : Imprint: Apress},
 title = {Python Unit Test Automation},
 year = {2017}
}
"""

        bibtex_string = reference_repository.create_bibtex_string(self.test_book)

        self.assertEqual(bibtex_string, test_string)

    def test_creating_bibtex_instance(self):

        bibtex_instance = reference_repository.create_bibtex_instance(self.test_book)

        self.assertDictEqual(bibtex_instance, self.test_book_dict)

    def test_formatting_multiple_authors(self):

        correct_format_authors = "Ashwin Pajankar and \n          Pashwin Ajankar"

        bibtex = reference_repository.bibtex_seperate_multiple(self.test_author_and_keyword_dict)

        self.assertEqual(bibtex["author"], correct_format_authors)

    def test_formatting_multiple_keywords(self):

        correct_format_keywords = "Testing,\n             Automation"

        bibtex = reference_repository.bibtex_seperate_multiple(self.test_author_and_keyword_dict)

        self.assertEqual(bibtex["keywords"], correct_format_keywords)
