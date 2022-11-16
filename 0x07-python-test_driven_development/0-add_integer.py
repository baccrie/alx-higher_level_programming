#!/usr/bin/python3


"""
A module that performs magic , baccrie 2022 ©
"""


def add_integer(a, b=98):
    """ The function returns the addition of a and b
    :a - a parameter either of type int or float
    :b - a parameter eitger of type int or float
    """

    if (type(a) is not int) and (type(a) is not float):
        raise TypeError("a must be an integer")
    if (type(b) is not int) and (type(b) is not float):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)
