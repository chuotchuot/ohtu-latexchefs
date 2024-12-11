import unittest
from entities.reference import Reference
from entities.output import Output

class TestReferenceInput(unittest.TestCase):

    def setUp(self):

        self.test_author_and_keyword_dict = {
            "ENTRYTYPE": "book",
            "ID": "PyUnitTest-17",
            "title": "Python Unit Test Automation",
            "author": "Ashwin Pajankar and Pashwin Ajankar",
            "year": "2017",
            "publisher": "Berkeley, CA : Apress : Imprint: Apress",
            "editor": "No known editor",
            "keywords": "Testing, Automation"
        }

        self.test_book_dict = {
            "title": "Python Unit Test Automation",
            "reference_type": "book",
            "reference_key": "PyUnitTest-17",
            "year": "2017",
            "authors": "Ashwin Pajankar",
            "publisher": "Berkeley, CA : Apress : Imprint: Apress",
            "editors": "No known editor"
        }

        self.test_book = Reference()

        for key, value in self.test_book_dict.items():
            setattr(self.test_book, key, value)

        self.test_output = Output(self.test_book)
        self.test_output.set_id(1)

    def test_creating_bibtex_string(self):
        # Fix weird formatting without breaking the test
        test_string = """@book{PyUnitTest-17,
 author = {Ashwin Pajankar},
 editor = {No known editor},
 publisher = {Berkeley, CA : Apress : Imprint: Apress},
 title = {Python Unit Test Automation},
 year = {2017}
}
"""

        bibtex_string = self.test_output.create_bibtex_string()["text"]
        id = self.test_output.create_bibtex_string()["id"]

        self.assertEqual(bibtex_string, test_string)
        self.assertEqual(1, id)

    def test_creating_bibtex_instance(self):

        test_dict = {
            "ENTRYTYPE": "book",
            "ID": "PyUnitTest-17",
            "title": "Python Unit Test Automation",
            "author": "Ashwin Pajankar",
            "year": "2017",
            "publisher": "Berkeley, CA : Apress : Imprint: Apress",
            "editor": "No known editor"
        }

        bibtex_instance = self.test_output.create_bibtex_instance()

        self.assertDictEqual(bibtex_instance, test_dict)

    def test_formatting_multiple_authors(self):

        correct_format_authors = "Ashwin Pajankar and \n          Pashwin Ajankar"

        bibtex = self.test_output.bibtex_seperate_multiple(self.test_author_and_keyword_dict)

        self.assertEqual(bibtex["author"], correct_format_authors)

    def test_formatting_multiple_keywords(self):

        correct_format_keywords = "Testing,\n             Automation"

        bibtex = self.test_output.bibtex_seperate_multiple(self.test_author_and_keyword_dict)

        self.assertEqual(bibtex["keywords"], correct_format_keywords)
