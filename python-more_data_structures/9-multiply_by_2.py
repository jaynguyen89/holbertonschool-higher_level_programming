#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dt = {}
    for k in a_dictionary:
        dt[k] = a_dictionary[k] * 2

    return dt
