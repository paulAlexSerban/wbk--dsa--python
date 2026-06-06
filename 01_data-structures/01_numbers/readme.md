---

## title: "Determine if a Number is Even"
language: "Python"
difficulty: "Beginner"
topic: "Number fundamentals"
slug: "determine-even-number"

## Problem Statement

Write a function `is_even(n)` that takes an integer `n` and returns `True` if the number is even, and `False` if it is odd.

Your solution must handle:

* Positive and negative integers.
* Zero (which is considered even).
* Invalid inputs: If the input is not an integer (e.g., float, string), the function must raise a `TypeError`.

## Starter Code / Skeleton

```python
def is_even(n: int) -> bool:
    """
    Determines if a given integer is even.
    
    Args:
        n (int): The number to check.
        
    Returns:
        bool: True if the number is even, False otherwise.
        
    Raises:
        TypeError: If n is not an integer.
    """
    # TODO: Validate the input type
    # TODO: Return True if even, False if odd
    pass

```

## Expected Output / Test Cases

```python
# Happy Path
assert is_even(4) == True
assert is_even(7) == False

# Edge Cases
assert is_even(0) == True
assert is_even(-2) == True
assert is_even(-13) == False

# Error Case
try:
    is_even(4.5)
    print("Failed: Should have raised TypeError")
except TypeError:
    print("Passed: TypeError correctly raised for float")

try:
    is_even("two")
    print("Failed: Should have raised TypeError")
except TypeError:
    print("Passed: TypeError correctly raised for string")

```

## Hints

1. **Hint 1:** How do you determine if a number is divisible by 2 in mathematics? Think about remainders.
2. **Hint 2:** In Python, the modulo operator (`%`) gives the remainder of a division. `x % y` returns the remainder of `x` divided by `y`.
3. **Hint 3:** Before doing the math, use `isinstance(n, int)` and `type(n) is not bool` to verify the input is strictly an integer, raising a `TypeError` if it isn't.

## Reference Solution

```python
def is_even(n: int) -> bool:
    # Booleans are a subclass of int in Python, so we strictly exclude them
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("Input must be an integer.")
    
    # An integer is even if its division by 2 leaves a remainder of 0
    return n % 2 == 0

```

## Time and Space Complexity Analysis

* **Time Complexity:** $O(1)$. The modulo operation and type checking take constant time regardless of the size of the number.
* **Space Complexity:** $O(1)$. No additional memory is allocated based on the input.

## Real-World Context Note

Determining if a number is even or odd is frequently used in UI development to alternate row colors in tables (zebra striping) or to distribute tasks evenly across two different processing queues (load balancing basics).

## Follow-up Challenge

Modify the function to determine if a number is a power of two using bitwise operators instead of the modulo operator.

---

## title: "Find the Maximum Element in a List"
language: "Python"
difficulty: "Beginner"
topic: "Data structures, Algorithms"
slug: "find-maximum-element"

## Problem Statement

Write a function `find_max(numbers)` that takes a list of numbers and returns the largest number in the list.

Your solution must handle:

* Lists containing positive numbers, negative numbers, or a mix of both.
* A list containing only a single element.
* Invalid inputs: If the list is empty, the function must raise a `ValueError`.

Do not use the built-in `max()` function.

## Starter Code / Skeleton

```python
from typing import List, Union

def find_max(numbers: List[Union[int, float]]) -> Union[int, float]:
    """
    Finds the maximum number in a list.
    
    Args:
        numbers (List[int, float]): A list of numbers.
        
    Returns:
        int or float: The largest number in the list.
        
    Raises:
        ValueError: If the list is empty.
    """
    # TODO: Check if the list is empty and raise ValueError if so
    # TODO: Initialize a variable to keep track of the maximum value seen so far
    # TODO: Iterate through the list to find the actual maximum
    pass

```

## Expected Output / Test Cases

```python
# Happy Path
assert find_max([1, 5, 3, 9, 2]) == 9

# Edge Cases
assert find_max([-10, -5, -20]) == -5
assert find_max([42]) == 42

# Error Case
try:
    find_max([])
    print("Failed: Should have raised ValueError")
except ValueError:
    print("Passed: ValueError correctly raised for empty list")

```

## Hints

