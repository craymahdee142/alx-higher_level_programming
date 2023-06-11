#!/usr/bin/python3
"""function that prints all integers in my list"""
def print_list_integer(my_list=[]):
    my_list = [1, 2, 3, 4, 5]
    for item in my_list:
        if isintance(item, int):
            print("{}".format(item))
