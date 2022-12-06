#!/usr/bin/python3
"""Later things"""


class BaseGeometry:
    """
    A base class
    """
    def area(self):
        """
        Raises an exception with error
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        An integer validator method
        """
        self.__name = name
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        self.__value = value
