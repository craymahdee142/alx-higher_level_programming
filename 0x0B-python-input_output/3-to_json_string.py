#!/usr/bin/python3
'''defines a string to json function'''

import json


def to_json_string(my_obj):
    '''returns json representation of an obj'''
    return json.dumps(my_obj)
