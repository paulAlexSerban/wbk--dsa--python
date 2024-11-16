size_input=input("How big is your house (in square feet): ")
# convert input to an integer
square_feet=int(size_input)
square_metres=square_feet/10.8
# :.2f means to format the number to 2 decimal places (f is for float)
print(f"{square_feet} square feet is {square_metres:.2f} square metres.")