1. **Hint 1:** You need to look at every single number in the list at least once. A `for` loop is your friend here.
2. **Hint 2:** Keep a running tracker of the "biggest number seen so far." What should you set this tracker to initially?
3. **Hint 3:** Initialize your tracker with the *first* element of the list `numbers[0]`. Then loop through the rest of the list. If you find a number bigger than your tracker, update the tracker.

## Reference Solution

```python
from typing import List, Union

def find_max(numbers: List[Union[int, float]]) -> Union[int, float]:
    # Handle the empty list error case first
    if not numbers:
        raise ValueError("Cannot find maximum in an empty list.")
    
    # Initialize the maximum with the first element of the list
    current_max = numbers[0]
    
    # Iterate through the remaining elements starting from index 1
    for num in numbers[1:]:
        if num > current_max:
            current_max = num  # Update if a strictly larger number is found
            
    return current_max

```

## Time and Space Complexity Analysis

* **Time Complexity:** $O(N)$, where $N$ is the number of elements in the list. We must inspect each element exactly once.
* **Space Complexity:** $O(1)$. We only use a single variable `current_max` to store the maximum value, taking constant extra space.

## Real-World Context Note

Finding the maximum (or minimum) value is a foundational linear search algorithm used constantly in data analytics (e.g., finding the highest temperature of the month, or the top-selling product).

## Follow-up Challenge

Update your function to return the *index* of the maximum element instead of the element itself. What happens if there are duplicate maximums?

---

## title: "Calculate the Sum of Digits"
language: "Python"
difficulty: "Beginner"
topic: "Number fundamentals, Algorithms"
slug: "calculate-sum-of-digits"

## Problem Statement

Write a function `sum_of_digits(n)` that takes an integer and returns the sum of its individual digits.

Your solution must handle:

* Positive numbers.
* Negative numbers (e.g., `-123` should evaluate to `1 + 2 + 3 = 6`).
* Zero (should evaluate to `0`).
* Invalid inputs: If the input is not an integer, raise a `TypeError`.

## Starter Code / Skeleton

```python
def sum_of_digits(n: int) -> int:
    """
    Calculates the sum of the digits of a given integer.
    
    Args:
        n (int): The integer whose digits will be summed.
        
    Returns:
        int: The sum of the digits.
        
    Raises:
        TypeError: If n is not an integer.
    """
    # TODO: Validate input
    # TODO: Handle negative numbers
    # TODO: Extract digits and sum them
    pass

```

## Expected Output / Test Cases

```python
# Happy Path
assert sum_of_digits(456) == 15  # 4 + 5 + 6 = 15

# Edge Cases
assert sum_of_digits(0) == 0
assert sum_of_digits(-314) == 8  # 3 + 1 + 4 = 8

# Error Case
try:
    sum_of_digits(45.6)
    print("Failed: Should have raised TypeError")
except TypeError:
    print("Passed: TypeError correctly raised for float")

```

## Hints

1. **Hint 1:** You can't iterate over an integer directly. How can you transform the number into something you can loop through? Alternatively, can you use math to extract digits one by one?
2. **Hint 2:** If using strings: Convert the absolute value of the number to a string, loop through the characters, convert back to integers, and sum them.
3. **Hint 3:** If using math: Use `abs(n)` to ignore the negative sign. Then use `n % 10` to get the last digit and `n // 10` to drop the last digit in a `while n > 0` loop.

## Reference Solution

```python
def sum_of_digits(n: int) -> int:
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("Input must be an integer.")
    
    # Use absolute value to handle negative numbers correctly
    n = abs(n)
    total_sum = 0
    
    # Mathematical approach: extract digits using modulo and integer division
    while n > 0:
        total_sum += n % 10  # Add the last digit to the sum
        n = n // 10          # Remove the last digit
        
    return total_sum

```

## Time and Space Complexity Analysis

* **Time Complexity:** $O(\log_{10} N)$, where $N$ is the value of the input number. The number of digits in $N$ is roughly $\log_{10} N$, and we process each digit once.
* **Space Complexity:** $O(1)$. The mathematical approach uses only a few variables. (If using string conversion, it would be $O(\log_{10} N)$ space to store the string).

## Real-World Context Note

Calculating the sum of digits is a fundamental component of various checksum algorithms, like the Luhn algorithm, which is used to validate credit card numbers and IMEI numbers.

## Follow-up Challenge

Keep summing the digits of the result until you are left with a single-digit number (this is known as finding the digital root).

---

## title: "Check for Palindrome String"
language: "Python"
difficulty: "Beginner"
topic: "Algorithms, Data structures"
slug: "check-palindrome-string"

