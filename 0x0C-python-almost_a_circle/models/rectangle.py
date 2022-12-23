#!/usr/bin/python3
"""A module that inherits from the base"""


from .base import Base


class Rectangle(Base):
    """A class that inherits from base class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor"""
        Base.__init__(self, id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """width getter"""
        return (self.__width)

    @width.setter
    def width(self, size):
        """width setter"""
        self.__width = size

    @property
    def height(self):
        """height getter"""
        return (self.__height)

    @height.setter
    def height(self, size):
        """height setter"""
        self.__height = size

    @property
    def x(self):
        """x getter"""
        return (self.__x)

    @x.setter
    def x(self, size):
        """x setter"""
        self.__x = size

    @property
    def y(self):
        """y getter"""
        return (self.__y)

    @y.setter
    def y(self, size):
        """y setter"""
        self.__y = size
