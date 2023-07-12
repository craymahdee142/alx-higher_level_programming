#!/usr/bin/python3
'''defines JSON file writing function'''

import json


def save_to_json_file(my_obj, filename):
    '''write object to a text fle using JSON representation'''
    with open(filename, "w") as file:
        json.dump(my_obj, file)
