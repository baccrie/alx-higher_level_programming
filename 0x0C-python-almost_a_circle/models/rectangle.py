#!/usr/bin/python3
"""
Why private attributes with getter/setter? Why not directly public attribute?
Because we want to protect attributes of our class.
With a setter, you are able to validate what
developer is trying to assign to a variable.
So after, in your class you can “trust” these attributes.
"""


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        Base.__init__(self, id=None)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, width):
        self.__width = width

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, height):
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return (self.__y)

    @y.setter
    def y(self, y):
        self.__y = y
