#!/usr/bin/python3
"""
This program performs magic
"""


def print_square(size):
    """
    Function to print a Square with # as delimeter
    """

    if type(size) is not int:
        raise TypeError('size must be an integer')

    if size < 0:
        raise ValueError('size must be >= 0')

    if size != 0:
        i = 0
        while i < size:
            print("#" * size)
            i += 1
