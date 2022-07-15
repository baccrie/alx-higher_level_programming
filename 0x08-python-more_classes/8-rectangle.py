#!/usr/bin/python3
"""
A module that contains a class Rectangle
"""


class Rectangle:
    """An empty class"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Constructor"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if(type(value) is not int):
            raise TypeError("width must be an integer")
        elif (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if(type(value) is not int):
            raise TypeError("height must be an integer")
        elif (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if (self.__width == 0 or self.__height == 0):
            return (0)
        else:
            return ((2 * self.__width) + (2 * self.__height))

    def __str__(self):
        if (self.__width == 0 or self.__height == 0):
            return ("")
        ch = str(self.print_symbol)
        val = [ch * self.__width for i in range(self.__height)]
        return '\n'.join(val)

    def __repr__(self):
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if (type(rect_1) is not Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif (type(rect_2) is not Rectangle):
            raise TypeError("rect_2 must be an instance     of Rectangle")

        if (rect_1.area() > rect_2.area()):
            return (rect_1)
        elif (rect_2.area() > rect_1.area()):
            return (rect_2)
        elif (rect_1.area() == rect_2.area()):
            return (rect_1)
