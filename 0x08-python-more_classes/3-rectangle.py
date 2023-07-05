#!/usr/bin/python3
'''define a rectangle'''


class Rectangle:
    '''represent a rectangle'''

    def __init__(self, width=0, height=0):
        '''
        initialise a new rectangle

        Args:
            width (int): width of a new rectangle
            height (int): height of a new recatngle
        '''
        self.height = height
        self.width = width

    @property
    def width(self):
        '''get or set the width of the rectangle'''
        return (self.__width)

    @width.setter
    def width(self, value):
        '''
        set width of a new rectangle

        Args:
            value (int): width value of a rectangle

        Raises:
            TypeError: raises error if value is not an integer
            ValueError: raises error if value is less than 0
        '''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''get or set the height of the rectangle'''
        return (self.__height)

    @height.setter
    def height(self, value):
        '''
        set height of a new rectangle

        Args:
            value (int): height value of a rectangle

        Raises:
            TypeError: raises error if value is not an integer
            ValueError: raises error if value is less than 0
        '''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''calc and return the area of rectangle'''
        return (self.__width * self.__height)

    def perimeter(self):
        '''calc and return the perimeter of the rectangle'''
        if self.width == 0 or self.height == 0:
            return (0)
        return (2 * (self.__width + self.__height))

    def __str__(self):
        '''return a string representation of rectangle'''
        if self.width == 0 or self.height == 0:
            return ""
        rect_str = ""
        for i in range(self.height):
            rect_str += '#' * self.width
            if i < self.height -1:
                rect_str += '\n'
        return (rect_str)
