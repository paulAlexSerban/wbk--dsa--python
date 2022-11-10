# the while statement
# while EXPRESSION:
  # code block that runs if expression is TRUE
# else:
  # if EXPRESSION is FALSE
  # run this code and terminate loop

# while loop - tests a conditional expression and runs the body of the loop while the condition remains true

def login(username: str, password: str) -> bool:
  is_authenticated = False
  if username == "admin" and password == "1234":
    is_authenticated = True
  return is_authenticated

user = input("Username: ")
password = input("Password: ")

while login(user, password) == False:
  print("Login failed, re-enter credentials!")
  user = input("Username: ")
  password = input("Password: ")
print("Login successful")
