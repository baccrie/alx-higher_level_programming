#!/usr/bin/python3
def max_integer(my_list=[]):
    length = len(my_list)

    if (length == 0):
        return (None)
    maxNum = my_list[0]
    for i in range(length):
        if (my_list[i] > maxNum):
            maxNum = my_list[i]

    return (maxNum)
