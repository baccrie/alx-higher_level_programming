#!/usr/bin/python3
"""
wahala
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle ingerits from BaseGeo
    """
    def __init__(self, width, height):
        """
        instantaneous
        """
        self.__width = width
        self.__height = height
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)
