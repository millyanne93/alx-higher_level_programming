#!/usr/bin/python3

def convert_roman(ch):
    """
    Converts a Roman numeral character into the respective integer.
    
    Args:
        ch (str): The Roman numeral character (I, V, X, L, C, D, or M).

    Returns:
        int: The corresponding integer value for the given Roman numeral character.
    """
    roman_to_int_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    return roman_to_int_map.get(ch, -1)

def roman_to_int(roman_string):
    """
    Converts a string of Roman numerals to decimal.

    Args:
        roman_string (str): The input string containing Roman numerals.

    Returns:
        int: The decimal value of the given Roman numeral string.
    """
    if not isinstance(roman_string, str):
        return 0

    total = 0
    prev_value = 0

    for ch in reversed(roman_string):
        cur_value = convert_roman(ch)
        if cur_value >= prev_value:
            total += cur_value
        else:
            total -= cur_value
        prev_value = cur_value

    return total
