# Hash Map (Dictionary in Python): A hash map is a data structure that stores key-value pairs. In 
# Python, dictionaries are used as hash maps. They provide efficient lookup, insert, and delete operations.

phone_book = {"Alice": "123-456-7890", "Bob": "987-654-3210"}
print(phone_book["Alice"])  # Returns "123-456-7890"

animals = {
  "lion": ["scary", "big", "cat"],
  "elephant": ["big", "grey", "wrinkled"],
  "teddy": ["cuddly", "stuffed"],
}
print(animals["lion"])  # Returns ["scary", "big", "cat"]

# Checking Existence in Hash Map: The solution often involves checking if a certain value exists in the hash map. 
# This is done to find if the complementary number (the difference calculated) is already in the list.
# Example:

nums_dict = {2: 0, 7: 1, 11: 2}  # Suppose the dictionary holds numbers and their indices
if 7 in nums_dict:
    print("7 exists in the dictionary")
    
# Iterating through Hash Map: Iterating through a hash map is similar to iterating through a list.
# Example:

phone_book = {"Alice": "123-456-7890", "Bob": "987-654-3210"}
for key in phone_book:
    print(key, phone_book[key])