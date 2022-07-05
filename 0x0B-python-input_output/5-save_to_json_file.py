#!/usr/bin/python3
"""
A JSON script written by baccrie
"""


import json


def save_to_json_file(my_obj, filename):
    """
    The function dumps the obj to the filename
    """
    with open(filename, 'w', encoding="UTF-8") as f:
        json.dump(my_obj, f)
