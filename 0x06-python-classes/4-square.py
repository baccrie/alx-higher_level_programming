#!/usr/bin/python3
"""
A module that contains a Class
"""


class Square:
    """an class with size attributes"""
    def __init__(self, size=0):
        """A constructor that initializes size"""
        self.__size = size

    def area(self):
        """Returns the area of Square"""
        return (self.__size)

    @property
    def size(self):
        """getter"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """a setter"""
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
