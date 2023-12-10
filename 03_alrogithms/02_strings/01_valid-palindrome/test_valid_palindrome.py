import unittest
from valid_palindrome import Solution

class TestValidPalindrome(unittest.TestCase):
  def test_is_palindrome(self):
    s = Solution()
    self.assertEqual(s.isPalindrome("A man, a plan, a canal: Panama"), True, "Should be True")    
    self.assertEqual(s.isPalindrome("race a car"), False, "Should be False")
    self.assertEqual(s.isPalindrome("0P"), False, "Should be False")
    self.assertEqual(s.isPalindrome(" "), True, "Should be True")
    
if __name__ == '__main__':
    unittest.main()