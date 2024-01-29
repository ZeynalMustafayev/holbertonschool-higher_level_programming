#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    res = 0
    prev_value = 0
    for symbol in reversed(roman_string):
        current_value = roman_values[symbol]
        if current_value >= prev_value:
            res += current_value
        else:
            res -= current_value
        prev_value = current_value

    return res
