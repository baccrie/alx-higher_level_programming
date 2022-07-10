#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    i = len(my_list)
    if not my_list:
        return

    while (i != 0):
        i -= 1
        print("{:d}".format(my_list[i]))
