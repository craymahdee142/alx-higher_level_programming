#!/usr/bin/python3

'''define a class'''


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

    def area(self):
        '''return area of square'''
        return (self.__size ** 2)
