#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    ls = []
    for i in range(0, list_length):
        e = False
        r = 0.0
        try:
            l1 = my_list_1[i]
            l2 = my_list_2[i]
            r = l1 / l2
        except IndexError:
            print("out of range")
            e = True
        except TypeError:
            print("wrong type")
            e = True
        except ZeroDivisionError:
            print("division by 0")
            e = True
        finally:
            ls.append(0 if e is True else r)

    return ls
