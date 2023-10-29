#!/usr/bin/python3
def pow(a, b):
    if b == 0:
        return 1

    neg = b < 0
    res = a if neg is False else 1/a
    for _ in range((b if neg is False else -1 * b) - 1):
        res = res * a if neg is False else res/a

    return res
