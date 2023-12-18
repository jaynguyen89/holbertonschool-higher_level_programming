#!/usr/bin/python3
import json

"""docs"""


def load_from_json_file(filename):
    with open(filename) as file:
        data = json.load(file)
        return data
