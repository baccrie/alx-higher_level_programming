#!/usr/bin/python3
"""
A script that defines a Class Rectangle
"""
class Rectangle:
    """
    A rectangle that does nothing with no class attributes
    """
    def __init__(self, width=0, height=0):
        """
        Instantiation method
        paramters:
            @width : defines the width of the rectangle
            @height : defines the height of the rectangle
        """
        self.height = height
        self.width = width

    @properties
    def width(self):
        """A method used to get the width value"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """A method for setting the width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @properties
    def height(self):
        """A method used to get the width value"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """A method for setting the height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
