#!/usr/bin/python3
for num in range(0, 100):
    fnum = "{:02d}".format(num)
    print("{0}{1}".format(fnum, '' if num == 99 else ', '), end='')

print("")
