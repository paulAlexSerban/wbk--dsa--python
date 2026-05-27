class Spreadsheet(object):

    def __init__(self, rows):
        """
        :type rows: int
        """
        # 26 columns (A-Z), rows as given
        self.rows = rows
        self.cols = 26
        # Use a dictionary to store only set values: key = (row, col) -> value
        self.data = {}

    def parse_cell(self, cell):
        # cell: "A1", "B10", etc.
        col = ord(cell[0]) - ord('A')
        row = int(cell[1:]) - 1  # convert to 0-based index
        return row, col

    def setCell(self, cell, value):
        """
        :type cell: str
        :type value: int
        :rtype: None
        """
        row, col = self.parse_cell(cell)
        self.data[(row, col)] = value

    def resetCell(self, cell):
        """
        :type cell: str
        :rtype: None
        """
        row, col = self.parse_cell(cell)
        if (row, col) in self.data:
            del self.data[(row, col)]

    def get_cell_value(self, cell):
        # cell is like "A1"
        row, col = self.parse_cell(cell)
        return self.data.get((row, col), 0)

    def getValue(self, formula):
        """
        :type formula: str
        :rtype: int
        """
        # formula is "=X+Y", where X and Y are either cell references or integers
        assert formula[0] == '='
        expr = formula[1:]
        left, right = expr.split('+')

        def get_operand_value(operand):
            operand = operand.strip()
            if operand and operand[0].isalpha():
                # It's a cell
                return self.get_cell_value(operand)
            else:
                # It's a number
                return int(operand)

        return get_operand_value(left) + get_operand_value(right)