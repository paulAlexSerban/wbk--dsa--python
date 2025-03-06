'''
1. Normalize the string
2. Check if the string is equal to its reverse

Notes:
char.isalnum() 
  - to check if a character is alphanumeric (either a letter or a number).
  - Return True if the string is an alpha-numeric string, False otherwise.
[::-1] 
  - is a common idiom for reversing a string or list.
  - Return a reversed copy of the string or list.
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        normalized_str = ''.join(char.lower() for char in s if char.isalnum()) # 1
        return normalized_str == normalized_str[::-1] # 2
