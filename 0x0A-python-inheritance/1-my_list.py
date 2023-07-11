#!/usr/bin/python3
'''represent a MyList class'''


class MyList(list):
    '''sunclass of list'''
    def __init__(self):
        '''initialise the object'''
        super().__init__()

    def print_sorted(self):
        '''print sorted list of an object'''
        print(sorted(self))
