#!/usr/bin/python3


"""A module that does wonder"""


def read_file(filename=""):
    """Function opens a file for.reading"""
    with open(filename, encoding="UTF-8") as f:
        print(f.read())
