#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    my_list = a_dictionary.copy()
    for k, v in my_list.items():
        if value == v:
            a_dictionary.pop(k)
    return (a_dictionary)
