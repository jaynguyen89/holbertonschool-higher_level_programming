#!/usr/bin/python3
def search_replace(my_list, search, replace):
    arr = []
    for i in my_list:
        arr.append(i if i != search else replace)

    return arr
