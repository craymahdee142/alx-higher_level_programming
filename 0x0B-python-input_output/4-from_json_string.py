#!/usr/bin/python3
'''defines JSON to string function'''

import json


def form_json_string(my_str):
    '''returns Python data structure represented by JSON string'''
    return json.loads(my_str)
