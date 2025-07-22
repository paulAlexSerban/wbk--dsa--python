def build_ferrari(color: str = "red"):
    string = f"Build a {color} Ferrari"
    print(string)
    return string


def greet(name: str):
    string = f"Hello {name}!"
    print(string)
    return string


def uppercase(text: str):
    string = text.upper()
    print(string)
    return string


def concatenate(text1: str, text2: str):
    string = f"{text1} {text2}"
    print(string)
    return string


def say_hi(name: str):
    string = greet(name)
    print(string)
    return string
