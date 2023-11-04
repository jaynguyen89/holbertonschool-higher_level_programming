#!/usr/bin/python3
import sys

if __name__ == '__main__':
    numOfArgs = len(sys.argv) - 1
    argText = 'argument' if numOfArgs == 1 else 'arguments'
    ending = '.' if numOfArgs == 0 else ':'
    print(f"{numOfArgs} {argText}{ending}")
    for i in range(1, numOfArgs + 1):
        print("{0}: {1}".format(i, sys.argv[i]))
