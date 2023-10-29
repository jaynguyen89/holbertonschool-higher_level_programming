#!/usr/bin/python3
def islower(c):
    try:
        s = str(c)
        if s.isdigit():
            print(f"{s} is upper")
        else:
            chcode = ord(c)
            if 65 <= chcode <= 90:
                return False
            elif 97 <= chcode <= 122:
                return True
            else:
                print(f"{s} is special")
                return None
    except TypeError:
        print("not a character")
        return None
