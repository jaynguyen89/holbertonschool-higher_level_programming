#!/usr/bin/python3
"""document"""


class MyList(list):
    """document"""

    def print_sorted(self):
        items = self.copy()
        items.sort()
        print(items)
