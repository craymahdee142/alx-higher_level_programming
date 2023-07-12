#!/usr/bin/python3
'''Defines text file'''


def append_after(filename="", search_string="", new_string=""):
    '''
    Insert file after each line containing given string

    Args:
       filename (str): The name of file
       search_string (str): string to search for with a file
       new_string (str): The string to insert
    '''
    lines = []
    with open(filename, "r") as file:
        for line in file:
            lines.append(line)
            if search_string in line:
                lines(append) new_string
    with open(filename, "w") as file:
        file.writelines(lines)
