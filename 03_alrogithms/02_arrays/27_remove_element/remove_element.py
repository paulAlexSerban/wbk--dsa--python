from typing import List

class Solution:
    def remove_element(self, nums: List[int], val: int) -> int:
        k = 0
        # use enumerate to iterate through the list
        for i, num in enumerate(nums):
            if num != val:  # check if the current element is not equal to the value to be removed
                nums[k] = num  # assign the current element to the next position
                k += 1  # increment the index of the last unique element
        return k  # return the length of the array after removing the element

    def remove_element_no_side_effects(self, nums: List[int], val: int) -> int:
        """Remove all instances of val from nums without side effects."""
        nums_copy = [num for num in nums if num != val]  # create a new list with elements not equal to val
        return len(nums_copy)