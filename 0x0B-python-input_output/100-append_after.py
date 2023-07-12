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
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            lines += [line]
            if line.find(search_string) != -1:
                lines += [new_string]

    with open(filename, "w", encoding="utf-8") as file:
        file.writelines(lines)