## Problem Statement

Write a function `is_palindrome(s)` that checks if a given string reads the same forwards and backwards.

Your solution must handle:

* Case-insensitivity (e.g., "Racecar" is a palindrome).
* Spaces should be considered part of the string. (We are doing a strict character check, not ignoring spaces. So "a ba" is a palindrome, but "ab a" is not).
* Empty strings and single-character strings (both are technically palindromes).
* Invalid inputs: If the input is not a string, raise a `TypeError`.

## Starter Code / Skeleton

```python
def is_palindrome(s: str) -> bool:
    """
    Checks whether a string is a palindrome.
    
    Args:
        s (str): The string to check.
        
    Returns:
        bool: True if it is a palindrome, False otherwise.
        
    Raises:
        TypeError: If the input is not a string.
    """
    # TODO: Validate input type
    # TODO: Handle case-insensitivity
    # TODO: Compare the string to its reverse
    pass

```

## Expected Output / Test Cases

```python
# Happy Path
assert is_palindrome("madam") == True
assert is_palindrome("hello") == False

# Edge Cases
assert is_palindrome("Racecar") == True  # Mixed case
assert is_palindrome("") == True         # Empty string
assert is_palindrome("a") == True        # Single character
assert is_palindrome("a ba") == True     # Spaces match symmetrically
assert is_palindrome("ab a") == False    # Spaces do not match

# Error Case
try:
    is_palindrome(12321)
    print("Failed: Should have raised TypeError")
except TypeError:
    print("Passed: TypeError correctly raised for integer")

```

## Hints

1. **Hint 1:** Because "Racecar" and "racecar" should both be valid, you should convert the entire string to lowercase first.
2. **Hint 2:** Python strings can be reversed very easily using slicing. What does `s[::-1]` do?
3. **Hint 3:** Alternatively, you can use two pointers: one starting at index `0` and one at `len(s) - 1`, moving them towards the center and checking if the characters match.

## Reference Solution

```python
def is_palindrome(s: str) -> bool:
    if not isinstance(s, str):
        raise TypeError("Input must be a string.")
    
    # Convert string to lower case to handle case-insensitivity
    s = s.lower()
    
    # Two-pointer approach for optimal memory usage (avoids creating a new reversed string)
    left = 0
    right = len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
        
    return True

```

## Time and Space Complexity Analysis

* **Time Complexity:** $O(N)$ where $N$ is the length of the string. In the worst case (it is a palindrome), we iterate through half the string. The `.lower()` operation also takes $O(N)$ time.
* **Space Complexity:** $O(N)$ because the `.lower()` method creates a new string in memory. If we ignored case-insensitivity or assumed lowercase input, the two-pointer approach would be $O(1)$ space.

## Real-World Context Note

Palindromic sequence detection is surprisingly common in bioinformatics, where DNA strings are analyzed for palindromic structures, which often form binding sites for enzymes.

## Follow-up Challenge

Modify the function to ignore all spaces and non-alphanumeric characters (e.g., "A man, a plan, a canal: Panama" should return `True`).

---

## title: "Count Vowels in a String"
language: "Python"
difficulty: "Beginner"
topic: "Algorithms, Data structures"
slug: "count-vowels"

## Problem Statement

Write a function `count_vowels(text)` that returns the total number of vowels ('a', 'e', 'i', 'o', 'u') in a given string.

Your solution must handle:

* Both uppercase and lowercase letters.
* Strings that contain no vowels.
* Empty strings.
* Invalid inputs: Raise a `TypeError` if the input is not a string.

## Starter Code / Skeleton

```python
def count_vowels(text: str) -> int:
    """
    Counts the number of vowels in a string.
    
    Args:
        text (str): The string to process.
        
    Returns:
        int: The total count of vowels.
        
    Raises:
        TypeError: If the input is not a string.
    """
    # TODO: Validate input
    # TODO: Define what characters are considered vowels
    # TODO: Loop through the text and count occurrences
    pass

```

## Expected Output / Test Cases

```python
# Happy Path
assert count_vowels("hello world") == 3
assert count_vowels("python") == 1

# Edge Cases
assert count_vowels("AEROPLANE") == 5 # Uppercase
assert count_vowels("rhythm") == 0    # No vowels
assert count_vowels("") == 0          # Empty string

# Error Case
try:
    count_vowels(["a", "e", "i"])
    print("Failed: Should have raised TypeError")
except TypeError:
    print("Passed: TypeError correctly raised for list input")

```

