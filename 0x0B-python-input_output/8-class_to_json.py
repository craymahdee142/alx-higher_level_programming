#!/usr/bin/python3
'''functionnthat returns a dictionary description with simple
data structure for JSON serialization of boject
'''

def class_to_json(obj):
    '''Function that returns dict description of an object'''
    result = {}
    if hasattr(obj, "__dict__"):
        result = obj.__dict__.copy()
    return (result)
