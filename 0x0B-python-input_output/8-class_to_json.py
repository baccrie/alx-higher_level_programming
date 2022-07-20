#!/usr/bin/python3
"""A magical module"""


import json


def class_to_json(obj):
    """JSON serialization of class instance"""
    new = obj.__dict__
    jsonData = json.dumps(new)
    return (jsonData)
