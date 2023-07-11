#!/usr/bin/python3
'''defines my class MyInt that inherits from Int'''


class MyInt(int):
    '''invert the opts == and !='''

    def __eq__(self, other):
        '''overide opt != with =='''
        return int(self) != other

    def __ne__(self, other):
        '''overide opt == with !='''
        return int(self) != other
