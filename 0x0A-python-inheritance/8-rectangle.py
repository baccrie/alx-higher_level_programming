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
