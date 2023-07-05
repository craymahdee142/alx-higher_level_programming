#!/usr/bin/python3
'''
This is "0-add_integer" module, which supplies one function,
add_integer(a, b)
'''


def add_integer(a, b=98):
    '''returns addition of two numbers a and b.

    Float args are typecast before addition is done

    Raises:
        TypeError: if either a bor b in not integer and non float
    '''
    if not isinstance(a, int) and not isinstance(b, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer ")
    return int(a) + int(b)
