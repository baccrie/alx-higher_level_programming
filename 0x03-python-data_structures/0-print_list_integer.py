#!/usr/bin/python3

def print_list_integer(my_list=[]):
    length = len(my_list)
    i = 0

    while (i < length):
        print("{:d}".format(my_list[i]))
        i += 1
