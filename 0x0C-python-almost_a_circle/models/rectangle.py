#!/usr/bin/python3
"""
A module that perfotms magic
"""
from base import Base


class Rectangle(Base):
    """
    Class Rectangle this class inheritance from Base class.
    """
    # Constructor
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor of a Rectangle
        Args:
          - width: int
          - height: int
          - x: int
          - y: int
          - id: int
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    # Getters and Setters
    @property
    def width(self):
        """Getter of the private attribute width"""
        return (self.__width)

    @width.setter
    def width(self, width):
        """
        Setter of the private attribute width
        Args:
          - value: int
        """
        self.__width = width

    @property
    def height(self):
        """Getter of the private attribute height"""
        return (self.__height)

    @height.setter
    def height(self, height):
        """
        Setter of the private attribute height
        Args:
          - value: int
        """
        self.__height = height

    @property
    def x(self):
        """Getter of the private attribute x"""
        return self.__x

    @x.setter
    def x(self, x):
        """
        Setter of the private attribute x
        Args:
          - value: int
        """
        self.__x = x

    @property
    def y(self):
        """Getter of the private attribute y"""
        return (self.__y)

    @y.setter
    def y(self, y):
        """
        Setter of the private attribute y
        Args:
          - value: int
        """
        self.__y = y
