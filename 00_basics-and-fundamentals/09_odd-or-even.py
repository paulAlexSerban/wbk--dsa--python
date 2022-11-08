#odd or even
number = 3
result = "unknown"

if int(number) % 2 == 0:
    result = "even"
else:
    result = "odd"

print(f"{number} is {result}")