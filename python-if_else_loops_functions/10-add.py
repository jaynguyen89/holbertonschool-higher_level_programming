#!/usr/bin/python3
def add(a, b):
    res = a
    neg = b < 0
    for _ in range(b if neg is False else -1 * b):
        res += (1 if neg is False else -1)

    return res
