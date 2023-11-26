#!/usr/bin/python3
"""document"""


class BaseGeometry:
    """document"""

    """document"""
    def area(self):
        raise Exception("area() is not implemented")

    """document"""
    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
