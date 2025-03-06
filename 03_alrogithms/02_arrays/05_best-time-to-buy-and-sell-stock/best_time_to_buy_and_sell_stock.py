'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104
'''

'''
# 1. Initialize min_price to infinity. This will store the lowest price seen so far.
# 2. Initialize max_profit to 0. This will store the maximum profit found so far.
# 3. Iterate through each price in the list of prices.
# 4.1 If the current price is lower than the minimum price seen so far,
# 4.2 update min_price to the current price.
# 5.1 If the current price minus the minimum price seen so far is greater than the
# 5.2 maximum profit found so far, update max_profit to this new profit.
# 6. Return the maximum profit found.
'''

from typing import List  # 1
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf') # 1
        max_profit = 0 # 2
        for price in prices: # 3
            if price < min_price: # 4
                min_price = price

            elif price - min_price > max_profit: # 5
                max_profit = price - min_price
        return max_profit # 6

s = Solution()

# Test
print(s.maxProfit([7,1,5,3,6,4])) # 5
print(s.maxProfit([7,6,4,3,1])) # 0
print(s.maxProfit([2,4,1])) # 2