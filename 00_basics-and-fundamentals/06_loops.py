for i in range(10):
    print(i)

quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""

# Use a for loop and an if statement to print just the capitals in the quote above.
for char in quote:
    if char.isupper():
        print(char)

# This solution uses a step value for the range function
for i in range(0, 101, 7):
    print(i)

# This solution uses a slice
for i in range(101)[::7]:
    print(i)

for i in range(0, 100, 7):
    print(i)
    if i > 0 and i % 11 == 0:
        break

for x in range(21):
    if x % 3 == 0 or x % 5 == 0:
        continue
    print(x)