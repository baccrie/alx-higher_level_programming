#!/usr/bin/python3
"""
A module that defines a class
"""


class Square:
    """
    A Class that defines a square
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        args:
            size = defines the size of the square
            position = fill up space wahala
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.size = size
        self.position = position

    def area(self):
        """
        Returns the area of Square
        """
        return (self.__size ** 2)

    @property
    def size(self):
        """
        A getter for instance attribute size
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        A setter for
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def my_print(self):
        """
        a method that prints to stdout with the character #
        """
        character = '#'

        if self.__size == 0:
            print()
        else:
            for k in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(self.__position[0] * ' ', end='')
                print(self.__size * character)

    @property
    def position(self):
        """
        getter
        """

        return (self.__position)

    @position.setter
    def position(self, value):
        """
        a setter method for the attr position
        """

        if (len(value) != 2) or (type(value) is not tuple) \
                or (type(value[0]) is not int) \
                or (type(value[1]) is not int) \
                or (value[0] < 0) or (value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
