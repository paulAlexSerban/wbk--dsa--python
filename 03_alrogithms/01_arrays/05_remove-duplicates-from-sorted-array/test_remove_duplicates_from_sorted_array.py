import unittest
from remove_duplicates_from_sorted_array import Solution

class TestRemoveDuplicatesFromSortedArray(unittest.TestCase):
  def test_remove_duplicates_from_sorted_array(self):
    self.assertEqual(Solution().removeDuplicates([1,1,2]), 2, "Should be 2")
    self.assertEqual(Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4]), 5, "Should be 5")
    self.assertEqual(Solution().removeDuplicates([1,2]), 2, "Should be 2")
    self.assertEqual(Solution().removeDuplicates([1]), 1, "Should be 1")
    
if __name__ == '__main__':
    unittest.main()