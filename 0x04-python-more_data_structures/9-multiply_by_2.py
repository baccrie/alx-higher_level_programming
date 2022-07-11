#!/usr/bin/python3
def best_score(a_dictionary):
    max = 0
    if not a_dictionary:
        return None
    else:
        for a in a_dictionary:
            if a_dictionary[a] > max:
                max = a_dictionary[a]
            else:
                pass

    return (max)
