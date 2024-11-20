import unittest
from entities.reference import Reference

class TestReference(unittest.TestCase):

    def setUp(self):
        self.correct_reference = Reference(
            "Test-driven Python development : develop high-quality and maintainable Python applications using the principles of test-driven development", 
            2015, 
            "Siddharta Govindaraj",
            "TDDPython",
            "Programming, Agile, Testing, Software development"
        )

    def test_create_reference(self):
        self.assertEqual(self.correct_reference.title, "Test-driven Python development : develop high-quality and maintainable Python applications using the principles of test-driven development")
        self.assertEqual(self.correct_reference.year, 2015)
        self.assertEqual(self.correct_reference.authors, "Siddharta Govindaraj")
        self.assertEqual(self.correct_reference.reference_key, "TDDPython")
        self.assertEqual(self.correct_reference.keywords, "Programming, Agile, Testing, Software development")