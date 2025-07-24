# Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([])"
Output: true

Example 5:
Input: s = "([)]"
Output: false

Constraints:

- 1 <= s.length <= 104
- s consists of parentheses only '()[]{}'.

## Practical Applications

1. **Syntax Checking**: Validating code syntax in programming languages, ensuring that all brackets and parentheses are correctly matched.
2. **Data Parsing**: Ensuring that data structures like JSON or XML are correctly formatted, where brackets and parentheses must be properly nested.
3. **Algorithm Design**: Many algorithms, such as those for parsing expressions or evaluating mathematical formulas, rely on valid parentheses to function correctly.
4. **Compiler Design**: Compilers use this validation to ensure that the source code adheres to the syntax rules of the programming language, preventing errors during compilation.
5. **Game Development**: In game development, valid parentheses are often used to define actions, behaviors, or groupings within the game's code, ensuring that the logic flows correctly.
6. **User Input Validation**: In applications where users can input expressions or commands, validating parentheses helps prevent errors and ensures that the input is correctly interpreted.
7. **Data Structures**: Understanding valid parentheses is crucial in data structures like stacks and queues, where operations often involve matching pairs of brackets.
8. **Mathematical Expressions**: Validating mathematical expressions to ensure that operations are correctly grouped and evaluated, especially in calculators or computational software.
