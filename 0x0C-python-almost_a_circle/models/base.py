#!/usr/bin/python3
"""A base module"""


import json


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
