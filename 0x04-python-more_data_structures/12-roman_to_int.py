#!/usr/bin/python3

def convert_roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0

    rom_n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    total = 0
    prev_value = 0

    for ch in roman_string:
        value = rom_n.get(ch, 0)
        total += value - 2 * prev_value if value > prev_value else value
        prev_value = value

    return total
