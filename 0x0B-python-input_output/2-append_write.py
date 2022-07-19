#!/usr/bin/python3
"""A magical module"""


def append_write(filename="", text=""):
    """A function that writes module"""
    with open(filename, 'a', encoding='utf-8') as f:
        return (f.write(text))
