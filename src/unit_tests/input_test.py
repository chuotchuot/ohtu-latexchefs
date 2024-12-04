import unittest
from repositories import reference_repository

class TestReferenceInput(unittest.TestCase):

    def test_creating_empty_input_dictionary(self):

        test_dict = reference_repository.create_input_dictionary()

        for key, value in test_dict.items():
            self.assertEqual(value, "")
            self.assertIsInstance(key, str)
