#!/usr/bin/python3
from sys import argv
if __name__ == '__main__':
    len_arg = len(argv)
    result = 0
    for i in range(1, len(argv)):
        result += int(argv[i])
    print("{:d}".format(result))
