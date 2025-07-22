from celsius_to_fahrenheit import celsius_to_fahrenheit
import pytest
import sys
# Skip tests on non-Windows platforms
# This is just an example; you can adjust the condition as needed.
# For instance, you might want to skip tests on Python versions greater than 3.11
# pytestmark = pytest.mark.skipif(sys.platform != "win32", reason="Skipping tests on Windows")

def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(100) == 212
    assert celsius_to_fahrenheit(-40) == -40
    assert celsius_to_fahrenheit(37) == 98.6

@pytest.mark.skip(reason="Skipping test for Celsius to Fahrenheit conversion")
def test_celsius_to_fahrenheit_negative():
    assert celsius_to_fahrenheit(-10) == 14
    assert celsius_to_fahrenheit(-20) == -4
    assert celsius_to_fahrenheit(-30) == -22

@pytest.mark.skipif(sys.version_info > (3, 11), reason="Requires Python 3.11 or lower")
def test_celsius_to_fahrenheit_float():
    assert celsius_to_fahrenheit(25.5) == 77.9
    assert celsius_to_fahrenheit(37.5) == 99.5
    assert celsius_to_fahrenheit(-15.5) == 4.100000000000001
    
def test_celsius_to_fahrenheit_edge_cases():
    assert celsius_to_fahrenheit(0.0) == 32.0
    assert celsius_to_fahrenheit(100.0) == 212.0
    assert celsius_to_fahrenheit(-40.0) == -40.0