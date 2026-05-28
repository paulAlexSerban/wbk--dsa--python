from typing import List


def contains_duplicate(nums: List[int]) -> bool:
    """
    Check if the array contains any duplicates.

    :param nums: List of integers
    :return: True if duplicates are found, False otherwise
    """
    return   len(nums) != len(set(nums))
