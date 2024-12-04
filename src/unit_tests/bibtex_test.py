import unittest
from entities.reference import Reference
from repositories import reference_repository

class TestReferenceInput(unittest.TestCase):

    def setUp(self):

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

        print(test_string)

        self.assertEqual(bibtex_string, test_string)
