#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        first = None
    else:
        length = len(sentence)
        first = sentence[0]

    new_tuple = (length, first)
    return (new_tuple)
