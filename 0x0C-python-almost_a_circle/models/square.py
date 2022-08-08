#!/usr/bin/python3
"""
A magical module that inherits from Rectangle
"""


from .rectangle import Rectangle


class Square(Rectangle):
    """A class that inherits from rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        Rectangle.__init__(self, size, size, x, y, id)

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

    #  public methods
    def update(self, *args, **kwargs):
        """A temp"""
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
        if not (args):
            for key, value in kwargs.items():
                if len(kwargs) == 1:
                    if (key == 'id'):
                        self.id = kwargs[key]
                    elif (key == 'size'):
                        self.width = kwargs[key]
                        self.height = kwargs[key]
                    elif (key == 'x'):
                        self.x = kwargs[key]
                    else:
                        self.y = kwargs[key]
                elif len(kwargs) == 2:
                    if (key == 'id'):
                        self.id = kwargs[key]
                    elif (key == 'size'):
                        self.width = kwargs[key]
                        self.height = kwargs[key]
                    elif (key == 'x'):
                        self.x = kwargs[key]
                    else:
                        self.y = kwargs[key]
                elif len(kwargs) == 3:
                    if (key == 'id'):
                        self.id = kwargs[key]
                    elif (key == 'size'):
                        self.width = kwargs[key]
                        self.height = kwargs[key]
                    elif (key == 'x'):
                        self.x = kwargs[key]
                    else:
                        self.y = kwargs[key]
                else:
                    if (key == 'id'):
                        self.id = kwargs[key]
                    elif (key == 'size'):
                        self.width = kwargs[key]
                        self.height = kwargs[key]
                    elif (key == 'x'):
                        self.x = kwargs[key]
                    else:
                        self.y = kwargs[key]

    def to_dictionary(self):
        """A dictionary repr of a square instance"""
        return (
                {
                    'id': self.id,
                    'size': self.width,
                    'x': self.x,
                    'y': self.y
                    }
                )
