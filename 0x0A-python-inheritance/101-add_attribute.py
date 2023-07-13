#!/usr/bin/python3
'''Add new attr to an object if possible'''


def add_attribute(obj, attr_name, attr_value):
    '''
    Add new attr to an object if possible

    Args::
        obj (object): object to which attr should be added
        attr_name (str): name of attribut
        attr_value (any): The value of the attr to be added

    Raises:
        if the object does not allow adding new attr
    Returns: None
    '''

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr_name,  attr_value)
