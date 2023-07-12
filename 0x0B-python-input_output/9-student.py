#!/usr/bin/python3
'''Defines a class fo students'''


class Student:
    '''Represenatation of student'''

    def __init__(self, first_name, last_name, age):
        '''initialization of a student

        Args:
           first_name (str): first name of student
           last_name (str): last name of student
           age (int): age of student
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''Get a dictionary represenation of a student'''
        return self.__dict__
