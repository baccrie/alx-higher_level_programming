#!/usr/bin/python3

i = 0
asciiAl = 122
while (i < 26):
    if (i % 2) == 0:
        c = asciiAl
    else:
        c = asciiAl - 32
    print("{:c}".format(c), end='')
    asciiAl -= 1
    i += 1
