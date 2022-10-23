#!/usr/bin/python3
def remove_char_at(str, n):
    tmp = str
    tmp = list(tmp)
    if (n >= 0) and (n < len(tmp)):
        tmp.pop(n)
    return ("".join(tmp))
