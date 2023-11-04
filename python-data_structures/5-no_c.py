#!/usr/bin/python3
def no_c(my_string):
    ls = list(my_string)
    for char in ls:
        if char == 'c' or char == 'C':
            ls[ls.index(char)] = ''

    return "".join(ls)

if __name__ == '__main__':
    print(no_c("Best School"))
    print(no_c("Chicago"))
    print(no_c("C is fun!"))
