#!/usr/bin/python3
'''Defines name printing function'''


def say_my_name(first_name, last_last=""):
    '''print a name

    Args:
        first_name (str): first_name to print
        last_name (str): last_name to print
    Raises:
        TypeError: if either first or last name is string
    '''
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(lastt_name, str):
        raise TypeError("lastt_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
