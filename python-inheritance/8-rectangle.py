#!/usr/bin/python3
"""document"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """document"""

    def __init__(self, width, height):
        """document"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self._width = width
        self._height = height
