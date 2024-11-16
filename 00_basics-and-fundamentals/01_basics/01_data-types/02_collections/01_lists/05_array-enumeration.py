# Enumeration: The enumerate function in Python adds a counter to an iterable and returns it as 
# an enumerate object. This is useful when you need both the value and the index of elements in a list.

# Example:
nums = [10, 20, 30]
for index, number in enumerate(nums):
    print(f"Index: {index}, Number: {number}")
    
strings = ["Hello", "World", "!"]
for index, string in enumerate(strings):
    print(f"Index: {index}, String: {string}")