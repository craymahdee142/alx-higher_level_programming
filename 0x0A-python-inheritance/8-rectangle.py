#!/usr/bin/python3
'''defines a rectangle class but inherits from Basegeometry'''

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    '''rectangle represenataion'''
    def __init__(self, width, height):
        '''initialiseation of rectangle'''
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
