#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for ls in matrix:
        for i in range(0, len(ls)):
            ending = " " if i < len(ls) - 1 else ""
            print("{:d}{}".format(ls[i], ending), end='')
        print("")
