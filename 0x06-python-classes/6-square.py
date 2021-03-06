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
        return (self.__position)

    @position.setter
    def position(self, value):
        """a setter for attr position"""

        if type(value) is not tuple or len(value) != 2 or \
                type(value[0]) is not int or type(value[1]) or \
                value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        if (self.__size == 0):
            print('')
        else:
            for blank in range(self.position[1]):
                print()
            for rows in range(self.__size):
                print(" " * self.position[0], end='')
                print("#" * self.__size)

    def area(self):
        """Returns the area of square"""
        return (self.__size ** 2)


"""


else:
            if (self.__position[0] == 0):
                for i in range(self.__size):
                    print("#" * self.__size)
            else:
                for j in range(self.__size):
                    print(' ' * self.__position[0], end='')
                    print('#' * self.__size)

my_square_1 = Square(3)
my_square_1.my_print()

print("--")

my_square_2 = Square(3, (1, 1))
my_square_2.my_print()

print("--")

my_square_3 = Square(3, (3, 0))
my_square_3.my_print()

print("--")"""
