from remove_duplicates_from_sorted_array import Solution


class TestRemoveDuplicatesFromSortedArray:
    def test_remove_duplicates_from_sorted_array(self):
        s = Solution()
        nums = [1, 1, 2]
        expected_nums = [1, 2]
        k = s.remove_duplicates(nums)
        assert k == len(expected_nums)

        for i in range(k):
            assert nums[i] == expected_nums[i]

    def test_remove_duplicates_empty_array(self):
        s = Solution()
        nums = []
        expected_nums = []
        k = s.remove_duplicates(nums)
        assert k == len(expected_nums)

        for i in range(k):
            assert nums[i] == expected_nums[i]

    def test_remove_duplicates_single_element(self):
        s = Solution()
        nums = [1]
        expected_nums = [1]
        k = s.remove_duplicates(nums)
        assert k == len(expected_nums)

        for i in range(k):
            assert nums[i] == expected_nums[i]

    def test_remove_duplicates_no_duplicates(self):
        s = Solution()
        nums = [1, 2, 3, 4]
        expected_nums = [1, 2, 3, 4]
        k = s.remove_duplicates(nums)
        assert k == len(expected_nums)

        for i in range(k):
            assert nums[i] == expected_nums[i]

    def test_remove_duplicates_all_duplicates(self):
        s = Solution()
        nums = [2, 2, 2, 2]
        expected_nums = [2]
        k = s.remove_duplicates(nums)
        assert k == len(expected_nums)

        for i in range(k):
            assert nums[i] == expected_nums[i]

    def test_remove_duplicates_large_array(self):
        s = Solution()
        nums = [1, 1, 2, 3, 3, 4, 5, 5, 6]
        expected_nums = [1, 2, 3, 4, 5, 6]
        k = s.remove_duplicates(nums)
        assert k == len(expected_nums)

        for i in range(k):
            assert nums[i] == expected_nums[i]

    def test_remove_duplicates_with_negative_numbers(self):
        s = Solution()
        nums = [-3, -3, -2, -1, 0, 0, 1]
        expected_nums = [-3, -2, -1, 0, 1]
        k = s.remove_duplicates(nums)
        assert k == len(expected_nums)

        for i in range(k):
            assert nums[i] == expected_nums[i]

    def test_remove_duplicates_with_large_numbers(self):
        s = Solution()
        nums = [1000000, 1000000, 2000000, 3000000]
        expected_nums = [1000000, 2000000, 3000000]
        k = s.remove_duplicates(nums)
        assert k == len(expected_nums)

        for i in range(k):
            assert nums[i] == expected_nums[i]

    def test_remove_duplicates_with_zero(self):
        s = Solution()
        nums = [0, 0, 1, 1, 2]
        expected_nums = [0, 1, 2]
        k = s.remove_duplicates(nums)
        assert k == len(expected_nums)

        for i in range(k):
            assert nums[i] == expected_nums[i]

    def test_remove_duplicates_with_repeated_elements(self):
        s = Solution()
        nums = [5, 5, 5, 5, 6, 7, 7]
        expected_nums = [5, 6, 7]
        k = s.remove_duplicates(nums)
        assert k == len(expected_nums)

        for i in range(k):
            assert nums[i] == expected_nums[i]

    def test_remove_duplicates_with_consecutive_duplicates(self):
        s = Solution()
        nums = [1, 2, 2, 3, 3, 3, 4]
        expected_nums = [1, 2, 3, 4]
        k = s.remove_duplicates(nums)
        assert k == len(expected_nums)

        for i in range(k):
            assert nums[i] == expected_nums[i]

class RemoveDuplicatesNoSideEffectsTest:
    def test_remove_duplicates_no_side_effects(self):
        s = Solution()
        nums = [1, 1, 2]
        expected_nums = [1, 2]
        k = s.remove_duplicates_no_side_effects(nums)
        assert k == len(expected_nums)

        for i in range(k):
            assert nums[i] == expected_nums[i]

    def test_remove_duplicates_no_side_effects_empty_array(self):
        s = Solution()
        nums = []
        expected_nums = []
        k = s.remove_duplicates_no_side_effects(nums)
        assert k == len(expected_nums)

        for i in range(k):
            assert nums[i] == expected_nums[i]

    def test_remove_duplicates_no_side_effects_single_element(self):
        s = Solution()
        nums = [1]
        expected_nums = [1]
        k = s.remove_duplicates_no_side_effects(nums)
        assert k == len(expected_nums)

        for i in range(k):
            assert nums[i] == expected_nums[i]