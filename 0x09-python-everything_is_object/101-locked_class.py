#!/usr/bin/python3
'''defines a class'''


class LockedClass:
    '''class that locks a class and prevents
       user from dynamically creating new instance attributes,
       except if the new attribute is called first_name
       '''

    __slots__ = ["first_name"]
