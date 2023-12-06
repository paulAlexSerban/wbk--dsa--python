data = [
    "Andromeda - Shrub",
    "Bellflower - Flower",
    "China Pink - Flower",
    "Daffodil - Flower",
    "Evening Primrose - Flower",
    "French Marigold - Flower",
    "Hydrangea - Shrub",
    "Iris - Flower",
    "Japanese Camellia - Shrub",
    "Lavender - Shrub",
    "Lilac - Shrub",
    "Magnolia - Shrub",
    "Peony - Shrub",
    "Queen Anne's Lace - Flower",
    "Red Hot Poker - Flower",
    "Snapdragon - Flower",
    "Sunflower - Flower",
    "Tiger Lily - Flower",
    "Witch Hazel - Shrub",
]
print(data)
print(len(data)) # prints the length of the list
print("test" in data) # prints True if the element is in the list
print(data[0]) # prints the first element in the list
print(data[-1]) # prints the last element in the list
print(data[0:3]) # prints the first three elements in the list

# lists are mutable - so we can add or remove items from it
data.append("test") # adds an element to the list
print(data)
data.insert(0, "test") # adds an element to the list
print(data)
print(data.count("test")) # prints the number of times the element appears in the list
data.remove("test") # removes an element from the list
print(data)
data.pop() # removes an element from the list
print(data)
data.clear() # removes all elements from the list
print(data)
del data # deletes the list
# print(data) # throws an error because the list has been deleted
