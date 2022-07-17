#!/usr/bin/python3
"""Later things"""


class BaseGeometry:
    """Trabaye"""

    def area(self):
        """Raising exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Temp"""
        self.__name = name
        if (type(value) is not int):
            raise TypeError(f"{self.__name} must be an integer")
        if (value <= 0):
            raise ValueError(f"{self.__name} must be greater than 0")
        self.__value = value
