#!/usr/bin/python3
def no_c(my_string):
    new = list(my_string)
    new1 = []
    for i in new:
        if i == 'C' or i == 'c':
            new.remove(i)
        else:
            pass

    return ("".join(new))
