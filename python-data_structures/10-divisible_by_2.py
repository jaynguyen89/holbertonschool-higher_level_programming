#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    ls = []
    for i in my_list:
        ls.append(True if i % 2 == 0 else False)
    return ls
