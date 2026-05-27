from valid_anagram import Solution

class TestValidAnagram:
    def test_valid_anagram_example_1(self):
        s = Solution()
        assert s.is_anagram("anagram", "nagaram") is True

    def test_valid_anagram_example_2(self):
        s = Solution()
        assert s.is_anagram("rat", "car") is False

    def test_valid_anagram_empty_strings(self):
        s = Solution()
        assert s.is_anagram("", "") is True

    def test_valid_anagram_different_lengths(self):
        s = Solution()
        assert s.is_anagram("abc", "ab") is False

    def test_valid_anagram_special_characters(self):
        s = Solution()
        assert s.is_anagram("a!b@c#", "#c@b!a") is True

    def test_valid_anagram_case_sensitivity(self):
        s = Solution()
        assert s.is_anagram("Listen", "Silent") is False  # Case-sensitive check

    def test_valid_anagram_with_spaces(self):
        s = Solution()
        assert s.is_anagram("a b c", "c b a") is True  # Spaces should be considered
        assert s.is_anagram("a b c", "c b a ") is False  # Extra space should not match
        assert s.is_anagram("a b c", "c b a d") is False