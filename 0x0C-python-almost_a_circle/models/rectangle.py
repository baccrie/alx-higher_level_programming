#!/usr/bin/python3
"""
A module that perfotms magic
"""
from .base import Base


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

    @property
    def width(self):
        """width getter"""
        return (self.__width)

    @width.setter
    def width(self, width):
        """
        width setter
        """
        if (type(width) is not int):
            raise TypeError("width must be an integer")
        elif (width <= 0):
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """height getter"""
        return (self.__height)

    @height.setter
    def height(self, height):
        """height setter"""
        if (type(height) is not int):
            raise TypeError("height must be an integer")
        elif (height <= 0):
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, x):
        """x setter"""
        if (type(x) is not int):
            raise TypeError("x must be an integer")
        elif (x < 0):
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """y getter"""
        return (self.__y)

    @y.setter
    def y(self, y):
        """y setter"""
        if (type(y) is not int):
            raise TypeError("y must be an integer")
        elif (y < 0):
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Returns rectnagle instance area"""
        return (self.__width * self.__height)

    def display(self):
        """Draw rectangle instance with #"""
        for i in range(self.__height):
            print("\n" * self.__y, end='')
            print(" " * self.__x, end='')
            print("#" * self.__width)

    def __str__(self):
        """Returns str repr"""
        return (f"[Rectangle] ({self.id})\
{self.__x}/{self.__y} - {self.__width}/{self.__height}")
