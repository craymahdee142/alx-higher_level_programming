#!/usr/bin/python3
'''Define a square class'''


class Square:
    '''representinf square

    Args:i
        size of a square
    '''
    def __init__(self, size=0):
        '''square initialisation'''

        self.size = size

    @property
    def size(self):
        '''set or get the size of the square'''
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        '''return the area of square'''
        return (self.__size ** 2)

    def __eq__(self, other):
        '''define the == comparison to the square'''
        return self.area() == other.area()

    def __ne__(self, other):
        '''define the != comparison to the square'''
        return self.area() != other.area()

    def __lt__(self, other):
        '''define the < comparison to the square'''
        return self.area() < other.area()

    def __le__(self, other):
        '''define the <= comparison to the square'''
        return self.area() <= other.area()

    def __ge__(self, other):
        '''define the >= comparison to the square'''
        return self.area() > other.area()

    def __gt__(self, other):
        '''define the > comparison to the square'''
        return self.area() > other.area()
