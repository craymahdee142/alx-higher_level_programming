#!/usr/bin/python3
'''represent is the same class'''


def inherits_from(obj, a_class):
    '''
    check if an object is exactly same as instance of a given class

    Args:
       obj (any): boject to check
       a_class (int): the class to mark type of object
    Returns:
        returns true if object is same as instance of a_class or false if fails
    '''
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
