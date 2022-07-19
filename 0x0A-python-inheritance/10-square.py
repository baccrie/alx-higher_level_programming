#!/usr/bin/python3
"""Later things"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    def __init__(self, size):
        Rectangle.__init__(self, size, size)
        self.__size = size
        Rectangle.integer_validator(self, 'size', size)
        Rectangle.area(self)
