#!/usr/bin/python3
"""
A module that contains a Class
"""


class Square:
    """an class with size attributes"""

    def __init__(self, size):
        """initialises size to a private attr"""
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
