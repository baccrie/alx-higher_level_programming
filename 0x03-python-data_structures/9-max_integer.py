#!/usr/bin/python3
def max_integer(my_list=[]):
    maxNum = 0
    length = len(my_list)

    if (length == 0):
        return (None)
    for i in range(length):
        if (my_list[i] > maxNum):
            maxNum = my_list[i]

    return (maxNum)
