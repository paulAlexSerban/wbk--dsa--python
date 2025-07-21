# Contains Duplicate
> Difficulty: Easy
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:
Input: nums = [1,2,3,1]
Output: true
Explanation: The element 1 occurs at the indices 0 and 3.

Example 2:
Input: nums = [1,2,3,4]
Output: false
Explanation: All elements are distinct.
All elements are distinct.

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
Explanation: The elements 1 and 3 occur multiple times.

Constraints:
1 <= nums.length <= 105
-109 <= nums[i] <= 109

## Practical Applications
1. **Data Validation**: Quickly check for duplicate entries in datasets, such as user IDs or transaction records.
2. **Inventory Management**: Ensure that product SKUs or barcodes are unique to prevent stock discrepancies.
3. **Social Media**: Detect duplicate posts or comments to maintain content integrity.
4. **Database Management**: Identify duplicate records in databases to maintain data quality and consistency.
5. **Network Security**: Monitor for duplicate IP addresses or MAC addresses to prevent network conflicts.
6. **Machine Learning**: Preprocess datasets to remove duplicate samples, ensuring model training is based on unique data points.
7. **Event Logging**: Detect duplicate events in logs to avoid redundancy and improve log analysis.
8. **E-commerce**: Identify duplicate product listings to streamline inventory and improve user experience.
9. **Healthcare**: Ensure patient records are unique to avoid medical errors and maintain accurate health information.
10. **Financial Transactions**: Detect duplicate transactions to prevent fraud and ensure accurate financial reporting.