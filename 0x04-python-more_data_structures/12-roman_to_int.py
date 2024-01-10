#!/usr/bin/python3
def roman_to_int(roman_string):

    if not isinstance(roman_string, str):
        return 0

    romandict = {'I': 1, 'V': 5, 'X': 10,
                 'L': 50, 'C': 100, 'D': 500, 'M': 100}
    numb = 0
    for i in range(len(roman_string)):
        if i < len(roman_string) - 1 and romandict[roman_string[i]] \
                < romandict[roman_string[i + 1]]:
            numb -= romandict[roman_string[i]]
        else:
            numb += romandict[roman_string[i]]

    return numb
