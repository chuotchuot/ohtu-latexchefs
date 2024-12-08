import unittest
from entities.reference import Reference
from repositories import reference_repository

class TestReference(unittest.TestCase):

    def setUp(self):

        input_book_dict = {
            "title": "Java Unit Testing with JUnit 5 : Test Driven Development with JUnit 5",
            "reference_type": "book",
            "reference_key": "JavaUT-17",
            "year": "2017",
            "authors": "Shekhar Gulati;Rahul Sharma",
            "publisher": "Berkeley, CA : Apress : Imprint: Apress",
            "editors": "Shekhar Gulati;Rahul Sharma",
            "keywords": "Testing;Java;Development"
        }

        queried_book_dict = {
            "title": "Java Unit Testing with JUnit 5 : Test Driven Development with JUnit 5",
            "reference_type": "book",
            "reference_key": "JavaUT-17",
            "year": "2017",
            "authors": "Shekhar Gulati and Rahul Sharma",
            "publisher": "Berkeley, CA : Apress : Imprint: Apress",
            "editors": "Shekhar Gulati and Rahul Sharma"
        }

        self.test_input_book = Reference()
        self.test_output_book = Reference()

        for key, value in input_book_dict.items():
            setattr(self.test_input_book, key, value)

        for key, value in queried_book_dict.items():
            setattr(self.test_output_book, key, value)

    def test_creating_empty_reference_dictionary(self):

        test_dict = reference_repository.create_input_dictionary()

        for key, value in test_dict.items():
            self.assertEqual(value, "")
            self.assertIsInstance(key, str)

    def test_creating_readable_string(self):

        correct_str = ("Java Unit Testing with JUnit 5 : Test Driven Development with JUnit 5, "
                       "Shekhar Gulati and Rahul Sharma, "
                       "2017, "
                       "Berkeley, CA : Apress : Imprint: Apress, "
                       "Shekhar Gulati and Rahul Sharma")

        readable_str= reference_repository.create_readable_string(self.test_output_book)

        self.assertEqual(correct_str, readable_str)

    def test_formatting_multiple_authors(self):

        correct_str = "Shekhar Gulati and Rahul Sharma"

        self.test_input_book.format_fields_with_multiple_values()

        self.assertEqual(correct_str, self.test_input_book.authors)

    def test_formatting_multiple_keywords(self):

        correct_str = "Testing, Java, Development"

        self.test_input_book.format_fields_with_multiple_values()

        self.assertEqual(correct_str, self.test_input_book.keywords)
