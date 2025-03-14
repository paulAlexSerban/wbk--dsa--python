import two

print("top-level in three.py")

if __name__ == "__main__":
    print("three.py is being run directly")
else:
    print("three.py is being imported into another module from", __name__)