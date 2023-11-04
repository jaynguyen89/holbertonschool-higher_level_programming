#!/usr/bin/python3
def uniq_add(my_list=[]):
    ls = []
    for i in my_list:
        try:
            if ls.index(i) >= 0:
                continue
        except ValueError:
            ls.append(i)

    total = 0
    for i in ls:
        total += i

    return total
