import unittest
from entities.reference import Reference
from repositories import reference_repository

class TestReference(unittest.TestCase):

    def setUp(self):

        book_dict = {
            "title": "Testikirja",
            "reference_type": "book",
            "reference_key": "PyUnitTest-24",
            "year": "2024",
            "authors": "Jukka Heikkinen and Arto Kuokkanen",
            "publisher": "Otava",
            "editors": "Marko Mäkinen"
        }

        self.test_book = Reference()

        for key, value in book_dict.items():
            setattr(self.test_book, key, value)

        self.test_authors = "Jukka Heikkinen;Arto Kuokkanen"
        self.test_keywords = "Development;Testing;Python"

    def test_creating_empty_reference_dictionary(self):

        test_dict = reference_repository.create_input_dictionary()

        for key, value in test_dict.items():
            self.assertEqual(value, "")
            self.assertIsInstance(key, str)

    def test_creating_readable_string(self):

        correct_str = "Testikirja, Jukka Heikkinen and Arto Kuokkanen, 2024, Otava, Marko Mäkinen"

        readable_str= reference_repository.create_readable_string(self.test_book)

        self.assertEqual(correct_str, readable_str)

    def test_formatting_multiple_authors(self):

        correct_str = "Jukka Heikkinen and Arto Kuokkanen"

        formatted_str= reference_repository.format_multiple_values(self.test_authors, "authors")

        self.assertEqual(correct_str, formatted_str)

    def test_formatting_multiple_keywords(self):

        correct_str = "Development, Testing, Python"

        formatted_str = reference_repository.format_multiple_values(self.test_keywords, "keywords")

        self.assertEqual(correct_str, formatted_str)
