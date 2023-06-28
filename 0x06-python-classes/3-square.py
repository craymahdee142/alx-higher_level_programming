#!/usr/bin/python3


class Square:
    '''initialised a sqaure'''

    def __init__(self, size=0):
        ''' initialise a new square

        Args:
            int the size of the square
        '''
        if not isinstance(size, int):
            raise TpyeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
    '''define public instance method area'''
    def area(self):
        return (self.__size ** 2)
