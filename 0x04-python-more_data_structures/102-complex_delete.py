#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if value not in list(a_dictionary.values()):
        return (a_dictionary)

    keys = list(key for key in a_dictionary if value == a_dictionary[key])
    for i in keys:
        del a_dictionary[i]
    return (a_dictionary)
