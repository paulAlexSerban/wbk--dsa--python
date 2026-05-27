class DecimalConverter:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        result = []

        # Handle sign
        if (numerator < 0) ^ (denominator < 0):
            result.append("-")

        n, d = abs(numerator), abs(denominator)
        # Integer part
        integer_part = n // d
        result.append(str(integer_part))

        remainder = n % d
        if remainder == 0:
            return ''.join(result)
        
        result.append(".")
        # Map from remainder -> index in result
        rem_pos = {}
        while remainder != 0:
            if remainder in rem_pos:
                # Insert parentheses
                idx = rem_pos[remainder]
                result.insert(idx, "(")
                result.append(")")
                break
            rem_pos[remainder] = len(result)
            remainder *= 10
            digit = remainder // d
            result.append(str(digit))
            remainder = remainder % d

        return ''.join(result)