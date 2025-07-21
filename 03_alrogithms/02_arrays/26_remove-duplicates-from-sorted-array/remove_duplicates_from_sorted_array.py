from typing import List



class Solution:
    def remove_duplicates(self, nums: List[int]) -> int:
        """Remove duplicates from a sorted array in-place.

        Args:
            nums (List[int]): The input sorted array.

        Returns:
            int: The length of the array after removing duplicates.
            
        Problem: This solution can produce side effects on the original array.
        It modifies the input array in-place to contain only unique elements.
        The function returns the new length of the array with unique elements.
        The original array is modified to contain the unique elements at the start.
        """
        if not nums: # check if the list is empty
            return 0
        i = 0
        for j in range(1, len(nums)):  # variable j is used to scan the array for unique elements
            # if the current element is different from the last unique element found
            if nums[j] != nums[i]:  # check if the current element is unique
                i += 1 # increment the index of the last unique element
                nums[i] = nums[j] # assign the current unique element to the next position
        return i + 1  # return the length of the array with unique elements
    
    def remove_duplicates_no_side_effects(self, nums: List[int]) -> int:
        """Remove duplicates from a sorted array without side effects.

        Args:
            nums (List[int]): The input sorted array.

        Returns:
            int: The length of the array after removing duplicates.
            
        Problem: This solution does not modify the original array.
        It creates a copy of the input array and modifies that copy.
        The function returns the new length of the array with unique elements.
        The original array remains unchanged.
        """
        if not nums:
            return 0
        nums_copy = nums[:]  # Create a copy of the array
        i = 0
        for j in range(1, len(nums_copy)):
            if nums_copy[j] != nums_copy[i]:
                i += 1
                nums_copy[i] = nums_copy[j]
        return i + 1
        # Note: This method does not modify the original nums array.
        # It returns the length of the modified copy, which is not reflected in nums.