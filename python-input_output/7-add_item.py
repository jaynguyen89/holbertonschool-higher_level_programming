#!/usr/bin/python3
"""docs"""
import os.path
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

"""docs"""

filename = 'add_item.json'
data = []

if os.path.exists(filename):
    data = load_from_json_file(filename)

data += sys.argv[1:]
save_to_json_file(data, filename)
