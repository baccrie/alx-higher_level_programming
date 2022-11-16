#!/usr/bin/env python3
"""
A module that performs magic , baccrie 2022 ©
"""

def add_integer(a, b=98):

    if type(a) is not int or type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int or type(b) is not float:
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)
