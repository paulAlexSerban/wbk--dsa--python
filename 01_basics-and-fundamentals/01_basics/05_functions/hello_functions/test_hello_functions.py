from hello_functions import greet, uppercase, concatenate, say_hi, build_ferrari


def test_greet():
    assert greet("Paul") == "Hello Paul!"
    assert greet("John") == "Hello John!"
    assert greet("George") == "Hello George!"
    assert greet("Ringo") == "Hello Ringo!"


def test_uppercase():
    assert uppercase("Paul") == "PAUL"
    assert uppercase("John") == "JOHN"
    assert uppercase("George") == "GEORGE"
    assert uppercase("Ringo") == "RINGO"


def test_concatenate():
    assert concatenate("Paul", "McCartney") == "Paul McCartney"
    assert concatenate("John", "Lennon") == "John Lennon"
    assert concatenate("George", "Harrison") == "George Harrison"
    assert concatenate("Ringo", "Starr") == "Ringo Starr"


def test_say_hi():
    assert say_hi("Paul") == "Hello Paul!"
    assert say_hi("John") == "Hello John!"
    assert say_hi("George") == "Hello George!"
    assert say_hi("Ringo") == "Hello Ringo!"


def test_build_ferrari():
    assert build_ferrari() == "Build a red Ferrari"
    assert build_ferrari("blue") == "Build a blue Ferrari"
    assert build_ferrari("yellow") == "Build a yellow Ferrari"
