#!/usr/bin/python3
def convert_roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
        return 0

    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result, prev_value = 0, 0

    for numeral in reversed(roman_string):
        value = roman_numerals.get(numeral, 0)
        result += value if value >= prev_value else -value
        prev_value = value

    return result
