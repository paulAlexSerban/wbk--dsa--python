from valid_parentheses import Solution


def test_valid_parentheses():
    s = Solution()

    # Test cases for valid parentheses
    assert s.is_valid("()") == True
    assert s.is_valid("()[]{}") == True
    assert s.is_valid("(]") == False
    assert s.is_valid("([)]") == False
    assert s.is_valid("{[]}") == True

    # Edge cases
    assert s.is_valid("") == True  # Empty string is valid
    assert s.is_valid("(") == False  # Single opening bracket is invalid
    assert s.is_valid(")") == False  # Single closing bracket is invalid
    assert s.is_valid("((()))") == True  # Nested valid parentheses
    assert s.is_valid("([{}])") == True  # Mixed valid parentheses
    assert s.is_valid("([)]") == False  # Mixed invalid parentheses
    assert s.is_valid("((()))[]{}") == True  # Multiple valid parentheses
    assert s.is_valid("((()))[{}]") == True  # Nested and mixed
    assert s.is_valid("((()))[{}]") == True  # Nested and mixed
    assert s.is_valid("((()))[{}]") == True  # Nested and mixed


def test_codebase():
    sut = Solution()

    codebase = """
    const isValid = (s) => {
      const stack = [];
      const mapping = {')': '(', '}': '{', ']': '['};
      for (const char of s) {
        if (char in mapping) {
          const topElement = stack.pop() || '#';
          if (mapping[char] !== topElement) return false;
        } else {
          stack.push(char);
        }
      }
      return !stack.length;
    };
    """
    assert sut.is_valid(codebase) == False  # Invalid parentheses in codebase
