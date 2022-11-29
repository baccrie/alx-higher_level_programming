#!/usr/bin/python3
"""
A module that contains a class Rectangle
"""


class Rectangle:
    """
    A class that defines a rectangle
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        getter method for width attribute
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """
        setter method for attr width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        height atrr getter
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """
        height attr setter
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        returns the area of rect
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """
        returns the perimeter of rect
        """

        if self.__width == 0 or self.__height == 0:
            perimeter = 0
        else:
            perimeter = (2 * self.__width) + (2 * self.__height)
        return (perimeter)

    def __str__(self):
        """
        Returns string representation
        """

        if self.__width == 0 or self.__height == 0:
            return ("")
        stri = [self.__width * str(self.print_symbol)
                for i in range(self.__height)]
        return ("\n".join(stri))

    def __repr__(self):
        return f'Rectangle({self.__width}, {self.__height})'

    def __del__(self):
        """
        Deletes an instance of rect
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        """
        static method that returns wahala based
        on the bigger rectangle instance
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if Rectangle.area(rect_1) >= Rectangle.area(rect_2):
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """
        returns a rect instance
        """
        return (cls(size, size))
