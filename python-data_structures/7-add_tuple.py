#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    ls = []
    mx = len(tuple_a) if len(tuple_a) >= len(tuple_b) else len(tuple_b)
    for i in range(0, mx):
        if i > len(tuple_a) - 1:
            ls.append(tuple_b[i])
        elif i > len(tuple_b) - 1:
            ls.append(tuple_a[i])
        else:
            ls.append(tuple_a[i] + tuple_b[i])

    return tuple(ls)
