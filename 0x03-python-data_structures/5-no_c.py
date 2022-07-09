#!/usr/bin/python3
def no_c(my_string):
    newString = my_string[:]
    i = 0

    for mem in my_string:
        if (mem == 'c' or mem == 'C'):
            del newString[i]
        i += 1
    return (newString)
