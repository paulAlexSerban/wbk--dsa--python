from typing import List  # 1

"""
# Solution:
# 1. Importing the List type from the typing module
# 2. Initialize a dictionary to store the number and its corresponding index
# 3. Iterate through the list of numbers along with their indices
# 4. Calculate the difference needed to reach the target from the current number
# 5. Check if the calculated difference is already present in the dictionary
# 6.1. If the difference is found, return the indices of the two numbers
# 6.2. The index of the current number and the index of the number that forms the required sum with the current number
# 7. If the difference is not found, store the current number and its index in the dictionary for future reference
# 8. Return an empty list if no such pair is found that adds up to the target
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        number_to_index = {}  # 2
        for index, number in enumerate(nums):  # 3
            difference = target - number  # 4
            if difference in number_to_index:  # 5
                return [number_to_index[difference], index]  # 6
            number_to_index[number] = index  # 7
        return []  # 8


s = Solution()
# Test
print(s.twoSum([2, 7, 11, 15], 9))  # [0, 1]
print(s.twoSum([3, 2, 4], 6))  # [1, 2]
print(s.twoSum([3, 3], 6))  # [0, 1]
