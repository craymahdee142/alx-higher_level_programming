#!/usr/bin/python3

'''define a square'''


class Square:
    '''represent a square'''

    def __init__(self, size=0):
        ''' initialise a new square

        Args:
            int the size of the square
        '''
        self.__size = size

    @property
    def size(self):
        '''get the current square size'''
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        '''return the area of size'''
        return (self.__size ** 2)
