#!/usr/bin/python3
"""A module that deals with inheritance"""


class MyList(list):
    """An inherited class"""
    def print_sorted(self):
        new = sorted(self)
        print(new)
