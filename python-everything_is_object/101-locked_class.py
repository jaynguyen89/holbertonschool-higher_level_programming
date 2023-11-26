#!/usr/bin/python3
"""document"""


class LockedClass:
    """document"""

    def __setattr__(self, key, value):
        """document"""
        if key != "first_name":
            raise AttributeError(f"'LockedClass' object has no attribute '{key}'")
        else:
            super().__setattr__(key, value)
