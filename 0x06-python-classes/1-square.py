#!/usr/bin/python3
"""
A module that contains a Class
"""


class Square:
    """an class with size attributes"""

    def __init__(self, size):
        """initialises size to a private attr
        Args:
            size: size of Square
        Return:
            Nothing
        """
        self.__size = size
