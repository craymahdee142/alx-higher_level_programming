#!/usr/bin/python3
'''represent is the same class'''


def is_kind_class(obj, a_class):
    '''
    check if an object is an instance or inherited instance of a given class

    Args:
       obj (any): boject to check
       a_class (int): the class to mark type of object
    Returns:
        returns true if object is same as instance of a_class or false if fails
    '''
    if isinstance(obj, a_class):
        return True
    return Fasle
