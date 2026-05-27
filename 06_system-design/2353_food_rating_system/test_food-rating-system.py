import unittest

from food_rating_system import FoodRatings

class TestFoodRatings(unittest.TestCase):
    def setUp(self):
        self.foods = ["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"]
        self.cuisines = ["korean", "japanese", "japanese", "greek", "japanese", "korean"]
        self.ratings = [9, 12, 8, 15, 14, 7]
        self.fr = FoodRatings(self.foods, self.cuisines, self.ratings)

    def test_initial_highest_rated(self):
        self.assertEqual(self.fr.highestRated("korean"), "kimchi")
        self.assertEqual(self.fr.highestRated("japanese"), "ramen")
        self.assertEqual(self.fr.highestRated("greek"), "moussaka")

    def test_change_rating_and_highest(self):
        self.fr.changeRating("sushi", 16)
        self.assertEqual(self.fr.highestRated("japanese"), "sushi")
        self.fr.changeRating("ramen", 16)
        self.assertEqual(self.fr.highestRated("japanese"), "ramen")  # tie, ramen < sushi

    def test_multiple_changes(self):
        self.fr.changeRating("kimchi", 5)
        self.assertEqual(self.fr.highestRated("korean"), "bulgogi")
        self.fr.changeRating("bulgogi", 10)
        self.assertEqual(self.fr.highestRated("korean"), "bulgogi")
        self.fr.changeRating("kimchi", 10)
        self.assertEqual(self.fr.highestRated("korean"), "bulgogi")  # tie, bulgogi < kimchi

    def test_single_food_cuisine(self):
        foods = ["a"]
        cuisines = ["x"]
        ratings = [1]
        fr = FoodRatings(foods, cuisines, ratings)
        self.assertEqual(fr.highestRated("x"), "a")
        fr.changeRating("a", 5)
        self.assertEqual(fr.highestRated("x"), "a")

    def test_all_same_rating(self):
        foods = ["a", "b", "c"]
        cuisines = ["x", "x", "x"]
        ratings = [5, 5, 5]
        fr = FoodRatings(foods, cuisines, ratings)
        self.assertEqual(fr.highestRated("x"), "a")
        fr.changeRating("b", 5)
        self.assertEqual(fr.highestRated("x"), "a")
        fr.changeRating("a", 1)
        self.assertEqual(fr.highestRated("x"), "b")

if __name__ == "__main__":
    unittest.main()