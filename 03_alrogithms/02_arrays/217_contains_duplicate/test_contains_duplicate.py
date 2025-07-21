from contains_duplicate import Solution

class TestContainsDuplicate:
    def test_contains_duplicate_example_1(self):
        s = Solution()
        assert s.contains_duplicate([1, 2, 3, 1]) is True

    def test_contains_duplicate_example_2(self):
        s = Solution()
        assert s.contains_duplicate([1, 2, 3, 4]) is False

    def test_contains_duplicate_example_3(self):
        s = Solution()
        assert s.contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) is True

    def test_contains_duplicate_empty_list(self):
        s = Solution()
        assert s.contains_duplicate([]) is False

    def test_contains_duplicate_single_element(self):
        s = Solution()
        assert s.contains_duplicate([1]) is False