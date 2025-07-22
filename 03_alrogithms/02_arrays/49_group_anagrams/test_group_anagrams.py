from group_anagrams import Solution


def test_group_anagrams():
    s = Solution()
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    expected_result = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
    result = s.group_anagrams(strs)

    # Check if the result contains the expected groups
    for group in expected_result:
        assert any(
            set(group) == set(r) for r in result
        ), f"Expected group {group} not found in result"

    # Check if all groups are present
    assert len(result) == len(
        expected_result
    ), f"Expected {len(expected_result)} groups, but got {len(result)}"


def test_group_anagrams_empty():
    s = Solution()
    strs = []
    expected_result = []
    result = s.group_anagrams(strs)
    assert result == expected_result, f"Expected {expected_result}, but got {result}"


def test_group_anagrams_single():
    s = Solution()
    strs = ["single"]
    expected_result = [["single"]]
    result = s.group_anagrams(strs)
    assert result == expected_result, f"Expected {expected_result}, but got {result}"


def test_group_anagrams_no_anagrams():
    s = Solution()
    strs = ["abc", "def", "ghi"]
    expected_result = [["abc"], ["def"], ["ghi"]]
    result = s.group_anagrams(strs)

    # Check if each string is in its own group
    assert len(result) == len(
        expected_result
    ), f"Expected {len(expected_result)} groups, but got {len(result)}"

    for group in expected_result:
        assert any(
            set(group) == set(r) for r in result
        ), f"Expected group {group} not found in result"


def test_group_anagrams_with_numbers():
    s = Solution()
    strs = ["123", "321", "231", "456"]
    expected_result = [["123", "321", "231"], ["456"]]
    result = s.group_anagrams(strs)

    # Check if the result contains the expected groups
    for group in expected_result:
        assert any(
            set(group) == set(r) for r in result
        ), f"Expected group {group} not found in result"

    # Check if all groups are present
    assert len(result) == len(
        expected_result
    ), f"Expected {len(expected_result)} groups, but got {len(result)}"
