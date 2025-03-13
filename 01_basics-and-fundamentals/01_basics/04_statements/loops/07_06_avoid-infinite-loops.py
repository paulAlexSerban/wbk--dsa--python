def login(username: str, password: str) -> bool:
  is_authenticated = False
  if username == "admin" and password == "1234":
    is_authenticated = True
  return is_authenticated

user = input("Username: ")
password = input("Password: ")

attempt = 1
max_attempts = 5
is_authenticated = False

while login(user, password) == False:
  attempt += 1
  if attempt > max_attempts: break # terminate loop instantly
  print("Login failed, re-enter credentials!")
  user = input("Username: ")
  password = input("Password: ")
else:
  is_authenticated = True
  print("Login successful")

if not is_authenticated:
  print("Your account has been temporarily locked")