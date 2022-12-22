#!/usr/bin/python3


"""A module that does wonder"""


def write_file(filename="", text=""):
    """Function that writes a string to a text file"""
    with open(filename, 'w', encoding='UTF-8') as f:
        retValue = f.write(text)
        return (retValue)
