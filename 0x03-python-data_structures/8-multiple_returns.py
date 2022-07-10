#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        first = "None"
    else:
        first = sentence[0]

    length = len(sentence)
    new_tuple = (length, first)
    return (new_tuple)
