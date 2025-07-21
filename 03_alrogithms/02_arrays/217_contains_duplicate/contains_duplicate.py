from typing import List


class Solution:
    def contains_duplicate(self, nums: List[int]) -> bool:
        """
        Check if the array contains any duplicates.

        :param nums: List of integers
        :return: True if duplicates are found, False otherwise
        """
        return len(set(nums)) != len(nums)
