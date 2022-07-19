#!/usr/bin/python3
"""A magical module"""


import json


def load_from_json_file(filename):
    """JSON"""
    with open(filename, 'w', encoding='utf-8') as f:
        data = json.load(f)
        return (data)
