# Concatenation of Array

Difficulty: Easy

Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
Specifically, ans is the concatenation of two nums arrays.
Return the array ans.

Example 1:
Input: nums = [1,2,1]
Output: [1,2,1,1,2,1]
Explanation: The array ans is formed as follows:

- ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
- ans = [1,2,1,1,2,1]

Example 2:
Input: nums = [1,3,2,1]
Output: [1,3,2,1,1,3,2,1]
Explanation: The array ans is formed as follows:

- ans = [nums[0],nums[1],nums[2],nums[3],nums[0],nums[1],nums[2],nums[3]]
- ans = [1,3,2,1,1,3,2,1]

Constraints:
n == nums.length
1 <= n <= 1000
1 <= nums[i] <= 1000

## Practical Applications

1. **Data Duplication**: Useful in scenarios where you need to duplicate data for processing
   or analysis, such as creating test datasets or simulating data streams.
2. **Array Manipulation**: Helps in understanding array manipulation techniques, which are
   fundamental in many algorithms and data structures.
3. **Algorithm Design**: Provides a basis for designing algorithms that require array concatenation,
   such as merging sorted arrays or combining results from different computations.
4. **Memory Management**: Demonstrates how to handle memory allocation and management when
   working with larger datasets, especially in languages with manual memory management.
