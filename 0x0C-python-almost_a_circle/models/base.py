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

    @staticmethod
    def save_to_file(cls, list_objs):
        """Save list objs dict to a file"""
        if list_objs is None:
            dict_repr = []
        else:
            for i in list_objs:
                dict_repr.append(i.to_dict())
