#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if not my_list:
        return

    i = len(my_list)
    while (i >= 0):
        print("{}".format(i))
        i -= 1

my_list = [1, 2, 3, 4, 5]
print_reversed_list_integer(my_list)
