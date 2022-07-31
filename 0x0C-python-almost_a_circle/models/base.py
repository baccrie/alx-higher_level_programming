#!/usr/bin/python3
"""This class will be the “base” of all other
classes in this project. The goal of it is to manage
id attribute in all your future classes and to
avoid duplicating the same code
(by extension, same bugs)
"""


import json


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if (id):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """A static method that returns json format"""
        if not (list_dictionary) or list_dictionary is None:
            return ("[]")
        return (json.dumps(list_dictionaties))
