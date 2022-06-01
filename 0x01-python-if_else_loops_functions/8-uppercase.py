#!/usr/bin/python3
def uppercase(str):
    i = 0
    diff = ord('a') - ord('A')

    while (i < len(str)):
        con = ord(str[i])
        if (con <= 122) and (con >= 97):
            con -= diff
            char = chr(con)
        else:
            char = str[i]
        print("{}".format(char), end='')
        i += 1
    print("")
