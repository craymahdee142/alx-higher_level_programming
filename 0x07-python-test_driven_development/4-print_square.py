#!/usr/bin/python3
'''Defines print square function'''


def print_square(size):
    '''print a square with char #

    Args:
        size (int): width or height of square
    Raises:
        TypeError: if siz is not an integer
        ValueError: if size is < 0
    '''
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size, end="")
        print("")
