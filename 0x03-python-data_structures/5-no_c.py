#!/usr/bin/python3
def no_c(my_string):
    new = list(my_string)
    new1 = []
    for i in new:
        if i == 'C' or i == 'c':
            pass
        else:
            new1.append(i)

    return ("".join(new1))
