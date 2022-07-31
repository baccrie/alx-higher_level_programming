#!/usr/bin/python3
"""
A magical module that inherits from Rectangle
"""

from .rectangle import Rectangle


class Square(Rectangle):
    """A class that inherits from rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        Rectangle.__init__(self, width=size, height=size, x=x, y=y, id=id)

    def __str__(self):
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}")

    @property
    def size(self):
        return (self.width)

    @size.setter
    def size(self, size):
        if (type(size) is not int):
            raise TypeError("width must be an integer")
        elif (size <= 0):
            raise ValueError("width must be > 0")
        self.width = size
        self.height = size
