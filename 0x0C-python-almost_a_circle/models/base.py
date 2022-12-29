#!/usr/bin/python3
"""A base module"""


import json
import csv
import os
import turtle


class Base:
    """A base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """A class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """list to dict"""
        if not list_dictionaries or list_dictionaries == "[]":
            return ("[]")
        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """Save list objs dict to a file"""
        name = cls.__name__+'.json'
        dict_repr = []
        if list_objs is None:
            dict_repr = []
        else:
            for i in list_objs:
                dict_repr.append(i.to_dictionary())
        new = Base.to_json_string(dict_repr)
        with open(name, 'w') as f:
            f.write(new)

    @staticmethod
    def from_json_string(json_string):
        """a static method that converts to dict from json string"""
        if not json_string or json_string == "":
            return ([])
        else:
            return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """a class method that creates an instance and uses it"""
        if cls.__name__ == 'Rectangle':
            new = cls(1, 1)
        elif cls.__name__ == 'Square':
            new = cls(1)
        new.update(**dictionary)
        return (new)

    @classmethod
    def load_from_file(cls):
        """a Tmp documentation"""

        filename = cls.__name__ + ".json"
        json_string = ""
        result = []

        if os.path.exists('./{:s}'.format(filename)):
            with open(filename, mode="r", encoding="utf-8") as _file:
                json_string = _file.read()

            list_of_instances = cls.from_json_string(json_string)
            for instance in list_of_instances:
                result.append(cls.create(**instance))

        return (result)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Save in a csv file a list of objs (Rectangles or Squares)
        """
        result = []
        namefile = cls.__name__ + ".csv"
        options = ["Rectangle", "Square"]
        name = ""

        if (list_objs is not None and len(list_objs)):
            name = type(list_objs[0]).__name__
            if (name in options):
                if all((type(obj).__name__ == name) for obj in list_objs):
                    result = [list(obj.to_dictionary().values())
                              for obj in list_objs]

        with open(namefile, "w", encoding="utf-8") as _file:
            for data in result:
                _file.write(','.join(str(data)[1:-1].split(', ')) + '\n')

    @classmethod
    def load_from_file_csv(cls):
        """
        Read a CSV file and create instances from the dicts
        """

        filename = cls.__name__ + ".csv"
        rectangle_props = ["id", "width", "height", "x", "y"]
        square_props = ["id", "size", "x", "y"]
        result = []

        if os.path.exists("./{:s}".format(filename)):
            with open(filename, mode="r", encoding="utf-8") as _file:
                data_csv = csv.reader(_file)
                if (cls.__name__ == "Rectangle"):
                    for data in data_csv:
                        new_dict = {}
                        for key, value in zip(rectangle_props, data):
                            new_dict[key] = int(value)
                        result.append(cls.create(**new_dict))
                elif (cls.__name__ == "Square"):
                    for data in data_csv:
                        new_dict = {}
                        for key, value in zip(square_props, data):
                            new_dict[key] = int(value)
                        result.append(cls.create(**new_dict))

        return (result)

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Takes all instances based with the class Base
        and draws it.
        """
        turtle.color('purple', 'lightblue')
        turtle.speed(4)
        turtle.shape('turtle')

        if all(inst.__class__.__name__ == 'Rectangle'
               for inst in list_rectangles):
            for rectangle in list_rectangles:
                turtle.goto(rectangle.x, rectangle.y)
                for _ in range(4):
                    turtle.pendown()
                    turtle.fd(rectangle.width)
                    turtle.rt(90)
                    turtle.fd(rectangle.height)
                    turtle.penup()

        if all(inst.__class__.__name__ == 'Square'
               for inst in list_squares):
            for square in list_squares:
                turtle.goto(square.x, square.y)
                for _ in range(4):
                    turtle.pendown()
                    turtle.fd(square.size)
                    turtle.rt(90)
                    turtle.penup()

        turtle.done()
