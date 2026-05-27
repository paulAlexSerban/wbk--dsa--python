from sum_two import Solution


class TestSumTwo:
    def test_sum_two_example_1(self):
        s = Solution()
        assert s.twoSum([2, 7, 11, 15], 9) == [0, 1]

    def test_sum_two_example_2(self):
        s = Solution()
        assert s.twoSum([3, 2, 4], 6) == [1, 2]

    def test_sum_two_example_3(self):
        s = Solution()
        assert s.twoSum([3, 3], 6) == [0, 1]

    def test_sum_two_no_solution(self):
        s = Solution()
        assert s.twoSum([1, 2, 3], 7) == []

    def test_sum_two_empty_list(self):
        s = Solution()
        assert s.twoSum([], 5) == []

    def test_sum_two_single_element(self):
        s = Solution()
        assert s.twoSum([1], 1) == []
