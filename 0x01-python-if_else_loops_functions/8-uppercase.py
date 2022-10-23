#!/usr/bin/python3
def uppercase(str):
    diff = 32
    for i in str:
        asc = ord(i)
        if (97 <= asc <= 122):
            asc -= diff
            i = f"{asc:c}"
        print("{}".format(i), end="")
    print("")
