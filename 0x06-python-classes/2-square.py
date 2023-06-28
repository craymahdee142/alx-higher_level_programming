#!/usr/bin/python3

''' define a class square'''


class Square:
    '''represent a square'''

    def __init__(self, size=0):
        ''' initialise a new square

        Args:
            int the size of the square
        '''
        if not isinstance(size, int):
            raise TypeError("size must be integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
