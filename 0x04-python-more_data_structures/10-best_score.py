#!/usr/bin/python3
def best_score(a_dictionary):
    maxn = 0
    if not a_dictionary:
        return ("None")
    else:
        for a in a_dictionary:
            if a_dictionary[a] > maxn:
                key = a
                maxn = a_dictionary[key]
            else:
                pass

    return (key)
