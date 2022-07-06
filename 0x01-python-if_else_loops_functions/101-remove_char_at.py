#!/usr/bin/python3

def remove_char_at(str, n):
    arr = []
    i = 0
    while (i < len(str)):
        if not (i == n):
            arr.append(str[i])
            i += 1
        else:
            i += 1

    string = "".join(arr)
    return (string)
