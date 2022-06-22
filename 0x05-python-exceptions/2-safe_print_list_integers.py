#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    a = 0
    while (i < x):
        try:
            print("{:d}".format(my_list[i]), end='')
            a += 1
        except (ValueError, TypeError):
            print(end='')

        i += 1
    print('')
    return (a)
