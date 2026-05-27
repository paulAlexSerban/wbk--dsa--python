from top_k_frequent_elements import Solution

def test_top_k_frequent_elements():
    s = Solution()
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    expected_result = [1, 2]
    result = s.top_k_frequent(nums, k)
    assert sorted(result) == sorted(expected_result)
    
def test_top_k_frequent_elements_empty():
    s = Solution()
    nums = []
    k = 1
    expected_result = []
    result = s.top_k_frequent(nums, k)
    assert result == expected_result
    
def test_top_k_frequent_elements_single_element():
    s = Solution()
    nums = [1]
    k = 1
    expected_result = [1]
    result = s.top_k_frequent(nums, k)
    assert result == expected_result
    
def test_top_k_frequent_elements_no_repeats():
    s = Solution()
    nums = [1, 2, 3, 4]
    k = 2
    expected_result = [1, 2]  # Any two elements can be returned
    result = s.top_k_frequent(nums, k)
    assert len(result) == k
    assert all(num in nums for num in result)
    
def test_top_k_frequent_elements_all_same():
    s = Solution()
    nums = [2, 2, 2, 2]
    k = 1
    expected_result = [2]
    result = s.top_k_frequent(nums, k)
    assert result == expected_result
    
def test_top_k_frequent_elements_large_array():
    s = Solution()
    nums = [1, 2, 3, 4, 5, 3, 2, 1]
    k = 3
    expected_result = [1, 2, 3]  # Any three elements can be returned
    result = s.top_k_frequent(nums, k)
    assert len(result) == k
    assert all(num in nums for num in result)
    
def test_top_k_frequent_elements_no_side_effects():
    s = Solution()
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    result = s.top_k_frequent(nums, k)
    assert len(result) == 2
    assert all(num in nums for num in result)
    
    # Ensure original nums is unchanged
    assert nums == [1, 1, 1, 2, 2, 3]