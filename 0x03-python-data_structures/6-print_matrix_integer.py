#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for a in matrix:
        leng = len(a) - 1
        i = 0
        for b in a:
            if i == leng:
                print("{:d}".format(b), end='')
            else:
                print("{:d} ".format(b), end='')
            i += 1
        print('')
