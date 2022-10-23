#!/usr/bin/python3
for i in range(122, 96, -1):
    if (i % 2 == 0):
        c = f"{i:c}"
    else:
        i -= 32
        c = f"{i:c}"
    print('{:}'.format(c), end="")