## Hints

1. **Hint 1:** You need a way to track the total count. Start a variable at `0`.
2. **Hint 2:** Create a collection of vowels (e.g., a string `"aeiou"` or a set `{'a', 'e', 'i', 'o', 'u'}`).
3. **Hint 3:** Loop through each character in the input string. Convert the character to lowercase. If it exists in your collection of vowels, increase your count by `1`.

## Reference Solution

```python
def count_vowels(text: str) -> int:
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")
    
    # Using a set for O(1) lookups. Including both cases avoids calling .lower() on every char.
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    count = 0
    
    # Iterate through the string and count matches
    for char in text:
        if char in vowels:
            count += 1
            
    return count

```

## Time and Space Complexity Analysis

* **Time Complexity:** $O(N)$ where $N$ is the length of the string. We look at each character exactly once. Set lookups take $O(1)$ time.
* **Space Complexity:** $O(1)$. The `vowels` set takes a constant amount of memory regardless of the input string size.

## Real-World Context Note

Counting specific characters or patterns is the foundation of lexical analysis and text parsing. Similar logic is used in word processors to calculate read times or complexity scores.

## Follow-up Challenge

Return a dictionary containing the frequency count of *each specific vowel* instead of the total sum (e.g., `{'a': 2, 'e': 1}`).

---

## title: "Reverse Elements in a List"
language: "Python"
difficulty: "Beginner"
topic: "Data structures, Algorithms"
slug: "reverse-list-elements"

## Problem Statement

Write a function `reverse_list(items)` that takes a list and returns a new list with the elements in reverse order.

Your solution must handle:

* Lists with multiple items of any type.
* Empty lists and single-element lists.
* Invalid inputs: Raise a `TypeError` if the input is not a list.

Do not use the built-in `reversed()` function or the `.reverse()` list method.

## Starter Code / Skeleton

```python
from typing import List, Any

def reverse_list(items: List[Any]) -> List[Any]:
    """
    Reverses the elements of a list.
    
    Args:
        items (List[Any]): The list to reverse.
        
    Returns:
        List[Any]: A new list containing the elements in reverse order.
        
    Raises:
        TypeError: If the input is not a list.
    """
    # TODO: Validate input type
    # TODO: Create a new list to hold the reversed elements
    # TODO: Iterate backwards through the original list and append to the new list
    pass

```

## Expected Output / Test Cases

```python
# Happy Path
assert reverse_list([1, 2, 3, 4]) == [4, 3, 2, 1]
assert reverse_list(["a", "b", "c"]) == ["c", "b", "a"]

# Edge Cases
assert reverse_list([42]) == [42]
assert reverse_list([]) == []
assert reverse_list([True, False, 1, "test"]) == ["test", 1, False, True]

# Error Case
try:
    reverse_list("1234")
    print("Failed: Should have raised TypeError")
except TypeError:
    print("Passed: TypeError correctly raised for string input")

```

## Hints

1. **Hint 1:** How do you read a list backwards? Python's `range()` function can step backwards.
2. **Hint 2:** The last index of a list is `len(items) - 1`. You can loop from this index down to `0` using `range(start, stop, step)`.
3. **Hint 3:** Alternatively, Python allows slice notation to create reversed copies trivially: `items[::-1]`.

## Reference Solution

```python
from typing import List, Any

def reverse_list(items: List[Any]) -> List[Any]:
    if not isinstance(items, list):
        raise TypeError("Input must be a list.")
    
    # Pythonic approach using slice notation
    # [start:stop:step]. A step of -1 iterates backwards through the entire sequence.
    return items[::-1]

    # Alternative iterative approach:
    # reversed_items = []
    # for i in range(len(items) - 1, -1, -1):
    #     reversed_items.append(items[i])
    # return reversed_items

```

## Time and Space Complexity Analysis

* **Time Complexity:** $O(N)$ where $N$ is the number of elements in the list. Python's slice operation iterates over all elements to create the new list.
* **Space Complexity:** $O(N)$. We are creating and returning a completely new list of the same size as the input list.

## Real-World Context Note

Reversing data arrays is a common requirement in displaying timelines, chat histories, or news feeds where the most recent (last added) item needs to be shown first.

## Follow-up Challenge

Modify the function to reverse the list *in-place* (modifying the original list without creating a new one) and return `None`.

