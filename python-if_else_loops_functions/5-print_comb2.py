#!/usr/bin/python3
for num in range(0, 100):
    fnum = "{:02d}".format(num)
    print(f"{fnum}{'' if num == 99 else ', '}", end='')
