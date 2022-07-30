#!/usr/bin/python3
"""
A module that perfotms magic
"""
from base import Base


class Rectangle(Base):
    """
    A rectangle class
    """
    # Constructor
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Instantiation of attr
        """
        Base.__init__(self, id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    # Getters and Setters
    @property
    def width(self):
        """width getter"""
        return (self.__width)

    @width.setter
    def width(self, width):
        """
        width setter
        """
        self.__width = width

    @property
    def height(self):
        """height getter"""
        return (self.__height)

    @height.setter
    def height(self, height):
        """height setter"""
        self.__height = height

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, x):
        """x setter"""
        self.__x = x

    @property
    def y(self):
        """y getter"""
        return (self.__y)

    @y.setter
    def y(self, y):
        """y setter"""
        self.__y = y
