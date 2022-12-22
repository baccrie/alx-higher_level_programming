#!/usr/bin/python3


"""A module that does wonder"""

def append_write(filename="", text=""):
    """Function that writes a string to a text file"""
    with open(filename, 'a', encoding='UTF-8') as f:
        f.write(text)
