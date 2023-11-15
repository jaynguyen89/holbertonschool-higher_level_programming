#!/usr/bin/python3
"""document"""


class Rectangle:
    """document"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        Rectangle.number_of_instances += 1
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
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        a1 = rect_1.area()
        a2 = rect_2.area()
        return rect_1 if a1 >= a2 else rect_2

    """document"""
    def __str__(self):
        s = ""
        if self.__width == 0 or self.__height == 0:
            return s

        for i in range(self.__height):
            for j in range(self.__width):
                s += f"{Rectangle.print_symbol}"

            if i != self.__height - 1:
                s += "\n"

        return s

    """document"""
    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
        del self
