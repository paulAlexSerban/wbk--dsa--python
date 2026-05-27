import unittest
from majority_element import Solution

class TestMajorityElement(unittest.TestCase):
    def test_majority_element(self):
        s = Solution()
        self.assertEqual(s.majorityElement([3,2,3]), 3, "Should be 3")
        self.assertEqual(s.majorityElement([2,2,1,1,1,2,2]), 2, "Should be 2")
        self.assertEqual(s.majorityElement([1]), 1, "Should be 1")
        self.assertEqual(s.majorityElement([1,2,2]), 2, "Should be 2")
        
if __name__ == '__main__':
    unittest.main()