def login(username: str, password: str) -> bool:
  is_authenticated = False
  if username == "admin" and password == "1234":
    is_authenticated = True
  return is_authenticated

user = input("Username: ")
password = input("Password: ")

logged_in = login(user, password)

# message = "Login failed, check your credentials"

# if logged_in:
#   message = "Login successful!"

# print(message)

print("Login successful!" if logged_in else "Login failed!")

# Conditional expression
# EXPRESSION if CONDITION else EXPRESSION_B