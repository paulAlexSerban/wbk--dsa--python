# Two Sum
> Difficulty: Easy
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 
Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

## Practical Applications
1. **Financial Transactions**: Quickly find pairs of transactions that sum to a specific amount.
2. **Inventory Management**: Identify pairs of items that together meet a certain weight or volume requirement.
3. **Social Networks**: Find pairs of users with a combined number of friends or followers that meets a target.
4. **E-commerce**: Recommend product bundles that together reach a specific price point.
5. **Gaming**: Identify pairs of players whose scores add up to a specific target for team formation.
6. **Healthcare**: Match patients with similar medical histories or treatment plans based on specific criteria.