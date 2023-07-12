#!/usr/bin/python3
'''defines a text appending function'''


def append_write(filename="", text=""):
    '''
    write a string to utf-8 text file

    Args:
        filename (str): name of file to write
        text (str): text to write into a file
    Returns:
        returns the number of written characters
    '''
    with open(filename, "a", encoding="utf-8") as file:
        file.write(text)
        return len(text)
