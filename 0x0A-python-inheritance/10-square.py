#!/usr/bin/python3
'''contains a class BaseGeometry and subclass Rectangle'''


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    '''representation of square'''
    def __init__(self, size):
        '''square initialisation'''
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        '''returns square of area'''
        return self.__size**2
