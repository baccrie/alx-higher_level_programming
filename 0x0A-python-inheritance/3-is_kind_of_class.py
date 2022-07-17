#!/usr/bin/python3
"""Trabaye Module"""


def is_kind_of_class(obj, a_class):

    if (isinstance(obj, a_class) or isinstance(obj, super(a_class, obj))):
        return (True)
    else:
        return (False)

a = 1
if is_kind_of_class(a, int):
    print("{} comes from {}".format(a, int.__name__))
if is_kind_of_class(a, float):
    print("{} comes from {}".format(a, float.__name__))
if is_kind_of_class(a, object):
    print("{} comes from {}".format(a, object.__name__))
