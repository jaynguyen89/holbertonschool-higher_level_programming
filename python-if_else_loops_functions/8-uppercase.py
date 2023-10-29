#!/usr/bin/python3
def uppercase(str):
    for c in str:
        chcode = ord(c)
        if 97 <= chcode <= 122:
            lchcode = chcode - 32
            print("{0}".format(chr(lchcode)))
        else:
            print("{0}".format(c))
