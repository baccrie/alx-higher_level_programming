#!/usr/bin/python3
"""
A module that defines a class
"""


class Square:
    """
    A Class that defines a square
    """

    def __init__(self, size=0):
        """
        args:
            size = defines the size of the square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """
        Returns the area of Square
        """
        return (self.__size ** 2)

    @size.getter
    def size(self):
        """
        A getter for instance attribute size
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        A setter for
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value