---

## title: "Remove Duplicates from a List"
language: "Python"
difficulty: "Beginner"
topic: "Data structures"
slug: "remove-duplicates-list"

## Problem Statement

Write a function `remove_duplicates(items)` that takes a list and returns a new list containing only the unique elements. The order of elements in the returned list does not matter.

Your solution must handle:

* Lists containing integers, strings, or mixed types.
* Lists where all elements are the same.
* Empty lists.
* Invalid inputs: Raise a `TypeError` if the input is not a list.

## Starter Code / Skeleton

```python
from typing import List, Any

def remove_duplicates(items: List[Any]) -> List[Any]:
    """
    Removes duplicate elements from a list.
    
    Args:
        items (List[Any]): The list containing potential duplicates.
        
    Returns:
        List[Any]: A new list containing only unique elements.
        
    Raises:
        TypeError: If the input is not a list.
    """
    # TODO: Validate input type
    # TODO: Find a way to track which elements you've already seen
    # TODO: Return the unique elements
    pass

```

## Expected Output / Test Cases

```python
# Happy Path
result1 = remove_duplicates([1, 2, 2, 3, 4, 4, 5])
assert sorted(result1) == [1, 2, 3, 4, 5]

# Edge Cases
result2 = remove_duplicates(["apple", "apple", "apple"])
assert result2 == ["apple"]

result3 = remove_duplicates([])
assert result3 == []

# Error Case
try:
    remove_duplicates(123)
    print("Failed: Should have raised TypeError")
except TypeError:
    print("Passed: TypeError correctly raised for integer input")

```

## Hints

1. **Hint 1:** You could loop through the list and append items to a new list only if they aren't already in it. But is there a built-in Python data structure designed specifically to hold unique elements?
2. **Hint 2:** A Python `set` is a collection of distinct, unique objects.
3. **Hint 3:** You can convert a list to a set using `set(items)`. This automatically removes duplicates. Then, convert it back to a list using `list()`.

## Reference Solution

```python
from typing import List, Any

def remove_duplicates(items: List[Any]) -> List[Any]:
    if not isinstance(items, list):
        raise TypeError("Input must be a list.")
    
    # Converting the list to a set automatically filters out duplicate values.
    # We then convert it back to a list to satisfy the return type requirement.
    return list(set(items))

```

## Time and Space Complexity Analysis

* **Time Complexity:** $O(N)$ on average, where $N$ is the number of items. Inserting elements into a set and then converting the set back to a list both scale linearly with the input size.
* **Space Complexity:** $O(N)$. The set data structure and the newly returned list allocate memory proportional to the number of unique elements.

## Real-World Context Note

Data cleaning workflows (ETL pipelines) constantly rely on deduplication to ensure analytical reports don't double-count metrics, like removing duplicate email registrations from a database.

## Follow-up Challenge

What if the order *does* matter? Rewrite the function so that the original order of the first occurrence of each element is preserved.

---

## title: "Calculate Factorial of a Number"
language: "Python"
difficulty: "Beginner"
topic: "Number fundamentals, Algorithms"
slug: "calculate-factorial"

## Problem Statement

Write a function `calculate_factorial(n)` that returns the factorial of a non-negative integer `n`. The factorial of `n` (denoted as `n!`) is the product of all positive integers less than or equal to `n`.

Your solution must handle:

* Positive integers.
* Zero: The factorial of 0 is mathematically defined as 1.
* Invalid inputs: Raise a `ValueError` if `n` is negative. Raise a `TypeError` if `n` is not an integer.

## Starter Code / Skeleton

```python
def calculate_factorial(n: int) -> int:
    """
    Calculates the factorial of a non-negative integer.
    
    Args:
        n (int): The number to calculate the factorial for.
        
    Returns:
        int: The factorial of n.
        
    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is negative.
    """
    # TODO: Validate input types and values
    # TODO: Handle the base case where n == 0
    # TODO: Compute the factorial using a loop or recursion
    pass

```

## Expected Output / Test Cases

```python
# Happy Path
assert calculate_factorial(5) == 120  # 5 * 4 * 3 * 2 * 1
assert calculate_factorial(3) == 6

# Edge Case
assert calculate_factorial(0) == 1
assert calculate_factorial(1) == 1

# Error Cases
try:
    calculate_factorial(-5)
    print("Failed: Should have raised ValueError")
except ValueError:
    print("Passed: ValueError correctly raised for negative number")

try:
    calculate_factorial(5.5)
    print("Failed: Should have raised TypeError")
except TypeError:
    print("Passed: TypeError correctly raised for float")

```

