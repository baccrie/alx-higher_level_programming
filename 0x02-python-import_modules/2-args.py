#!/usr/bin/python3
from sys import argv
if __name__ == '__main__':
    len_arg = len(argv)
    if (len_arg == 1):
        print("0 arguments.")

    elif (len_arg == 2):
        print("1 arguments:")
        for i in range(1, len(argv)):
            print("{:d}: {}".format(i, argv[i]))
    else:
        print("{:d} arguments:".format(len_arg - 1))
        for i in range(1, len(argv)):
            print("{:d}: {}".format(i, argv[i]))
