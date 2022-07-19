#!/usr/bin/python3
"""Later things"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Tmp"""

    def __init__(self, width, height):
        """Tmp"""
        super().integer_validator(self, 'width', width)
        self.__width = width
        super().integer_validator(self, 'height', height)
        self.__height = height
