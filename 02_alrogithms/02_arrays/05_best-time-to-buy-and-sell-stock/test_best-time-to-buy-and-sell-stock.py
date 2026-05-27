import unittest
from best_time_to_buy_and_sell_stock import Solution


class TestBestTimeToBuyAndSellStock(unittest.TestCase):
    def test_best_time_to_buy_and_sell_stock(self):
        s = Solution()
        self.assertEqual(s.maxProfit([7, 1, 5, 3, 6, 4]), 5)
        self.assertEqual(s.maxProfit([7, 6, 4, 3, 1]), 0)
        self.assertEqual(s.maxProfit([2, 4, 1]), 2)
