from value_error_exception import divide
import pytest


def test_divide_by_zero():
    with pytest.raises(ValueError, match="Division by zero is not allowed."):
        divide(10, 0)


def test_divide_valid():
    assert divide(10, 2) == 5.0
    assert divide(-10, 2) == -5.0
    assert divide(10, -2) == -5.0
    assert divide(-10, -2) == 5.0
    assert divide(0, 1) == 0.0
    assert divide(1, 1) == 1.0


def test_divide_by_zero_message():
    with pytest.raises(ValueError) as exc_info:
        divide(5, 0)
    assert str(exc_info.value) == "Division by zero is not allowed."
