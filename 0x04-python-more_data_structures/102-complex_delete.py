#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    i = 0
    j = 0
    for a in a_dictionary:
        if a_dictionary[a] == value:
            i += 1
        else:
            pass
    while (j < i):
        del a_dictionary[a]
        j++
