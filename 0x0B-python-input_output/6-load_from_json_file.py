#!/usr/bin/python3
"""A magical module"""


import json


def load_from_json_file(filename):
    """JSON"""
    with open(filename, 'r', encoding='utf-8') as f:
        data = f.read()
        new = json.loads(data)
        return (new)
