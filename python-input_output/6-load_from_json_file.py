#!/usr/bin/python3
"""docs"""
import json

"""docs"""


def load_from_json_file(filename):
    """docs"""
    with open(filename) as file:
        data = json.load(file)
        return data
