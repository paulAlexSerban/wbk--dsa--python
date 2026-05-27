class MinimumPathSum(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        # We'll use a bottom-up dynamic programming approach.
        # Start from the last row and move upwards, updating the minimum path sum for each element.
        # We can do this in-place, but to meet the O(n) extra space follow-up, use a single array.
        
        n = len(triangle)
        # Copy the last row as the initial minimum path sums
        min_path = triangle[-1][:]
        
        # Iterate from second last row up to the top
        for row in range(n - 2, -1, -1):
            for i in range(len(triangle[row])):
                # For each element, choose the minimum path sum from the adjacent numbers below
                min_path[i] = triangle[row][i] + min(min_path[i], min_path[i + 1])
        
        # The answer is the minimum path sum from the top
        return min_path[0]