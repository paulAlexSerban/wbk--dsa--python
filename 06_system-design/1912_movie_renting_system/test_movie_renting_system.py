import unittest

from movie_renting_system import MovieRentingSystem

class TestMovieRentingSystem(unittest.TestCase):
    def test_movie_renting_system(self):
        mrs = MovieRentingSystem(3, [[0, 1, 5], [0, 2, 6], [0, 3, 7], [1, 1, 4], [1, 2, 7], [2, 1, 5]])
        self.assertEqual(mrs.search(1), [1, 0, 2])
        mrs.rent(0, 1)
        mrs.rent(1, 2)
        self.assertEqual(mrs.report(), [[0, 1], [1, 2]])
        mrs.drop(1, 2)
        self.assertEqual(mrs.search(2), [0, 1])

    def test_additional_cases(self):
        mrs = MovieRentingSystem(2, [[0, 1, 3], [0, 2, 4], [1, 1, 2], [1, 2, 5]])
        self.assertEqual(mrs.search(1), [1, 0])
        mrs.rent(1, 1)
        self.assertEqual(mrs.report(), [[1, 1]])
        mrs.drop(1, 1)
        self.assertEqual(mrs.search(1), [1, 0])
 
    