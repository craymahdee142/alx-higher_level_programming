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


class Rectangle(BaseGeometry):
    '''rectangle represenataion'''
    def __init__(self, width, height):
        '''initialiseation of rectangle'''
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        '''return area of rectangle'''
        return self.__width * self.__height

    def __str__(self):
        '''informal string represenatation of  a rectangle'''
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
