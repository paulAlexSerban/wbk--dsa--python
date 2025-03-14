def is_valid_index(index: int, list: list) -> bool:
  result = False
  if 0 <= index and index <= len(list):
    result = True
  return result
index = 3
list = ["test", "test1", "test2", "test3"]
print(f"Index {index} is valid" if is_valid_index(index, list) else f"Index {index} is out of range")

# common list methods in Python
# append(value)
# insert(value, index)
# pop(index)
# remove(value)