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

    def to_json(self, attrs=None):
        '''Get a dictionary represenation of a student

        If attrs is a list of strings, only attribute
        '''
        if (type(attrs) == list and all(type(element) == str for element in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        '''replace all attributes of a student

        Args:
            json (dict): the dictionary containing key-value pairs to replace the attributes
        '''
        for key, value in json.items():
            setattr(self, key, value)
