#!/usr/bin/python3
line = ''
for num in range(1, 100):
    if num < 10:
        line += "{:02d}, ".format(num)
    else:
        reverse = int(str(num)[::-1])

        redundant = False
        for i in range(1, num + 1):
            if reverse == i:
                redundant = True
                break

        if redundant:
            continue

        line += f"{num}, "

print("{0}".format(line[0:-2]))
