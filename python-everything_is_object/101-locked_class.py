#!/usr/bin/python3
class LockedClass:
    def __setattr__(self, key, value):
        if key != "first_name":
            raise AttributeError(f"'LockedClass' object has no attribute '{key}'")
        else:
            super().__setattr__(key, value)
