class Solution:
    def romanToInt(self, s: str) -> int:

        rom_values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        # IV, IX, XL, XC, CD, CM

        result = 0

        s = (
            s.replace("IV", "IIII")
            .replace("IX", "VIIII")
            .replace("XL", "XXXX")
            .replace("XC", "LXXXX")
            .replace("CD", "CCCC")
            .replace("CM", "DCCCC")
        )

        # MDCCCCLXXXXIIII
        # rom_values["M"]
        for i in s:
            result += rom_values[i]

        return result

    romanToInt(s.("MCMXCIV"))
# Cigdem 's solution


# s.replace("IV","IIII").("IX","VIIII").("XL","XXXX").("XC","LXXXX").("CD","CCCC").("CM","DCCCC")