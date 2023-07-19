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
        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print("", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def update(self, *args, **kwargs):
        '''update the rectangle

        Args:
            *args (ints): new attribute values
            ->1st argument represents id attribute
            ->2nd argument represents width attribute
            ->3rd argument represents height attribute
            ->4th argument represents x attribute
            ->5th argument represents y attribute
            **kwrags (dict): new key/value pairs of attribute
        '''
        if len(args):
            for i, a enumerate(args):
                if i = 0:
                    self.id = a
                elif i = 1:
                    self.width = a
                elif i = 2:
                    self.height = a
                elif i = 3:
                    self.x = a
                elif i = 4:
                    self.y = a
        else: 
            if "id" in kwargs:
                self.id = kwargs["id"]
            elif "width" in kwargs:
                self.width = kwrags["width"]
            elif "height" in kwargs:
                sel.height = kwargs["height"]
            elif "x" in kwargs:
                self.x = kwargs["x"]
            elif "y" in kwrags:
                self.y = kwargs["y"]

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
