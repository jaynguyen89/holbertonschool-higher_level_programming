#!/usr/bin/python3


class Rectangle:

    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise TypeError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise TypeError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        return (self.__height + self.__width) * 2

    def __str__(self):
        s = ""
        if self.__width == 0 or self.__height == 0:
            return s

        for i in range(self.__height):
            for j in range(self.__width):
                s += "#"

            if i != self.__height - 1:
                s += "\n"

        return s

    def __del__(self):
        print("Bye rectangle...")
        del self