## Hints

1. **Hint 1:** You need to multiply a running total by numbers decreasing from `n` down to `1`.
2. **Hint 2:** Initialize a `result` variable to `1`. Use a `for` loop combined with `range()` or a `while` loop to iterate from 1 up to `n` (or `n` down to 1), multiplying `result` by the loop variable.
3. **Hint 3:** Alternatively, you can solve this recursively: `factorial(n) = n * factorial(n - 1)`. Don't forget your base case!

## Reference Solution

```python
def calculate_factorial(n: int) -> int:
    # Strict type checking
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("Input must be an integer.")
    
    # Value checking
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    
    # Base case for 0! = 1
    if n == 0:
        return 1
        
    result = 1
    # Iterative approach avoids recursion depth limits
    for i in range(1, n + 1):
        result *= i
        
    return result

```

## Time and Space Complexity Analysis

* **Time Complexity:** $O(N)$ where $N$ is the value of the input number. The loop runs exactly $N$ times.
* **Space Complexity:** $O(1)$. We only use a single variable to accumulate the result, requiring constant extra memory. (If using recursion, space complexity would be $O(N)$ due to the call stack).

## Real-World Context Note

Factorials are fundamental in combinatorics and probability theory—for example, calculating how many different ways a deck of cards can be shuffled or the likelihood of drawing a specific hand in poker.

## Follow-up Challenge

Factorials grow incredibly fast. Compute `calculate_factorial(100)` and notice how Python effortlessly handles arbitrarily large integers, unlike languages like C++ or Java which would experience integer overflow.

---

## title: "Find the Missing Number"
language: "Python"
difficulty: "Beginner"
topic: "Algorithms, Number fundamentals"
slug: "find-missing-number"

## Problem Statement

You are given a list of `n - 1` unique integers in the range of `1` to `n`. One number in that range is missing. Write a function `find_missing_number(numbers, n)` to find and return the missing number.

Your solution must handle:

* Unsorted lists.
* Edge cases where the missing number is the first (`1`) or last (`n`) in the sequence.
* Invalid inputs: Raise a `ValueError` if the list is empty.

## Starter Code / Skeleton

```python
from typing import List

def find_missing_number(numbers: List[int], n: int) -> int:
    """
    Finds the missing number in a sequence of 1 to n.
    
    Args:
        numbers (List[int]): List of n-1 unique integers from 1 to n.
        n (int): The upper bound of the sequence.
        
    Returns:
        int: The missing number.
        
    Raises:
        ValueError: If the input list is empty.
    """
    # TODO: Check if list is empty
    # TODO: Calculate the expected sum of numbers from 1 to n
    # TODO: Calculate the actual sum of the list
    # TODO: The difference is the missing number
    pass

```

## Expected Output / Test Cases

```python
# Happy Path
assert find_missing_number([3, 1, 4, 5], 5) == 2
assert find_missing_number([2, 4, 1, 6, 3, 7, 8], 8) == 5

# Edge Cases
assert find_missing_number([2, 3, 4], 4) == 1  # Missing first
assert find_missing_number([1, 2, 3], 4) == 4  # Missing last

# Error Case
try:
    find_missing_number([], 1)
    print("Failed: Should have raised ValueError")
except ValueError:
    print("Passed: ValueError correctly raised for empty list")

```

## Hints

1. **Hint 1:** You *could* sort the list and look for a gap, but sorting is slow. Can math help you find what's missing instantly?
2. **Hint 2:** Think about the sum. If no numbers were missing, what would all the numbers from `1` to `n` add up to?
3. **Hint 3:** The formula for the sum of the first `n` numbers is `n * (n + 1) / 2`. Calculate this expected sum, then subtract the `sum(numbers)`. The result is your missing number.

## Reference Solution

```python
from typing import List

def find_missing_number(numbers: List[int], n: int) -> int:
    if not numbers:
        raise ValueError("The list of numbers cannot be empty.")
    
    # Mathematical formula to find the sum of consecutive integers from 1 to n
    expected_sum = (n * (n + 1)) // 2
    
    # Calculate the sum of the integers actually present in the list
    actual_sum = sum(numbers)
    
    # The missing number is exactly the difference between the expected and actual sums
    return expected_sum - actual_sum

```

