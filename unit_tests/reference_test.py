import unittest
from entities.reference import Reference

class TestReference(unittest.Testcase):

    def setup(self):
        self.correct_reference = Reference(
            "Test-driven Python development : develop high-quality and maintainable Python applications using the principles of test-driven development ", 
            2015, 
            "Siddharta Govindaraj"
        
        )