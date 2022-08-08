#!/usr/bin/python3

class test():
    def __init__(self, width, height):
        self.width = width
        self.height = height
    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if value > 10:
            self.__width = 10
        self.__width = value

    @property
    def height(self):
        return (self.__height)

    @width.setter
    def height(self, value):
        if value > 10:
            self.__height = 10
        self.__height = value

    def area(self):
        return (self.__width * self.__height)

a = test(13, 77)
a.width(66)
b = a.area()
print(b)
