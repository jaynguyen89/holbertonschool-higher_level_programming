#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""document"""


class Rectangle(BaseGeometry):
    """document"""

    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self._width = width
        self._height = height

    """document"""
    def area(self):
        return self._width * self._height

    """document"""
    def __str__(self):
        return f"[Rectangle] {self._width}/{self._height}"
