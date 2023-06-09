#!/usr/bin/python3

'''define a class'''


class Square:
    '''square representation'''

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        '''get the current size'''
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        '''get current position'''
        return (self.__position)

    @position.setter
    def position(self, postion):
        if not isintance(value, tuple) or len(value) != 2 or \
                not all(isinstance(posi, int) for posi in value) or \
                not all(posi >= 0 for posi in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        '''area of the square'''
        return (self.__size ** 2)

    def my_print(self):
        '''print square with char #'''
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__position[1]):
                print("")
            for j in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
