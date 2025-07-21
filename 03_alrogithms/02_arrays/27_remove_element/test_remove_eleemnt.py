from remove_element import Solution


class TestRemoveElement:
    def test_remove_element(self):
        s = Solution()
        nums = [3, 2, 2, 3]
        val = 3
        expected_nums = [2, 2]
        k = s.remove_element(nums, val)
        assert k == len(expected_nums)
        
        for i in range(k):
            assert nums[i] == expected_nums[i]
            
    def test_remove_element_empty_array(self):
        s = Solution()
        nums = []
        val = 1
        expected_nums = []
        k = s.remove_element(nums, val)
        assert k == len(expected_nums)
        for i in range(k):
            assert nums[i] == expected_nums[i]
    
    def test_remove_element_no_occurrences(self):
        s = Solution()
        nums = [1, 2, 3, 4]
        val = 5
        expected_nums = [1, 2, 3, 4]
        k = s.remove_element(nums, val)
        assert k == len(expected_nums)
        
        for i in range(k):
            assert nums[i] == expected_nums[i]
    
    def test_remove_element_all_occurrences(self):
        s = Solution()
        nums = [2, 2, 2, 2]
        val = 2
        expected_nums = []
        k = s.remove_element(nums, val)
        assert k == len(expected_nums)
        
        for i in range(k):
            assert nums[i] == expected_nums[i]
    
    def test_remove_element_large_array(self):
        s = Solution()
        nums = [1,  2, 3, 4, 5, 3, 2, 1]
        val = 3
        expected_nums = [1, 2, 4, 5, 2, 1]
        k = s.remove_element(nums, val)
        assert k == len(expected_nums)
        
        for i in range(k):
            assert nums[i] == expected_nums[i]
    
    def test_remove_element_no_side_effects(self):
        s = Solution()
        nums = [3, 2, 2, 3]
        val = 3
        k = s.remove_element_no_side_effects(nums, val)
        assert k == 2
        assert nums == [3, 2, 2, 3]