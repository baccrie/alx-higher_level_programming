#!/usr/bin/python3
"""
A module that contains a class Rectangle
"""


class Rectangle:
    """
    A class that defines a rectangle
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        getter method for width attribute
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """
        setter method for attr width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        height atrr getter
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """
        height attr setter
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        returns the area of rect
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """
        returns the perimeter of rect
        """

        if self.__width == 0 or self.__height == 0:
            perimeter = 0
        else:
            perimeter = (2 * self.__width) + (2 * self.__height)
        return (perimeter)
