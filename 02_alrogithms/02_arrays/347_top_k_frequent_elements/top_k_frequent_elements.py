from typing import List
from collections import Counter
import heapq


class Solution:
    def top_k_frequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count frequency of each number - Example: If nums = [1, 1, 2, 2, 2, 3], freq_map will be {1: 2, 2: 3, 3: 1}.
        freq_map = Counter(nums)

        # Step 2: Use a heap to get the top k frequent elements
        # We use a min-heap of size k
        min_heap = []

        for num, freq in freq_map.items():
            heapq.heappush(min_heap, (freq, num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        # A min-heap is used to keep track of the top k frequent elements.
        # The heap stores tuples (freq, num) where freq is the frequency and num is the number.
        # For each (freq, num) in freq_map:
        # Add the tuple to the heap using heapq.heappush.
        # If the heap size exceeds k, remove the smallest element using heapq.heappop. This ensures the heap always contains the k most frequent elements.

        # Step 3: Extract the elements from the heap
        # Extract the numbers (num) from the heap and store them in the result list.
        # Return the result list as the output.
        result = [num for freq, num in min_heap]
        return result
