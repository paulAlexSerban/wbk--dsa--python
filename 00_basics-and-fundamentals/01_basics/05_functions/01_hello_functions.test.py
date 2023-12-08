import unittest
from hello_functions import greet, uppercase, concatenate, say_hi, build_ferrari

class TestHelloFunctions(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("Paul"), "Hello Paul!")
        self.assertEqual(greet("John"), "Hello John!")
        self.assertEqual(greet("George"), "Hello George!")
        self.assertEqual(greet("Ringo"), "Hello Ringo!")

    def test_uppercase(self):
        self.assertEqual(uppercase("Paul"), "PAUL")
        self.assertEqual(uppercase("John"), "JOHN")
        self.assertEqual(uppercase("George"), "GEORGE")
        self.assertEqual(uppercase("Ringo"), "RINGO")

    def test_concatenate(self):
        self.assertEqual(concatenate("Paul", "McCartney"), "Paul McCartney")
        self.assertEqual(concatenate("John", "Lennon"), "John Lennon")
        self.assertEqual(concatenate("George", "Harrison"), "George Harrison")
        self.assertEqual(concatenate("Ringo", "Starr"), "Ringo Starr")

    def test_say_hi(self):
        self.assertEqual(say_hi("Paul"), "Hello Paul!")
        self.assertEqual(say_hi("John"), "Hello John!")
        self.assertEqual(say_hi("George"), "Hello George!")
        self.assertEqual(say_hi("Ringo"), "Hello Ringo!")

    def test_build_ferrari(self):
        self.assertEqual(build_ferrari(), "Build a red Ferrari")
        self.assertEqual(build_ferrari("blue"), "Build a blue Ferrari")
        self.assertEqual(build_ferrari("yellow"), "Build a yellow Ferrari")
        
if __name__ == '__main__':
    unittest.main()