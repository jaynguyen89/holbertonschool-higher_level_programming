#!/usr/bin/python3
import sys

if __name__ == '__main__':
    numOfArgs = len(sys.argv) - 1
    print(f"{numOfArgs} {'argument' if numOfArgs == 1 else 'arguments'}{'.' if numOfArgs == 0 else ':'}")
    for i in range(1, numOfArgs + 1):
        print("{0}: {1}".format(i, sys.argv[i]))
