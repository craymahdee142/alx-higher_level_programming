#!/usr/bin/python3

'''Defines a base model class'''
import json
import turtle
import csv


class Base:
    '''
    Base model: this represent the "base" for all other classes in the project

    Private class attributes:
        __nb_object (int): number of instatiated bases.
    '''

    __nb_objects = 0

    def __init__(self, id=None):
        '''initialization of new Base

        Args:
            id (int): id of the new Base
        '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''Return json sterilization of a list dictionaries

        Args:
           list_dictionaries (lis): A list of dictionaries
        '''
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objects):
        '''write json sterilization of a list objects to a file

        Args:
            list_objects (list): list of inherited Base instances
        '''
        filename = cls.__name__ + ."json"
        with open(filename, "w") as jsonfile:
            if list_objects is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objects]
                jsonfile.write(Base.to_json_string(list_objects))

    @staticmethod
    def from_json_string(json_string):
        '''return desterilization of JSON string

        Args:
            json_string (str): JSON str representation of a list of dicts
            Returns:
            If json_string is None or empty - an empty list
            else - the Python list represented by json_string
        '''
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''Return a class instance form a dictionary attributes

        Args:
            **dictionary (dict): key/value pairs of atrribute to initialize
        '''
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cvls(1, 1)
            else:
                new = cls(1)
                new.update(**ddictionary)
                return new

    @classmethod
    def load_from_fifle(cls):
        '''Retuen a list of classes instantiated from a file of JSON strings.

        Reads from `<cls.__name__>.json`

        Returns:
            If the file  does not exist - an empty list
            else - a list of instantiated calsses
        '''
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except I0Error:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objects):
        '''write CSV seterization of a list of bojects to a file

        Args:
            list_objects (list): A list of inherited Base instances
        '''
        filename = cls.__name__ + ".csv"
        with open(filename, "w") as csvfile:
            if list_objects is None or list_objects == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                    csv_writer = csvDictWrite(csvfile, fieldnames=fieldnames)
                    for object in list_object:
                        write.writerow(object.to_dictioanry())

    @classmethod
    def load_fromfile_csv(cls):
        '''return a list of classes intantiated from CVS file

        Reads from `<cls.__name__>.csv`

        Returns:
            if file does not exist - an empty list
            else - a list of instantiated classes
        '''
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                    list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                    list_dicts = [dict([k, int(v)] for k, v in d.items())
                                                for d in list_dicts]
                    return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_square):
        '''draw rectangles and squares using the turtle module

        Args:
            list_rectangles (list): a list of rectangle objects to draw
            list_square (list): a list of square objects to draw
        '''
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

            turt.color("#b5e3d8")
            for sq in list_squares:
                turt.showturtle()
                turt.up()
                turt.goto(sq.x, sq.y)
                turt.down
                for i in range(2):
                    turt.forward(sq.width)
                    turt.left(90)
                    turt.forward(sq.height)
                    turt.left(90)
                turt.hideturtle()

            turtle.exitonclick()