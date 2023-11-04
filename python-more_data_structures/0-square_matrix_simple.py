#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    mx = []
    for arr in matrix:
        ls = []
        for i in arr:
            ls.append(i * i)

        mx.append(ls)

    return mx
