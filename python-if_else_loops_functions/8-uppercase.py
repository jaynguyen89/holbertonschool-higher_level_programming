#!/usr/bin/python3
def uppercase(str):
    res = []
    for c in str:
        chcode = ord(c)
        if 97 <= chcode <= 122:
            res.append(chr(chcode - 32))
        else:
            res.append(c)

    print("{0}".format("".join(res)))
