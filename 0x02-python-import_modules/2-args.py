#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    length = len(argv)

    print("{} arguments:".format(length - 1))
    for i in range(1, length):
        print("{}: {}".format(i, argv[i]))
