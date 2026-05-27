from concatenation_of_array import Solution


def test_get_concatenation():
    s = Solution()
    nums = [1, 2, 3]
    expected_result = [1, 2, 3, 1, 2, 3]
    result = s.getConcatenation(nums)
    assert result == expected_result


def test_get_concatenation_empty():
    s = Solution()
    nums = []
    expected_result = []
    result = s.getConcatenation(nums)
    assert result == expected_result


def test_get_concatenation_single_element():
    s = Solution()
    nums = [5]
    expected_result = [5, 5]
    result = s.getConcatenation(nums)
    assert result == expected_result
