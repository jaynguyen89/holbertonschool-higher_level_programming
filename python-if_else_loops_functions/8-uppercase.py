#!/usr/bin/python3
def uppercase(str):
    for c in str:
        chcode = ord(c)
        if 97 <= chcode <= 122:
            lchcode = chcode - 32
            print(chr(lchcode), end='')
        else:
            print(f"{c}", end='')
