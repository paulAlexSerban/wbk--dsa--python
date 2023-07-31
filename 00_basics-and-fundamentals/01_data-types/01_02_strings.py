str = 'Hello World!'

print (str)          # Prints complete string
print (str[0])       # Prints first character of the string
print (str[2:5])     # Prints characters starting from 3rd to 5th
print (str[2:])      # Prints string starting from 3rd character
print (str * 2)      # Prints string two times
print (str + "TEST") # Prints concatenated string

partOne = "Stay hungry"
partTwo = "Stay foolish"
quote = f"{partOne} {partTwo}"
print(quote)

name = "Paul"
age = "31"
message = f"Your name is {name} and your age is {age}"
print(message)

car = "tesla Roadster"
acceleration = 1.9
newMessage = f"The {car} goes 0-60 mph in {acceleration} seconds"
print(newMessage)

string_length = len(newMessage)
print(string_length)

uppercase_message = newMessage.upper()
print(uppercase_message)

lowercase_message = newMessage.lower()
print(lowercase_message)
