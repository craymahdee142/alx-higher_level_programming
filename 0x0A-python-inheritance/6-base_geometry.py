#!/usr/bin/python3
'''defines baseclass  class geometry'''


class BaseGeometry:
    '''class with publuc attributes'''
    def area(self):
        '''raises an exception when called'''
        raise Exception("area() is not implemented")
