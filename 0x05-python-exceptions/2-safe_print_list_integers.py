#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        i = 0
        while i < x:
            try:
                print("{:d}".format(my_list[i]), end='')
            except:
                print('', end='')
            i += 1
    except:
        return (None)
    print('')

    return (x)
