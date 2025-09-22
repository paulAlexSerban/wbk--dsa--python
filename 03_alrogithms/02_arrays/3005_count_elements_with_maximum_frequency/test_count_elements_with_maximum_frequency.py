import unittest

from count_elements_with_maximum_frequency import CountElementsWithMaximumFrequency

class TestCountElementsWithMaximumFrequency(unittest.TestCase):
    def setUp(self):
        self.solver = CountElementsWithMaximumFrequency()
    
    def test_example1(self):
        nums = [1, 2, 2, 3, 1]
        self.assertEqual(self.solver.maxFrequencyElements(nums), 4)  # Elements 1 and 2 both have max frequency of 2

    def test_example2(self):
        nums = [1, 1, 1, 2, 2, 3]
        self.assertEqual(self.solver.maxFrequencyElements(nums), 3)  # Element 1 has max frequency of 3

    def test_example3(self):
        nums = [4, 4, 4, 4]
        self.assertEqual(self.solver.maxFrequencyElements(nums), 4)  # Element 4 has max frequency of 4

    def test_example4(self):
        nums = [5]
        self.assertEqual(self.solver.maxFrequencyElements(nums), 1)  # Only one element

    def test_example5(self):
        nums = [1, 2, 3, 4, 5]
        self.assertEqual(self.solver.maxFrequencyElements(nums), 5)  # All elements have frequency of 1

    def test_example6(self):
        nums = [1, 1, 2, 2, 3, 3]
        self.assertEqual(self.solver.maxFrequencyElements(nums), 6)  # All elements have frequency of 2