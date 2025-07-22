from math_operations import add

"""
Unit testing in Python is commonly done using the unittest framework, which is a standard library module for writing and running tests. Here's a basic example to demonstrate how you can write and run a unit test for a simple function.

In this test file:
We import unittest and the function add from math_operations.py.
We define a test class TestMathOperations that inherits from unittest.TestCase.
Inside the class, we define a test method test_add. This method uses assertEqual to check if the output of the add function matches the expected result.
We include the if __name__ == '__main__': unittest.main() block to make the test executable.
"""


class TestMathOperations:
    def test_add(self):
        assert add(1, 2) == 3
        assert add(-1, 1) == 0
        assert add(-1, -1) == -2


"""
If all tests pass, you will see a message indicating that (usually something like OK). If a test fails, the unittest framework will provide details about the failing test case.
Unit tests are used to ensure that small parts (units) of your code work as expected.
It's a good practice to write tests that cover different edge cases and scenarios for your functions.
The unittest framework offers a variety of assert methods like assertEqual, assertTrue, assertFalse, assertRaises, etc., to handle different test conditions.
"""
