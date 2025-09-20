import unittest

from spreadsheet import Spreadsheet

class TestSpreadsheet(unittest.TestCase):
    def setUp(self):
        self.spreadsheet = Spreadsheet(10)  # 10 rows

    def test_set_and_get_cell(self):
        self.spreadsheet.setCell("A1", 5)
        self.assertEqual(self.spreadsheet.get_cell_value("A1"), 5)

        self.spreadsheet.setCell("B2", 10)
        self.assertEqual(self.spreadsheet.get_cell_value("B2"), 10)

    def test_reset_cell(self):
        self.spreadsheet.setCell("A1", 5)
        self.spreadsheet.resetCell("A1")
        self.assertEqual(self.spreadsheet.get_cell_value("A1"), 0)

    def test_get_value_with_cells(self):
        self.spreadsheet.setCell("A1", 5)
        self.spreadsheet.setCell("B2", 10)
        self.assertEqual(self.spreadsheet.getValue("=A1+B2"), 15)

    def test_get_value_with_numbers(self):
        self.assertEqual(self.spreadsheet.getValue("=3+7"), 10)
        self.assertEqual(self.spreadsheet.getValue("=0+0"), 0)

    def test_get_value_with_mixed(self):
        self.spreadsheet.setCell("A1", 5)
        self.assertEqual(self.spreadsheet.getValue("=A1+3"), 8)
        self.assertEqual(self.spreadsheet.getValue("=4+B2"), 4)  # B2 is unset, defaults to 0

    def test_get_value_with_whitespace(self):
        self.spreadsheet.setCell("A1", 5)
        self.spreadsheet.setCell("B2", 10)
        self.assertEqual(self.spreadsheet.getValue("= A1 + B2 "), 15)
        self.assertEqual(self.spreadsheet.getValue("=   3   +   7   "), 10)

    def test_problems_case(self):
        self.assertEqual(self.spreadsheet.getValue("=5+7"), 12)
        self.spreadsheet.setCell("A1", 10)
        self.assertEqual(self.spreadsheet.getValue("=A1+6"), 16)
        self.spreadsheet.setCell("B2", 15)
        self.assertEqual(self.spreadsheet.getValue("=A1+B2"), 25)
        self.spreadsheet.resetCell("A1")
        self.assertEqual(self.spreadsheet.getValue("=A1+B2"), 15)
