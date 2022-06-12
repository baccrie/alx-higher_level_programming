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


my_list = [1, 90, 2, 13, 34, 5, -13, 3]
max_value = max_integer(my_list)
print("Max: {}".format(max_value))
