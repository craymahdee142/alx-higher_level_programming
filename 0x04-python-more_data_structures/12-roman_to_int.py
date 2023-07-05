#!/usr/bin/python3
def roman_to_int(roman_string):
    # check if input is None or not a string
    if roman_string is None or not isinstance(roman_string, str):
        return (0)
    data = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    # create list of integer value corp. to each symbol in roman_string
    numbers = [data[x] for x in roman_string] + [0]
    result = 0
    for i in range(len(numbers) - 1):
        if numbers[i] >= numbers[i + 1]:
            result += numbers[i]
        else:
            result -= numbers[i]
    return (result)