## Time and Space Complexity Analysis

* **Time Complexity:** $O(N)$ where $N$ is the number of items in the list. Calculating `expected_sum` is $O(1)$, but Python's built-in `sum()` iterates over the list in $O(N)$ time.
* **Space Complexity:** $O(1)$. We are only storing integer variables for the sums, requiring no extra memory correlated to the list size.

## Real-World Context Note

Mathematical tricks like this are frequently used to optimize algorithms. Finding data discrepancies using checksums or parity bits in network transmission protocols heavily relies on arithmetic differences rather than scanning arrays line by line.

## Follow-up Challenge

Solve the problem using the XOR (`^`) bitwise operator. Why might XOR be safer than the mathematical sum approach in languages with strict integer size limits?

---

## title: "Two Sum"
language: "Python"
difficulty: "Beginner"
topic: "Algorithms, Data structures"
slug: "two-sum-beginner"

## Problem Statement

Write a function `two_sum(numbers, target)` that takes a list of numbers and a target integer. It should return a list containing the two numbers from the array that add up to the target.

Your solution must handle:

* Finding the *first* pair that adds up to the target.
* Returning an empty list `[]` if no such pair exists.
* A number cannot be used twice (e.g., if target is 10, and array is `[5, 2]`, it cannot return `[5, 5]`).
* Invalid inputs: Raise a `ValueError` if the `numbers` list contains fewer than 2 elements.

## Starter Code / Skeleton

```python
from typing import List

def two_sum(numbers: List[int], target: int) -> List[int]:
    """
    Finds two numbers in a list that add up to a target sum.
    
    Args:
        numbers (List[int]): The list of numbers to search.
        target (int): The target sum.
        
    Returns:
        List[int]: A list containing the two numbers, or empty list if not found.
        
    Raises:
        ValueError: If the input list has fewer than 2 elements.
    """
    # TODO: Validate input list length
    # TODO: Use nested loops to check pairs, OR use a dictionary/set for efficiency
    # TODO: Return the pair when found
    pass

```

## Expected Output / Test Cases

```python
# Happy Path
assert two_sum([2, 7, 11, 15], 9) == [2, 7]
assert two_sum([3, 2, 4], 6) == [2, 4]

# Edge Cases
assert two_sum([1, 5, 9], 100) == []       # No valid pair exists
assert two_sum([3, 3], 6) == [3, 3]        # Same value, different indices

# Error Case
try:
    two_sum([5], 5)
    print("Failed: Should have raised ValueError")
except ValueError:
    print("Passed: ValueError correctly raised for list too short")

```

## Hints

1. **Hint 1:** The most straightforward way is to check every possible pair of numbers. You can do this with a `for` loop inside another `for` loop.
2. **Hint 2:** If you want a more efficient approach, iterate through the numbers. For each number, calculate its "complement" (`target - number`).
3. **Hint 3:** Keep track of the numbers you have seen so far in a `set`. As you iterate, if the `complement` is already in your `seen` set, you have found your pair!

## Reference Solution

```python
from typing import List

def two_sum(numbers: List[int], target: int) -> List[int]:
    if len(numbers) < 2:
        raise ValueError("List must contain at least 2 elements.")
    
    # We use a set to keep track of the numbers we've iterated over.
    # Lookups in a set are O(1) average time complexity.
    seen = set()
    
    for num in numbers:
        complement = target - num
        # If the complement exists in our set, we've found our pair.
        if complement in seen:
            return [complement, num]
        
        # Otherwise, add the current number to the set and continue.
        seen.add(num)
        
    # If the loop completes without finding a pair, return an empty list.
    return []

```

## Time and Space Complexity Analysis

* **Time Complexity:** $O(N)$ where $N$ is the number of elements. We loop through the list exactly once. Checking `if complement in seen` takes $O(1)$ time on average. (The brute-force nested loop approach would be $O(N^2)$).
* **Space Complexity:** $O(N)$. In the worst-case scenario (no pair found), we end up storing all $N$ elements in the `seen` set.

## Real-World Context Note

This algorithm demonstrates the classic "time-space tradeoff," where we use extra memory (a hash set) to dramatically speed up processing time. This is standard practice in caching queries in high-performance web applications.

## Follow-up Challenge

Modify the function to return the *indices* of the two numbers instead of the numbers themselves (you will need to replace the `set` with a `dict` to store index mappings).