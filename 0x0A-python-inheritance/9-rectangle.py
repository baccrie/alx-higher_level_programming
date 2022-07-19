#!/usr/bin/python3
"""Later things"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Tmp"""

    def __init__(self, width, height):
        """Tmp"""
        self.__width = width
        self.__height = height
        BaseGeometry.integer_validator(self, 'width', width)
        BaseGeometry.integer_validator(self, 'height', height)

    def area(self):
        """Area of.rect"""
        return (self.__width * self.__height)

    def __str__(self):
        return '[Rectangle] {:d}/{:d}'.format(self.__width, self.__height)
