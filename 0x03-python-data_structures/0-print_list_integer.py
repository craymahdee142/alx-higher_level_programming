#!/usr/bin/python3
"""function that prints all integers in my list"""
def print_list_integer(my_list=[]):
    for i in range(len(my_list)):
        print("{:d}".format(my_list[i]))
