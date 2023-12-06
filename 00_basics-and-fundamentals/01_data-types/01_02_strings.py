str = 'Hello World!'

print (str)          # Prints complete string
print (str[0])       # Prints first character of the string
print (str[2:5])     # Prints characters starting from 3rd to 5th
print (str[2:])      # Prints string starting from 3rd character
print (str * 2)      # Prints string two times
print (str + "TEST") # Prints concatenated string

#####################
# string formatting from python 3.6 onwards using f-strings
#####################
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

#####################
# string formatting from python 3.5 onwards using .format()
#####################
# default (implicit) order
default_order = "{}, {} and {}"
with_order = default_order.format('John','Bill','Sean')
print("\n--- Default Order ---")
print(default_order)
print(with_order)

# order using positional argument
positional_order = "{1}, {0} and {2}"
with_order = positional_order.format('John','Bill','Sean')
print("\n--- Positional Order ---")
print(positional_order)
print(with_order)

# order using keyword argument
keyword_order = "{s}, {b} and {j}"
with_order = keyword_order.format(j='John',b='Bill',s='Sean')
print("\n--- Keyword Order ---")
print(keyword_order)
print(with_order)

#####################
# string formatting from python 2.6 onwards using %
#####################
x = 10
y = 20
print("\n--- Python 2.6 onwards ---")
print("The value of x is %d and y is %d" % (x,y))

