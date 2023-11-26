#!/usr/bin/python3
"""document"""


def inherits_from(obj, a_class):
    """document"""
    return issubclass(obj.__class__, a_class) and obj.__class__ != a_class
