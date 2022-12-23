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
        """Getter of the private attribute width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """
        Setter of the private attribute width
        Args:
          - value: int
        """
        if (type(value) is not int):
            raise TypeError("width must be an integer")
        elif (value <= 0):
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter of the private attribute height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """
        Setter of the private attribute height
        Args:
          - value: int
        """
        if (type(value) is not int):
            raise TypeError("height must be an integer")
        elif (value <= 0):
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter of the private attribute x"""
        return (self.__x)

    @x.setter
    def x(self, value):
        """
        Setter of the private attribute x
        Args:
          - value: int
        """
        if (type(value) is not int):
            raise TypeError("x must be an integer")
        elif (value < 0):
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter of the private attribute y"""
        return (self.__y)

    @y.setter
    def y(self, value):
        """
        Setter of the private attribute y
        Args:
          - value: int
        """
        if (type(value) is not int):
            raise TypeError("y must be an integer")
        elif (value < 0):
            raise ValueError("y must be >= 0")
        self.__y = value
