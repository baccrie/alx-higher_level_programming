#!/usr/bin/python3
"""A module that performs magic"""


def is_same_class(obj, a_class):
    """Check if obj is an instance of a_class"""
    if (isinstance(obj, a_class) and type(obj) is a_class):
        return (True)
    else:
        return (False)
