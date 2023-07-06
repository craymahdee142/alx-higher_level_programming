#!/usr/bin/python3
'''define a rectangle'''


class Rectangle:
    '''represent a rectangle

    Attributes:
            number_of_instnace (int): number rect instances
            print_symbol (any): symbol used for string representation
    '''

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        '''
        initialise a new rectangle

        Args:
            width (int): width of a new rectangle
            height (int): height of a new recatngle
        '''
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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

    @classmethod
    def square(cls, size=0):
        '''return a new rectangle instance width == height == size'''
        return cls(size, size)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        '''
        Compares two rectangle and returns one with biggest area.

        Args:
            rect_1 (Rectangle): firts rectangle
            rect_2 (Rectangle): second rectangle

        Raises:
            TypeError: if either rect_1, or rect_2
            is not an instance of rectangle.
        '''
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    def __str__(self):
        '''print a string representation of rectangle'''
        if self.width == 0 or self.height == 0:
            return ""
        rect_str = ""
        for i in range(self.height):
            rect_str += str(self.print_symbol) * self.width
            if i < self.height - 1:
                rect_str += '\n'
        return (rect_str)

    def __repr__(self):
        '''return a string representation of rectangle'''
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        '''print message when instance rectangle is deleted'''
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
