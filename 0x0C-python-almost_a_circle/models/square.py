#!/usr/bin/python3
"""
A magical module that inherits from Rectangle
"""

from .rectangle import Rectangle


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


"""
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
                else:
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

    s1 = Square(5)
    print(s1)

    s1.update(10)
    print(s1)

    s1.update(1, 2)
    print(s1)

    s1.update(1, 2, 3)
    print(s1)

    s1.update(1, 2, 3, 4)
    print(s1)

    s1.update(x=12)
    print(s1)

    s1.update(size=7, y=1)
    print(s1)

    s1.update(size=7, id=89, y=1)
    print(s1)
    """
