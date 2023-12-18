#!/usr/bin/python3
"""docs"""


def read_file(filename=""):
    with open(filename) as file:
        lines = file.readlines()

    for line in lines:
        print(line, end='')
