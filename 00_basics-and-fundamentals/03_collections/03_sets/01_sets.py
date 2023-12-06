# sets are unordered collections of unique elements
# sets are mutable - so we can add or remove items from it
sets = {"test", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"}
print(sets)
print(len(sets)) # prints the length of the set
print("test" in sets) # prints True if the element is in the set
print("test" not in sets) # prints True if the element is not in the set
sets.add("eleven") # adds an element to the set
print(sets)
sets.remove("eleven") # removes an element from the set
print(sets)
sets.discard("ten") # removes an element from the set
print(sets)
sets.pop() # removes an element from the set
print(sets)
sets.clear() # removes all elements from the set
print(sets)
del sets # deletes the set
# sets.pop() # throws an error because the set has been deleted