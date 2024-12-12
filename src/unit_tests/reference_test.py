import unittest
from entities.reference import Reference
from entities.output import Output

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

        self.test_output = Output(self.test_output_book)
        self.test_output.set_id(1)

    def test_creating_readable_string(self):

        correct_str = ("Java Unit Testing with JUnit 5 : Test Driven Development with JUnit 5, "
                       "Shekhar Gulati and Rahul Sharma, "
                       "2017, "
                       "Berkeley, CA : Apress : Imprint: Apress, "
                       "Shekhar Gulati and Rahul Sharma")

        readable_str = self.test_output.create_readable_string()["text"]
        ref_id = self.test_output.create_readable_string()["id"]

        self.assertEqual(correct_str, readable_str)
        self.assertEqual(1, ref_id)

    def test_formatting_multiple_authors(self):

        correct_str = "Shekhar Gulati and Rahul Sharma"

        self.test_input_book.format_fields_with_multiple_values()

        self.assertEqual(correct_str, self.test_input_book.authors)

    def test_formatting_multiple_keywords(self):

        correct_str = "Testing, Java, Development"

        self.test_input_book.format_fields_with_multiple_values()

        self.assertEqual(correct_str, self.test_input_book.keywords)

    def test_add_values_from_dictionary(self):
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

        reference = Reference()
        reference.add_values_from_dictionary(input_book_dict.items())

        self.assertEqual(reference.title, self.test_input_book.title)
        self.assertEqual(reference.reference_type, self.test_input_book.reference_type)
        self.assertEqual(reference.reference_key, self.test_input_book.reference_key)
        self.assertEqual(reference.year, self.test_input_book.year)
        self.assertEqual(reference.authors, self.test_input_book.authors)
        self.assertEqual(reference.publisher, self.test_input_book.publisher)
        self.assertEqual(reference.editors, self.test_input_book.editors)
        self.assertEqual(reference.keywords, self.test_input_book.keywords)

    def test_add_values_from_doi(self):
        data = {
            "title": "Software unit test coverage and adequacy",
            "author": "Zhu, Hong and Hall, Patrick A. V. and May, John H. R.",
            "year": "1997",
            "journal": "ACM Comput. Surv.",
            "volume": "29",
            "number": "4",
            "page": "366–427",
            "month": "dec",
        }

        reference = Reference()
        reference.add_values_from_doi(data)

        self.assertEqual(reference.title, data.get("title"))
        self.assertEqual(reference.authors, data.get("author"))
        self.assertEqual(reference.year, data.get("year"))
        self.assertEqual(reference.journal, data.get("journal"))
        self.assertEqual(reference.volume, data.get("volume"))
        self.assertEqual(reference.number, data.get("number"))
        self.assertEqual(reference.page, data.get("page"))
        self.assertEqual(reference.month, data.get("month"))

    def test_set_reference_key(self):
        test_ref_key = "RefKey"

        reference = Reference()
        reference.set_reference_key(test_ref_key)

        self.assertEqual(test_ref_key, reference.reference_key)
