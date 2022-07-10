#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    new_list = [:]
    i = len(my_list)
    if not my_list:
        pass
    while (i != 0):
        i -= 1
        new_list.append(my_list[i])
        print("{:d}".format(my_list[i]))
    my_list = new_list
