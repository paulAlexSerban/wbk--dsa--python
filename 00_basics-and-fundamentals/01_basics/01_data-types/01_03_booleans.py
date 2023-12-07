is_empty = True
if_hidden = False

is_bigger = 10 > 20
print(is_bigger)

print(5 == 5) # is 5 equal to 5? True
print(5 == 10) # is 5 equal to 10? False
print(5 > 10) # is 5 greater than 10? False
print(5 != 10) # is 5 not equal to 10? True
print(5 <= 10) # is 5 less than or equal to 10? True
print(5 >= 10) # is 5 greater than or equal to 10? False

friends = ["Rolf", "Bob"]
abroad = ["Rolf", "Bob"]
print(friends == abroad) # True because the values are the same
print(friends is abroad) # False because they're not the same object

abroad = friends
print(friends is abroad) # True because they're the same object
