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
            raise TypeError("width must be >= 0")
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
            raise TypeError("height must be >= 0")
        else:
            self.__height = value
