#!/usr/bin/python3
from sys import argv
if __name__ == '__main__':
    len_arg = len(argv)
    if (len_arg == 1):
        print("0 arguements.")

    elif (len_arg == 2):
        print("1 arguements:")
        for i in range(1, len(argv)):
            print("{:d}: {}".format(i, argv[i]))
    else:
        print("{:d} arguements:".format(len_arg - 1))
        for i in range(1, len(argv)):
            print("{:d}: {}".format(i, argv[i]))
