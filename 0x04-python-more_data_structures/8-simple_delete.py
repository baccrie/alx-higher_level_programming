#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if key not in a_dictionary:
        pass
    else:
        a_dictionary.pop(key)
