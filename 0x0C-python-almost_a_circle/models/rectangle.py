#!/usr/bin/python3
"""A module that inherits from the base"""


from .base import Base


class Rectangle(Base):
    """A class that inherits from base class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor"""
        super().__init__(id)
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
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """height getter"""
        return (self.__height)

    @height.setter
    def height(self, height):
        """height setter"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """x getter"""
        return (self.__x)

    @x.setter
    def x(self, x):
        """x setter"""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """y getter"""
        return (self.__y)

    @y.setter
    def y(self, y):
        """x setter"""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """a method that returns area"""
        return (self.__width * self.__height)

    def display(self):
        """prints to stdout the rect with the character '#'"""
        print("\n" * self.__y, end='')
        for a in range(self.__height):
            print(' ' * self.__x, end='')
            print('#' * self.__width)

    def __str__(self):
        """Returns str repr to stdout"""
        stri = f"[{type(self).__name__}] ({self.id}) {self.__x}/\
{self.__y} - {self.__width}/{self.__height}"

        return (stri)

    def update(self, *args, **kwargs):
        """Magical method"""
        if (args) and len(args) != 0:
            if len(args) == 1:
                self.id = args[0]
            elif len(args) == 2:
                self.id = args[0]
                self.__width = args[1]
            elif len(args) == 3:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
            elif len(args) == 4:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
            else:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
                self.__y = args[4]

        if not args:
            for key, value in kwargs.items():
                if len(kwargs) == 1:
                    if (key == 'id'):
                        self.id = kwargs[key]
                    elif (key == 'width'):
                        self.__width = kwargs[key]
                    elif (key == 'height'):
                        self.__height = kwargs[key]
                    elif (key == 'x'):
                        self.__x = kwargs[key]
                    elif (key == 'y'):
                        self.__y = kwargs[key]
                elif len(kwargs) == 2:
                    if (key == 'id'):
                        self.id = kwargs[key]
                    elif (key == 'width'):
                        self.__width = kwargs[key]
                    elif (key == 'height'):
                        self.__height = kwargs[key]
                    elif (key == 'x'):
                        self.__x = kwargs[key]
                    elif (key == 'y'):
                        self.__y = kwargs[key]
                    elif (key == 'width'):
                        self.__width = kwargs[key]
                elif len(kwargs) == 3:
                    if (key == 'id'):
                        self.id = kwargs[key]
                    elif (key == 'width'):
                        self.__width = kwargs[key]
                    elif (key == 'height'):
                        self.__height = kwargs[key]
                    elif (key == 'x'):
                        self.__x = kwargs[key]
                    elif (key == 'y'):
                        self.__y = kwargs[key]
                elif len(kwargs) == 4:
                    if (key == 'id'):
                        self.id = kwargs[key]
                    elif (key == 'width'):
                        self.__width = kwargs[key]
                    elif (key == 'height'):
                        self.__height = kwargs[key]
                    elif (key == 'x'):
                        self.__x = kwargs[key]
                    elif (key == 'y'):
                        self.__y = kwargs[key]
                else:
                    if (key == 'id'):
                        self.id = kwargs[key]
                    elif (key == 'width'):
                        self.__width = kwargs[key]
                    elif (key == 'height'):
                        self.__height = kwargs[key]
                    elif (key == 'x'):
                        self.__x = kwargs[key]
                    elif (key == 'y'):
                        self.__y = kwargs[key]

    def to_dictionary(self):
        """Converts to dict repr"""
        return (
                {
                    'id': self.id,
                    'width': self.__width,
                    'height': self.__height,
                    'x': self.__x,
                    'y': self.__y
                 }
                )
