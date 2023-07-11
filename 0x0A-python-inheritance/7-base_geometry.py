#!/usr/bin/python3
'''defines baseclass  class geometry'''


class BaseGeometry:
    '''class with publuc attributes'''
    def area(self):
        '''raises an exception when called'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''validate parameter of an integer

        Args:
            name (str): name of parameter
            value (int): parameter to validetes
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is <= 0
        '''
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
