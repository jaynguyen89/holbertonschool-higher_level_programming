#!/usr/bin/python3
"""docs"""


def append_write(filename="", text=""):
    with open(filename, "a+") as file:
        file.write(text)

    return len(text)
