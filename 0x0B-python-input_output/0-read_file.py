#!/usr/bin/python3
'''defines a text file file reading'''


def read_file(filename=""):
    '''prints the content of UTF-8 to the stdout'''
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
