#!/usr/bin/python3
"""document"""


class LockedClass:
    """document"""

    def __setattr__(self, key, value):
        """document"""
        m = f"'LockedClass' object has no attribute '{key}'"
        if key != "first_name":
            raise AttributeError(m)
        else:
            super().__setattr__(key, value)
