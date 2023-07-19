#!/usr/bin/python3
'''Defines a rectangle class'''

from models.base import Base


class Rectangle(Base):
    '''represent a new Rectangle'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''initialize the rectangle class


        Args:
            width (int): the width of the new Rectangle.
            height (int): the height of the new Rectangle
            x (int): the x coordinate of the new Rectangle
            y (int): the y coordinate of the new Rectangle
            id (int): the identity of the new Rectangle
       Raises:
            TypeError: if either of width or height is not int
            ValueError: if either of width or height <= 0
            TypeError: if either of x or y is not an int
            ValueError: if either of x y < 0
        '''
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        '''get the width of the Rectangle'''
        return self.__width

    @width.setter
    def width(self, value):
        '''set width of the rectangle'''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        '''get the heigth of the Rectangle'''
        return self.__height

    @height.setter
    def height(self, value):
        '''set width of the rectangle'''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        '''get the x of the Rectangle'''
        return self.__x

    @x.setter
    def x(self, value):
        '''set width of the rectangle'''
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        '''get the y of the Rectangle'''
        return self.__y

    @y.setter
    def y(self, value):
        '''set width of the rectangle'''
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        '''Return the area of the rectangle'''
        return self.__width * self.__height

    def display(self):
        '''print the rectangle using '#' char'''
        if self.width == 0 or self.height == 0:
            print("")
            return
        for y in range(self.y):
            print("")
        for h in range(self.height):
            if self.x == 0:
                for w in range(self.width):
                    print("#", end="")
            else:
                for x in range(self.x):
                    print(" ", end="")
                for w in range(self.width):
                    print("#", end="")
            print("")

    def update(self, *args, **kwargs):
        '''update the rectangle

        Assign key/value arguments to attributes
        kwargs is skipped if args is not empty

        Args:
            *args - variable number of no keyword args
            **kwargs - variable number of keyword args
        '''
        if len(args) == 0:
            for key, value in kwargs.items():
                self.__setter__(key, value)
            return

        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass

    def to_dictionary(self):
        '''Return the dictionary represenatation of a rectangle'''
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        '''return the print and str() representation of the rect'''
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)
