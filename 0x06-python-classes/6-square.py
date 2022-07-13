#!/usr/bin/python3
"""
A module that contains a Class
"""


class Square:
    """an class with size attributes"""
    def __init__(self, size=0, position=(0, 0)):
        """A constructor that initializes size"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """getter"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """a setter"""
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """a getter for attr position"""
        return (size.__position)

    @position.setter
    def position(self, value):
        """a setter for attr position"""
        if (type(value) is not tuple or (value[0] < 0 or value[1] < 0)):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (type(value[0] is not int or value[1] is not int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        if (self.__size == 0):
            print('')
        elif (self.__position[0] == 0):
            for i in range(self.__size):
                print(self.__size * "#", end='')
                print()
        elif (self.__position[0] > 0):
            for i in range(self.__size):
                print(" " * self.__position[0], end='')
                print(self.__size * "#", end='')
                print()

    def area(self):
        """Returns the area of square"""
        return (self.__size ** 2)
