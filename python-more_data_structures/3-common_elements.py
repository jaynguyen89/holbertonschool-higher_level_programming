#!/usr/bin/python3
def common_elements(set_1, set_2):
    len1 = len(set_1)
    len2 = len(set_2)
    ls = []
    for i in (set_1 if len1 <= len2 else set_2):
        if len1 <= len2 and i in set_2:
            ls.append(i)

        if len2 < len1 and i in set_1:
            ls.append(i)

    return ls
