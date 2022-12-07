#!/usr/bin/python3

"""
A magical module
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class that inherits from Rectangle class
    """

    def __init__(self, size):
        """
        instantateous
        """
        Rectangle.integer_validator(self, "size", size)
        Rectangle.__init__(self, size, size)
