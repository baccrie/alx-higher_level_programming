#!/usr/bin/python3
"""
A magical module that inherits from Rectangle
"""

from .rectangle import Rectangle


class Square(Rectangle):
    """A class that inherits from rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        width = size
        height = size
        Rectangle.__init__(self, width, height, x=x, y=y, id=None)

    def __str__(self):
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}")
