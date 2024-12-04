import unittest
from entities.reference import Reference
from repositories import reference_repository

class TestReference(unittest.TestCase):

    def setUp(self):

        self.test_book = Reference(
            "Testikirja",
            "book",
            "PyUnitTest-24",
            "2024",
            "Jukka Heikkinen",
            "Otava",
            "Marko Mäkinen"
        )

    def test_creating_empty_reference_dictionary(self):

        test_dict = reference_repository.create_input_dictionary()

        for key, value in test_dict.items():
            self.assertEqual(value, "")
            self.assertIsInstance(key, str)

    def test_creating_readable_string(self):

        correct_string = "Testikirja, Jukka Heikkinen, 2024, Otava, Marko Mäkinen"

        readable_string = reference_repository.create_readable_string(self.test_book)

        self.assertEqual(correct_string, readable_string)
