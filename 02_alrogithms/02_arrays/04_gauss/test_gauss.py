import unittest
from gauss import sum, sum_optimized, measure_sum, measure_sum_optimized

ranges = [10, 100, 1000, 10000, 100000, 1000000]

class TestGauss(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum(10), 55)
    
    def test_sum_optimized(self):
        self.assertEqual(sum_optimized(10), 55)
        
    def test_measure_sum(self):
        measure_sum(ranges)
    
    def test_measure_sum_optimized(self):
        measure_sum_optimized(ranges)
        
if __name__ == '__main__':
    unittest.main()