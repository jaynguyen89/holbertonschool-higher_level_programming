#!/usr/bin/python3
class MyList(list):
    def print_sorted(self):
        items = self.copy()
        items.sort()
        print(items)
