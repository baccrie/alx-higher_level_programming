#!/usr/bin/python3


"""
A module that perfoms magic
"""


def say_my_name(first_name, last_name=""):
    """
    A func that prints first name and last name
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    elif type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
