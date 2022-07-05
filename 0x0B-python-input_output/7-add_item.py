#!/usr/bin/python3
"""
"A JSON script coupled with command line arguement"""


import json
import sys


i = len(sys.argv)
jsonList = []
for a in range(1, i):
    jsonList.append(sys.argv[a])


def save_to_json_file(my_obj, filename):
    """
    The function dumps the obj to the filename
    """
    with open(filename, 'w', encoding="UTF-8") as f:
        json.dump(my_obj, f)a


def load_from_json_file(filename):
    """
    A function that dumps from JSON to script
    """
    with open(filename, 'r', encoding="UTF-8") as f:
        new = json.load(f)
        return (new)


save_to_json_file(jsonList, 'add_item.json')
load_from_json_file('add_item.json')
