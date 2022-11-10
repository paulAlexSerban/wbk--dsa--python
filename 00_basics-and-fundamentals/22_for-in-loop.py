# the for-in loop
# for var in sequence
  # code block that runs
  # for each element in the sequence

# range(START, STOP, STEP)
for index in range(100):
  if index % 2 == 0: continue
  print(f"{index} - iteration count {index + 1}")

# while expression: runs while EXPRESSION is TRUE
# for var in sequence: runs for each element in the sequence

def login(username: str, password: str) -> bool:
  is_authenticated = False
  if username == "admin" and password == "1234":
    is_authenticated = True
  return is_authenticated

username = input("Username: ")
password = input("Password: ")

is_authenticated = False

for attempt in range(4):
  if login(username, password) == True:
    is_authenticated = True
    break
  else:
    print("Login failed, reenter your credentials")
    username = input("Username: ")
    password = input("Password: ")

print("Login successful" if is_authenticated else "Your account has been temporarily locked")