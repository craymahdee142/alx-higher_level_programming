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
        '''set the value of the square'''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        '''update the Square

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
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        except IndexError:
            pass

    def to_dictionary(self):
        '''return dict represenation of a Square'''
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        '''return the print and str() represenattion of a Square'''
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
