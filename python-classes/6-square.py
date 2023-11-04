#!/usr/bin/python3
"""file document"""


class Square:
    """class document"""

    """init"""
    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

        if len(position) != 2 or \
                not isinstance(position[0], int) or \
                not isinstance(position[1], int) or \
                (isinstance(position[0], int) and position[0] < 0) or \
                (isinstance(position[1], int) and position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    """attr"""
    @property
    def size(self):
        return self.__size

    """attr"""
    @property
    def position(self):
        return self.__position

    """attr"""
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    """attr"""
    @position.setter
    def position(self, value):
        if len(value) != 2 or \
                not isinstance(value[0], int) or \
                not isinstance(value[1], int) or \
                (isinstance(value[0], int) and value[0] < 0) or \
                (isinstance(value[1], int) and value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    """area"""
    def area(self):
        return self.__size * self.__size

    """my_print"""
    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            print("\n"*self.__position[1], end='')
            for i in range(self.__size):
                print(" "*self.__position[0], end='')
                for j in range(self.__size):
                    print("#", end='')
                print("")
