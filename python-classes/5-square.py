#!/usr/bin/python3
"""file document"""


class Square:
    """class document"""

    """init"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    """attr"""
    @property
    def size(self):
        return self.__size

    """attr"""
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    """area"""
    def area(self):
        return self.__size * self.__size

    """my_print"""
    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end='')
                print("")
