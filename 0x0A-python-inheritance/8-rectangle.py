#!/usr/bin/python3
"""Later things"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry



class Rectangle(BaseGeometry):
    """Tmp"""

    def __init__(self, width, height):
        """Tmp"""
        self.__width = width
        self.__height = height
        super().integer_validator(self, width)
        super().integer_validator(self, height)
