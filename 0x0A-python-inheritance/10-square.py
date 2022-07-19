#!/usr/bin/python3
"""Later things"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Trabaye"""

    def __init__(self, size):
        Rectangle.__init__(self, size, size)
        self.__size = size
        Rectangle.integer_validator(self, 'size', size)

    def area(self):
        return (self.__size ** 2)
