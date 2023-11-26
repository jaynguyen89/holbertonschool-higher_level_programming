#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

"""document"""


class Square(Rectangle):
    """document"""
    def __init__(self, size):
        super().integer_validator("size", size)
        self._size = size

    """document"""
    def area(self):
        return self._size * self._size

    """document"""
    def __str__(self):
        return f"[Rectangle] {self._size}/{self._size}"
