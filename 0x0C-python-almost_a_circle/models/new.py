#!/usr/bin/python3
"""This class will be the “base” of all other
classes in this project. The goal of it is to manage
id attribute in all your future classes and to
avoid duplicating the same code
(by extension, same bugs)
"""
import json

class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if (id):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """A static method that returns json format"""
        if not (list_dictionaries) or list_dictionaries is None:
            return ("[]")
        return (json.dumps(list_dictionaries))
"""
A module that perfotms magic
"""



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
        print("\n" * self.__y, end='')
        for i in range(self.__height):
            print(" " * self.__x, end='')
            print("#" * self.__width)

    def __str__(self):
        """Returns str repr"""
        return (f"[Rectangle] ({self.id})\
{self.__x}/{self.__y} - {self.__width}/{self.__height}")

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
        return (
                {
                    'id': self.id,
                    'width': self.__width,
                    'height': self.__height,
                    'x': self.__x,
                    'y': self.__y
                    }
                )
"""
A magical module that inherits from Rectangle
"""



class Square(Rectangle):
    """A class that inherits from rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        Rectangle.__init__(self, width=size, height=size, x=x, y=y, id=id)

    def __str__(self):
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}")

    @property
    def size(self):
        return (self.width)

    @size.setter
    def size(self, size):
        if (type(size) is not int):
            raise TypeError("width must be an integer")
        elif (size <= 0):
            raise ValueError("width must be > 0")
        self.width = size
        self.height = size


    def update(self, *args, **kwargs):
        if (args) and len(args) != 0:
            if len(args) == 1:
                self.id = args[0]
            elif len(args) == 2:
                self.id = args[0]
                self.width = args[1]
                self.height = args[1]
            elif len(args) == 3:
                self.id = args[0]
                self.width = args[1]
                self.height = args[1]
                self.x = args[2]
            else:
                self.id = args[0]
                self.width = args[1]
                self.height = args[1]
                self.x = args[2]
                self.y = args[3]

        if not args:
            for key, value in kwargs.items():
                if len(kwargs) == 1:
                    if (key == 'id'):
                        self.id = kwargs[key]
                    elif (key == 'size'):
                        self.width = kwargs[key]
                        self.height = kwargs[key]
                    elif (key == 'x'):
                        self.x = kwargs[key]
                    elif (key == 'y'):
                        self.y = kwargs[key]
                elif len(kwargs) == 2:
                    if (key == 'id'):
                        self.id = kwargs[key]
                    elif (key == 'size'):
                        self.width = kwargs[key]
                        self.height = kwargs[key]
                    elif (key == 'x'):
                        self.x = kwargs[key]
                    elif (key == 'y'):
                        self.y = kwargs[key]
                elif len(kwargs) == 3:
                    if (key == 'id'):
                        self.id = kwargs[key]
                    elif (key == 'size'):
                        self.width = kwargs[key]
                        self.height = kwargs[key]
                    elif (key == 'x'):
                        self.x = kwargs[key]
                    elif (key == 'y'):
                        self.y = kwargs[key]
                elif len(kwargs) == 4:
                    if (key == 'id'):
                        self.id = kwargs[key]
                    elif (key == 'size'):
                        self.width = kwargs[key]
                        self.height = kwargs[key]
                    elif (key == 'x'):
                        self.x = kwargs[key]
                    elif (key == 'y'):
                        self.y = kwargs[key]



if __name__ == "__main__":

    r1 = Rectangle(10, 7, 2, 8)
    dictionary = r1.to_dictionary()
    json_dictionary = Base.to_json_string([dictionary])
    print(dictionary)
    print(type(dictionary))
    print(json_dictionary)
    print(type(json_dictionary))
