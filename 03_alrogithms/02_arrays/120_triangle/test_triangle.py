import unittest

from triangle import MinimumPathSum

class TestMinimumPathSum(unittest.TestCase):
    def setUp(self):
        self.solver = MinimumPathSum()

    def test_example1(self):
        triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
        self.assertEqual(self.solver.minimumTotal(triangle), 11)

    def test_example2(self):
        triangle = [[-10]]
        self.assertEqual(self.solver.minimumTotal(triangle), -10)

    def test_single_row(self):
        triangle = [[1]]
        self.assertEqual(self.solver.minimumTotal(triangle), 1)

    def test_two_rows(self):
        triangle = [[1],[2,3]]
        self.assertEqual(self.solver.minimumTotal(triangle), 3)

    def test_negative_numbers(self):
        triangle = [[-1],[-2,-3],[-4,-5,-6]]
        self.assertEqual(self.solver.minimumTotal(triangle), -10)

    def test_large_triangle(self):
        triangle = [
            [1],
            [2, 3],
            [4, 5, 6],
            [7, 8, 9, 10],
            [11, 12, 13, 14, 15]
        ]
        self.assertEqual(self.solver.minimumTotal(triangle), 25)

    def test_all_same_numbers(self):
        triangle = [
            [5],
            [5, 5],
            [5, 5, 5]
        ]
        self.assertEqual(self.solver.minimumTotal(triangle), 15)