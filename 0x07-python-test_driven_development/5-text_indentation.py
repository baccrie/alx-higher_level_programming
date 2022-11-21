#!/usr/bin/python3
"""
A module that performs magic
"""


def text_indentation(text):
    """
    baccrie 2022 copyright
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    for i in text:
        if i not in [':', '?', '.']:
            print(i, end='')
        else:
            print(i, end='')
            print('')
            print('')
