#!/usr/bin/python3
def uppercase(str):
    diff = ord('a') - ord('A')
    for i in range(len(str)):
        if (97 <= ord(str[i]) <= 122):
            a = ord(str[i]) - diff
            b = chr(a)
        else:
            b = str[i]
        print("{}".format(b), end='')
    print('')
