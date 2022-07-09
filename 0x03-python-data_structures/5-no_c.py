#!/usr/bin/python3
def no_c(my_string):
    i = 0
    new = []
    for i in my_string:
        if (i == 'c' or i == 'C'):
            pass
        else:
            new.append(i)
    new = "".join(new)
    return new
