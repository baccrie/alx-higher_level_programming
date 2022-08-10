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
        if not (list_dictionaries) or list_dictionaries is None:
            return ("[]")
        return (json.dumps(list_dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """A dict"""
        if not (json_string) or json_string is None:
            return []
        return (json.loads(json_string))

    @classmethod
    def save_to_file(cls, list_objs)
    """save to.json"""
    if list_objs is None:
        a = "[]"
    else:
        a = from_json_string(list_objs)
    with open('json', 'w') as f:
        json.dump(a, f)
