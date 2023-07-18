#!/usr/bin/python3
'''defines square class'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''Represent a square'''

    def __init__(self, size, x=0, y=0, id=None):
        '''initialize a new square

        Args:
            size (int): the size of the new Square
            x (int): the x coordinate of the new Square
            y (int): the x coordinate of the new Square
            id (int): the identity of the new Square
        '''
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        '''get the size of the Square'''
        return self.width

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

        self.width = value
        self.height = value

    def update(self, *args, **kargs):
        '''update the Square

        Args:
            *args (ints): new attribute values
            ->1st argument represents id attribute
            ->2st argument represents width attribute
            ->3st argument represents height attribute
            ->4st argument represents x attribute
            ->5st argument represents y attribute
            **kwrags (dict): new key/value pairs of attribute
        '''
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                    elif a == 1:
                        self.size = arg
                    elif a == 2:
                        self.x = arg
                    elif a == 3:
                        self.y = arg
                    a += 1

        elif kwrags and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                    elif k == "size":
                        self.size = v
                    elif k == "x":
                        self.x = v
                    elif k == "y":
                        self.y = v

    def to_dictionary(self):
        '''return dict represenation of a Square'''
        return {
            "id": self.id
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        '''return the print and str() represenattion of a Square'''
        return "[Square] ({} {}/{} - {}".format(self.id, self.x, self.y,
                                                        self.width)




