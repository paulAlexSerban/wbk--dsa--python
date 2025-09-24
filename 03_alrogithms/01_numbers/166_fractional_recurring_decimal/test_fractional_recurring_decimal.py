import unittest

from fractional_recurring_decimal import DecimalConverter

class TestDecimalConverter(unittest.TestCase):

    def setUp(self):
        self.converter = DecimalConverter()

    def test_fractionToDecimal(self):
        self.assertEqual(self.converter.fractionToDecimal(1, 2), "0.5")
        self.assertEqual(self.converter.fractionToDecimal(2, 1), "2")
        self.assertEqual(self.converter.fractionToDecimal(2, 3), "0.(6)")
        self.assertEqual(self.converter.fractionToDecimal(1, 6), "0.1(6)")
        self.assertEqual(self.converter.fractionToDecimal(0, 1), "0")

    def test_negative(self):
        self.assertEqual(self.converter.fractionToDecimal(-1, 2), "-0.5")
        self.assertEqual(self.converter.fractionToDecimal(1, -2), "-0.5")
        self.assertEqual(self.converter.fractionToDecimal(-1, -2), "0.5")

    def test_large_numbers(self):
        self.assertEqual(self.converter.fractionToDecimal(1, 333), "0.(003)")
        self.assertEqual(self.converter.fractionToDecimal(1, 6), "0.1(6)")
        self.assertEqual(self.converter.fractionToDecimal(22, 7), "3.(142857)")