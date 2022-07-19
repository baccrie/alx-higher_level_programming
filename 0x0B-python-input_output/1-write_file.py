#!/usr/bin/python3
"""A magical module"""


def write_file(filename="", text=""):
    """A function that writes module"""
    with open(filename, 'w', encoding='utf-8') as f:
        return (f.write(text))
