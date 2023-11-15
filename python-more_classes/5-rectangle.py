#!/usr/bin/python3
"""document"""


class Rectangle:
    """document"""

    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width

    """document"""
    @property
    def width(self):
        return self.__width

    """document"""
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    """document"""
    @property
    def height(self):
        return self.__height

    """document"""
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    """document"""
    def area(self):
        return self.__height * self.__width

    """document"""
    def perimeter(self):
        return (self.__height + self.__width) * 2

    """document"""
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

    """document"""
    def __del__(self):
        print("Bye rectangle...")
        del self
