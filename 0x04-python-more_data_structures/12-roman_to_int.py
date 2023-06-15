#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or len(roman_string) == 0:
        return 0
    val = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
        }
    ret = 0
    if not roman_string:
        return ret
    else:
        for i in range(len(roman_string)):
            if (i+1 < len(roman_string) and
                    val[roman_string[i+1]] > val[roman_string[i]]):
                ret -= val[roman_string[i]]
            else:
                ret += val[roman_string[i]]
        return ret
