#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        mx = my_list[0]
        for i in my_list:
            mx = mx if mx > i else i
        return mx
