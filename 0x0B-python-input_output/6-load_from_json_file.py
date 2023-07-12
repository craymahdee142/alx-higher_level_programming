#!/usr/bin/python3
'''defines JSON file redaing function'''

import json


def load_from_json_file(filename):
    '''create a Python object from JSON file'''
    with open(filename) as file:
        return json.load(file)
