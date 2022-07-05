#!/usr/bin/python3
"""
A JSON script
"""


import json


def to_json_string(my_obj):
    """
    The function returns the json format of an object
    """
    new = json.dumps(my_obj)
    return (new)
