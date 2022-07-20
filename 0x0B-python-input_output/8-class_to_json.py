#!/usr/bin/python3
"""A magical module"""


def class_to_json(obj):
    """JSON serialization of class instance"""
    new = obj.__dict__
    return (new)
